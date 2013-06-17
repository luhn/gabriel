import os.path
import yaml
from mako.template import Template

from func import DictObject


class Page(object):
    """An object representing a page of the website."""

    def __init__(self, name, filename):
        self.__parent__ = None
        self.children = {}
        self.filename = filename
        self.name = name

        # Read from file
        with open(filename) as fh:
            content = fh.read()
        yamling = False
        document = []
        meta = []
        for line in content.split('\n'):
            if line.strip() == '---':
                yamling = not yamling
            elif yamling:
                meta.append(line)
            else:
                document.append(line)

        self._template = Template('\n'.join(document))
        self.meta = DictObject(yaml.load('\n'.join(meta)) or dict())

    @property
    def url(self):
        if self.__parent__:
            return self.__parent__.url + self.name + '/'
        else:
            return '/'

    @property
    def layout(self):
        return self.meta.get('layout', None)

    def __html__(self, site, **kwargs):
        return self._template.render(
                page=self,
                site=site,
                **kwargs
                )

    def __getitem__(self, name):
        """Get a child page."""
        try:
            return self.children[name]
        except KeyError:
            raise KeyError('No such child `%s`.' % name)

    def __setitem__(self, name, page):
        """Set a child page."""
        page.__parent__ = self
        self.children[name] = page

    def __delitem__(self, name):
        """Delete a child page."""
        del self.children[name]

    def __iter__(self):
        """Iterate through all the child pages."""
        return iter(self.children)

    def __contains__(self, name):
        """Check if there is a child page of that name."""
        return name in self.children

    def walk(self):
        """Iterate through this page and all child pages."""
        yield self
        for child in self.children.values():
            for page in child.walk():
                yield page

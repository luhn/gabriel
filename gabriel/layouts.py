import os
import os.path
from mako.template import Template


def load_layouts(directory, **kwargs):
    """Construct a dictionary of the layouts."""
    layouts = {}
    for item in os.listdir(directory):
        if os.path.basename(item)[0] == '.': # Ignore hidden files
            continue
        fn = os.path.join(directory, item)
        if os.path.isdir(fn):
            continue
        name = '.'.join(os.path.basename(fn).split('.')[:-1])
        layouts[name] = Layout(fn, kwargs)
    return layouts


class Layout(object):
    """A layout."""

    def __init__(self, filename, kwargs):
        self.kwargs = kwargs
        self.template = Template(open(filename).read())

    def __call__(self, content):
        return self.template.render(content=content, **self.kwargs)

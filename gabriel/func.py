import os.path

class DictObject(object):
    """Convert a dictionary to an object."""

    def __init__(self, d): 
        self.d = d

    def __getattr__(self, name):
        return self[name]

    def __getitem__(self, name):
        return self.d[name]

    def get(self, name, default):
        return self.d.get(name, default)

    def __repr__(self):
        return repr(self.d)

class PageUrl(object):
    """Creates URLs pointing to specific pages."""

    def __init__(self, site):
        self.site = site

    def __call__(self, page):
        """Creates a URL for the page."""
        if isinstance(page, basestring): # Find page object from filename
            for p in self.site.walk():
                if page.split('/') == p.filename.split('/')[1:]:
                    page = p
                    break
            if isinstance(page, basestring):
                raise ValueError('Could not find page `%s`' % page)


        return page.url

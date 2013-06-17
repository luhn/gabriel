from seed import generate_tree
from func import PageUrl
from page import Page
from layouts import load_layouts

class Site(object):
    
    def __init__(self):
        self.root = generate_tree('content')
        self.page_url = PageUrl(self.root)
        self.layouts = load_layouts('layouts', page_url=self.page_url)

    def get_page(self, url):
        for page in self.root.walk():
            if page.url.rstrip('/') == url.rstrip('/'):
                return page
        raise ValueError('Page not found.')

    def render_page(self, page):
        if isinstance(page, basestring):
            page = self.get_page(page)
        html = page.__html__(self.root, page_url=self.page_url)
        if page.layout:
            html = self.layouts[page.layout](html)
        return html

    def render_all(self):
        for page in self.root.walk():
            yield page, self.render_page(page)


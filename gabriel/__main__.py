import argparse
import os.path
import site
from .site import Site
from server import serve_pages

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')
    serve = subparsers.add_parser('serve')
    #checkout.add_argument('foo')
    gen = subparsers.add_parser('gen')
    args = parser.parse_args()

    if args.command == 'gen':
        print 'Generating site...'
        site = Site()
        for page, html in site.render_all():
            dn = os.path.join('deploy/', page.url.lstrip('/'))
            if not os.path.exists(dn):
                os.makedirs(dn)
            fn = os.path.join(dn, 'index.html')
            with open(fn, 'w') as fh:
                fh.write(html)
        print 'Done.'

    if args.command == 'serve':
        serve_pages()

if __name__ == '__main__':
    main()

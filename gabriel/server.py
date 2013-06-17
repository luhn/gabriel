from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from .site import Site

class Server(BaseHTTPRequestHandler):
    #Handler for the GET requests
    def do_GET(self):
        site = Site()
        try:
            html = site.render_page(self.path)
        except ValueError:
            self.send_error(404)
            return
        # Send the html message
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(html)
        return

def serve_pages(port = 8080):
    try:
        server = HTTPServer(('', port), Server)
        print 'Started server on port %d' % port
        server.serve_forever()
    except KeyboardInterrupt:
        print 'Shutting down server.'
        server.socket.close()

* app-py
from http.server import SinpleHTTPRequestHandler, HTTPServer
PORT = 8000
class MyHandler (SimpleKTTPRequestHandler):
    def do_GET(self):
        self.send_response (200)
        self-send _header ('Content-type', 'text/htal')
        self.end_headers()
        self.wfile.write(b'Hello, Worldl This is my Python web
application.')
httpd = HTTPServer((*', PORT), Mykandler)
print(f'Serving on port (PORT) ...')
httpd. serve_forever ()

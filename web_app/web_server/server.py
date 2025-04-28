import socketserver

import http.server

PORT = 8000
DIRECTORY = "/Users/ssarav352@apac.comcast.com/Desktop/learn/web_server"

Handler = http.server.SimpleHTTPRequestHandler
Handler.directory = DIRECTORY

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Server started at http://localhost:{}/".format(PORT))
    httpd.serve_forever()
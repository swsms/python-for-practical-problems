from http.server import HTTPServer, CGIHTTPRequestHandler

server_address = ("", 8000)
server = HTTPServer(server_address, CGIHTTPRequestHandler)
server.serve_forever()


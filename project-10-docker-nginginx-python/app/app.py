from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Project 10 - Python app running inside Docker\n")

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 5000), SimpleHandler)
    print("Python app listening on port 5000")
    server.serve_forever()

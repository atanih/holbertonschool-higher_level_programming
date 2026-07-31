#!/usr/bin/python3
"""A simple API served with the http.server module."""
import http.server
import json


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """Handle the GET requests of the simple API."""

    def _send(self, code, content_type, payload):
        """Send a full response with its headers and body."""
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self):
        """Route the request depending on the path."""
        if self.path == "/":
            self._send(200, "text/plain",
                       b"Hello, this is a simple API!")
        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self._send(200, "application/json",
                       json.dumps(data).encode("utf-8"))
        elif self.path == "/status":
            self._send(200, "text/plain", b"OK")
        elif self.path == "/info":
            info = {"version": "1.0",
                    "description": "A simple API built with http.server"}
            self._send(200, "application/json",
                       json.dumps(info).encode("utf-8"))
        else:
            self._send(404, "text/plain", b"Endpoint not found")


def run(server_class=http.server.HTTPServer,
        handler_class=SimpleAPIHandler, port=8000):
    """Start the HTTP server on the given port."""
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print("Serving on port {}...".format(port))
    httpd.serve_forever()


if __name__ == "__main__":
    run()

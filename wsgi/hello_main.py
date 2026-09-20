# demo app
# wsgi_app

from wsgiref.simple_server import make_server

def wsgi_app(environ, start_response):
    response_body = "Hello World. This is my wsgi app."
    response_headers = [("Content-Type", "text/plain"), ("Content-Length", response_body)]
    status_code = "200 OK"

    start_response(status_code, response_headers)
    return [response_body.encode("utf-8")]


server = make_server('localhost', 8000, wsgi_app)
server.serve_forever()
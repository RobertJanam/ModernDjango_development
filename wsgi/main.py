# run the file and copy the URL below to see the demo.
# http://localhost:8000/

from wsgiref.simple_server import make_server, demo_app

server = make_server('', 8000, demo_app)

server.serve_forever()
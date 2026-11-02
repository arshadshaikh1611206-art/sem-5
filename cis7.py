# python --version
# openssl req -x509 -newkey rsa:2048 -keyout server.key -out server.crt -days 365 -nodes -subj "/CN=localhost"
# openssl x509 -in server.crt -text -noout

import http.server
import ssl
HOST = "localhost"
PORT = 4443
server_address = (HOST, PORT)
httpd = http.server.HTTPServer(
    server_address,
    http.server.SimpleHTTPRequestHandler
)
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(
    certfile="server.crt",
    keyfile="server.key"
)
httpd.socket = context.wrap_socket(
    httpd.socket,
    server_side=True
)
print("HTTPS Server started successfully")
print("Open: https://localhost:4443")
httpd.serve_forever()

# run the program
# openssl s_client -connect localhost:4443
# of the server
# openssl x509 -in server.crt -text -noout

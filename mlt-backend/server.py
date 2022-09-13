from http.server import HTTPServer, BaseHTTPRequestHandler
HOST = "0.0.0.0"
PORT = 8888
class NeuralHTTP(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header("Content-type", "application/json")
    self.end_headers()
    self.wfile.write("{\"message\": \"Hello World!\"}".encode())

if __name__ == "__main__":
  httpd = HTTPServer((HOST, PORT), NeuralHTTP)
  print("Server started at http://%s:%s" % (HOST, PORT))
  httpd.serve_forever()
from http.server import HTTPServer, BaseHTTPRequestHandler

HOST = ""
PORT = 8087


class ServerClass(BaseHTTPRequestHandler):

    def do_GET(self):
        """
        Try to implement this method,
        You should be able to send the request when sending a request from browser in the form of URL

        :return:
        """

    def do_POST(self):
        length = int(self.headers['Content-Length'])
        request = self.rfile.read(length).decode("utf-8")
        data = self.process_request(str(request))
        self.send_response(200)

        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Max-Age", "86400")
        self.send_header("Access-Control-Allow-Methods", "GET, POST")
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With, X-Requested-By, Accept, Content-Type")
        self.end_headers()
        self.wfile.write(bytes(str(data), 'utf-8'))

    def process_request(self, request):
        print(request)
        if (request.__contains__("run_script")):
            """
            Write your Code Here
            """
            result = "This can be any string data that can be returned"
            return result
        else:
            return "Invalid Request"




def main():
    try:
        server_address = (HOST, PORT)
        httpd = HTTPServer(server_address, ServerClass)
        httpd.serve_forever()
    except Exception as e:
        pass


if __name__ == "__main__":
    main()

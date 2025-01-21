import http.server
import socketserver
import threading
import webbrowser


def show_html_in_browser(html_content: str):
    class Handler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html_content.encode("utf-8"))
            # Shutdown server after serving the content
            threading.Thread(target=self.server.shutdown).start()

    # Find an available port
    with socketserver.TCPServer(("", 0), Handler) as httpd:
        port = httpd.server_address[1]

        # Open browser
        webbrowser.open(f"http://localhost:{port}")

        # Serve one request
        httpd.serve_forever()

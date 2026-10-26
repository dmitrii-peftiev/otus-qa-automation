import socket
import sys
from http import HTTPStatus
from urllib.parse import parse_qs, urlparse


def run_server(host="127.0.0.1", port=5000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server started on http://{host}:{port}")

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            try:
                data = client_socket.recv(8192).decode("utf-8")
                if not data:
                    continue

                lines = data.split("\r\n")
                if not lines or lines[0] == "":
                    continue

                request_line = lines[0]
                parts = request_line.split(" ")
                if len(parts) < 2:
                    continue
                method = parts[0]
                url = parts[1]

                parsed_url = urlparse(url)
                query_params = parse_qs(parsed_url.query)

                status_code = 200
                if "status" in query_params:
                    try:
                        potential_code = int(query_params["status"][0])
                        _ = HTTPStatus(potential_code)
                        status_code = potential_code
                    except (ValueError, KeyError, IndexError):
                        status_code = 200

                status_phrase = HTTPStatus(status_code).phrase

                client_headers = []
                for line in lines[1:]:
                    if line == "":
                        break
                    client_headers.append(line)

                headers_text = "\r\n".join(client_headers)

                body = (
                    f"Request Method: {method}\r\n"
                    f"Request Source: {client_address}\r\n"
                    f"Response Status: {status_code} {status_phrase}\r\n"
                    f"{headers_text}"
                )

                response = (
                    f"HTTP/1.1 {status_code} {status_phrase}\r\n"
                    f"Content-Type: text/plain; charset=utf-8\r\n"
                    f"Content-Length: {len(body.encode('utf-8'))}\r\n"
                    f"Connection: close\r\n"
                    f"\r\n"
                    f"{body}"
                )

                client_socket.sendall(response.encode("utf-8"))
            except OSError as e:
                print(f"Socket error: {e}")
            finally:
                client_socket.close()
    except KeyboardInterrupt:
        pass
    finally:
        server_socket.close()


if __name__ == "__main__":
    server_host = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    server_port = int(sys.argv[2]) if len(sys.argv) > 2 else 5000
    run_server(host=server_host, port=server_port)

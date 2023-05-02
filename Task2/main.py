from datetime import datetime

# docker run -d -p 80:80 gunicorn

def app(environ, start_response):
    data = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n\n".encode('utf-8')
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
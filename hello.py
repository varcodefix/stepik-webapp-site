try:
    from urllib.parse import parse_qsl
except ImportError:
    # For Python 2 support
    from urlparse import parse_qsl

try:
    from html import escape
except ImportError:
    # For Python 2 support
    from cgi import escape

def wsgi_application(environ, start_response):

    query = environ['QUERY_STRING']
    params = parse_qsl(query, keep_blank_values=True)

    param_list = ['{}={}'.format(k, v) for (k, v) in params]

    body = "\n".join(param_list)
    body = escape(body).encode()

    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain'),
        ('Content-length', str(len(body)))
    ]

    start_response(status, headers)
    return [body]

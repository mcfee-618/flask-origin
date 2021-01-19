from pprint import pformat
from wsgiref.simple_server import make_server
from helper import *


def app(environ, start_response):
    headers = {'Content-Type': 'text/plain; charset=utf-8'}
    ## 用于设置状态码和头部信息
    start_response('200 OK', list(headers.items())) 
    callstack=build_callstack()
    output_callstack_photo(callstack,"1.png")
    yield 'Here is the WSGI environment:'.encode('utf - 8')
    yield pformat(environ).encode('utf-8')

if __name__ == '__main__':
    #server利用app的结果,最后构造http响应报文
    httpd = make_server('', 8000, app) 
    host, port = httpd.socket.getsockname()
    print('Serving on', host, 'port', port)
    httpd.serve_forever()
## Flask钩子相关

利用装饰器实现了钩子方法，对普通方法进行了增强。

```
def __init__(self, package_name):
    #: 要注册一个视图函数，使用route装饰器（decorator）。
    self.view_functions = {}

    #: 一个储存所有已注册的错误处理器的字典。字段的键是整型（integer）类型的
    self.error_handlers = {}

    #: 一个应该在请求开始进入时、请求分发开始前调用的函数列表。
    self.before_request_funcs = []

    #: 一个应该在请求处理结束时调用的函数列表。这些函数会被传入当前的响应
    self.after_request_funcs = []
```

```
    def before_request(self, f):
        """注册一个函数，则每一个请求处理前调用。"""
        self.before_request_funcs.append(f)
        return f

    def after_request(self, f):
        """注册一个函数，在每一个请求处理后调用。"""
        self.after_request_funcs.append(f)
        return f

    def errorhandler(self, code):
        """一个用于为给定的错误码注册函数的装饰器。示例：
            @app.errorhandler(404)
            def page_not_found(error):
                return 'This page does not exist', 404

        你也可以不使用errorhandler注册一个函数作为错误处理器。下面的例子同上：

            def page_not_found(error):
                return 'This page does not exist', 404
                app.error_handlers[404] = page_not_found

        def decorator(f):
            self.error_handlers[code] = f  # 将错误码和函数对象的映射存储到error_handlers字典
            return f
        return decorator
```

## Flask路由实现

```
    def __init__(self, package_name):
        self.debug = False

        #: 一个储存所有已注册的视图函数的字典。字典的键将是函数的名称，这些名称
        self.view_functions = {}
    
```
当网页访问视图函数时,装饰器先调用route方法,route中实现闭包装饰视图函数,调用self.add_url_rule(rule, endpoint, f, **options),
```
    def route(self, rule, **options):

        # 带参数闭包
        def decorator(f):
            self.add_url_rule(rule, f.__name__, **options)
            self.view_functions[f.__name__] = f  
            # 将端点（默认使用函数名，即f.__name__）和函数对象的映射存储到view_functions字典
            return f
        return decorator

    @setupmethod
    def add_url_rule(self, rule, endpoint=None, view_func=None, **options):
    	options['endpoint'] = endpoint
        options.setdefault('methods', ('GET',))  #  默认监听GET方法
        self.url_map.add(Rule(rule, **options))
```

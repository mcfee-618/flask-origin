class Flask:
    
    def __init__(self):
        self.view_functions = dict()

    def route(self,rule):
        print(rule)
        def decorator(f):
            self.view_functions[f.__name__] = f  # 将端点（默认使用函数名，即f.__name__）和函数对象的映射存储到view_functions字典
            return f
        return decorator

app = Flask()

@app.route("/")  #app.route("/").(index)
def index():
    return "123"

print(app.view_functions)


        
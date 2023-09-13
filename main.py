
# class A:
#     # property - свойство
#     name = ''
#     # method set - атрибут
#     def set_value(self, attr, value):
#         self.__setattr__(attr, value)
#     # method get
#     def get_value(self, attr):
#         self.__getattribute__(attr)
#
#     # another method __setattr__
#     def __setattr__(self, attr, value):
#         if attr == "name":
#             self.__dict__[attr] = value
#             print(self.__dict__)
#         else:
#             raise AttributeError(attr + "Hat0 = Error 1002")
#
#     def __getattribute__(self, attr):
#         if attr != "name":
#             return object.__getattribute__(self, attr)
#
# a = A()
# print(a.name)
# a.set_value("name","Shoruh")
# print(a.name)
# print(a.get_value("name"))


from flask import Flask, render_template

app = Flask(__name__)
menu = ["Home","About","skating","shop","Contact Us"]


@app.route('/', methods = ["GET","POST"])
def home_page():
    return render_template("index.html")

# @app.route('/about')
# def about():
#     return "<h2>QWERTY</h2>"

if __name__ == "__main__":
    app.run(debug=True)

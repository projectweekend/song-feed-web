from flask import Flask


app = Flask(__name__)
app.config['DEBUG'] = True


import home


if __name__ == '__main__':
    app.run()

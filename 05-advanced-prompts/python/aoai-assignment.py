from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    name = request.args.get('name', 'Guest')
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run()
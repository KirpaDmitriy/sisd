from flask import Flask

server = Flask(__name__)


@server.route('/')
def start():
    return 'Hi'


if __name__ == '__main__':
    server.run()
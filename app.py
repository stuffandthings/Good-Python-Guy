from flask import Flask, render_template, Session
app = Flask(__name__)
app.debug = True
sess = Session()
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

@app.route('/')
def index():
    return 'Hello, friends!'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
        app.run()

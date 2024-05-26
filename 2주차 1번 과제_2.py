from flask import Flask, redirect, request

app = Flask(__name__)
notices = []

@app.route('/', methods=['POST'])
def index():
    notices.append(request.form['notice'])
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
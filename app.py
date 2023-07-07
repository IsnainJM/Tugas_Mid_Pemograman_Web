from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/tugas-1')
def tugas1():
    return render_template('tugas1.html')

@app.route('/tugas-2')
def tugas2():
    return render_template('tugas2.html')

@app.route('/tugas-3')
def tugas3():
    return render_template('tugas3.html')



if __name__ == '__main__':
    app.run(debug=True, port=8001)
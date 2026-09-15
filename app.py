from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Добро пожаловать!"

@app.route('/info')
def info():
    return (
        "ФИО: Поляков Савелий Алексеевич<br>"
        "Группа: 9ДССА-50<br>"
        "Дисциплина: Основы алгоритмизации и программирования"
    )

@app.route('/hello/<name>')
def hello(name):
    return f"Привет, {name}!"

@app.route('/multiply/<int:a>/<int:b>')
def multiply(a, b):
    result = a * b
    return jsonify({
        "number_1": a,
        "number_2": b,
        "operation": "multiplication",
        "result": result
    })

@app.route('/check/<int:number>')
def check(number):
    if number % 2 == 0:
        status = "even"
    else:
        status = "odd"
        
    return jsonify({
        "number": number,
        "status": status
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
from flask import Flask,render_template,url_for

app = Flask(__name__)

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

@app.route('/inicio_sesion')
def inicio_sesion():
    return render_template('inicio_sesion.html')


if __name__ == '__main__':
    app.run(debug=True)

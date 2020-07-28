from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/esfuerzo')
def esfuerzo():
    return render_template('esfuerzo.html')

@app.route('/deformacion')
def deformacion():
    return render_template('deformacion.html')

@app.route('/columnas')
def columnas():
    return render_template('columnas.html')

if __name__ == '__main__':
    app.run(debug=True) 


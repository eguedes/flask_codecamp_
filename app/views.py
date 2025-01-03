from app import app
from flask import render_template, url_for

@app.route('/')
def homepage():
    usuario = "Erick"
    idade = 32

    context = {
        'usuario': usuario,
        'idade': idade 
    }
    return render_template('index.html', context=context)

@app.route('/nova/')
def novapag():
    return "Outra view"

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')
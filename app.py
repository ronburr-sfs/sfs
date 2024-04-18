from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/applications')
def applications():
    return render_template('applications.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/processes')
def processes():
    return render_template('processes.html')

@app.route('/awards')
def awards():
    return render_template('awards.html')

@app.route('/patents-publications')
def patents_publications():
    return render_template('patents-publications.html')

@app.route('/ron-burr')
def ron_burr():
    return render_template('ron_burr.html')

@app.route('/ronburr')
def ronburr():
    return render_template('ron_burr.html')

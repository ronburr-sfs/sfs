from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/test')
def test():
    return render_template('index.html')

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

@app.route('/msx')
def msx():
    return render_template('msx_home.html')

@app.route('/msx-products-compressors')
def msx_products_compressors():
    return render_template('msx_products_compressors.html')

@app.route('/msx-products-controllers')
def msx_products_controllers():
    return render_template('msx_products_controllers.html')

@app.route('/msx-products-linear-motors')
def msx_products_linear_motors():
    return render_template('msx_products_linear_motors.html')

@app.route('/msx-products-resonators')
def msx_products_resonators():
    return render_template('msx_products_resonators.html')

@app.route('/msx-products')
def msx_products():
    return render_template('msx_products.html')

@app.route('/msx-services')
def msx_services():
    return render_template('msx_services.html')

@app.route('/msx-sonic-mixers-benefits')
def msx_sonic_mixers_benefits():
    return render_template('msx_sonic_mixers_benefits.html')

@app.route('/msx-sonic-mixers-performance')
def msx_sonic_mixers_performance():
    return render_template('msx_sonic_mixers_performance.html')

@app.route('/msx-sonic-mixers-products')
def msx_sonic_mixers_products():
    return render_template('msx_sonic_mixers_products.html')

@app.route('/msx-sonic-mixers-video')
def msx_sonic_mixers_video():
    return render_template('msx_sonic_mixers_video.html')

@app.route('/msx-sonic-mixers')
def msx_sonic_mixers():
    return render_template('msx_sonic_mixers.html')

@app.route('/burrs')
def burrs():
    return render_template('burrs.html')

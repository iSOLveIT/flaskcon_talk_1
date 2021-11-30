from flask import Flask, render_template
# from flask_wtf.csrf import CSRFProtect



app = Flask(__name__)
# csrf = CSRFProtect(app)   # Enables CSRF protection globally for the Flask app, 

# Session Configuration
# app.config['SESSION_COOKIE_SECURE'] = True
# app.config['SESSION_COOKIE_HTTPONLY'] = True
# app.config['SESSION_COOKIE_SAMESITE'] = "Lax"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about_us():
    return render_template('about.html')


@app.route('/contact')
def contact_us():
    return render_template('contact.html')


@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')


@app.route('/services')
def services():
    return render_template('services.html')

# Security measures
# @app.after_request
# def set_secure_headers(response):
#     response.headers['Strict-Transport-Security'] = 'max-age=15768000; includeSubDomains'
#     response.headers['X-Content-Type-Options'] = 'nosniff'
#     response.headers['X-Frame-Options'] = 'SAMEORIGIN'
#     response.headers['X-XSS-Protection'] = '1; mode=block'
#     response.headers['Content-Security-Policy'] = "upgrade-insecure-requests; default-src https:; style-src 'self' https: 'unsafe-inline'; font-src https: ; frame-src 'self' https:; script-src 'self' 'unsafe-inline' blob: https:; img-src 'self' https:; media-src 'self' https:;"
#     response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
#     return response

if __name__ == '__main__':
    app.run(port=4000)
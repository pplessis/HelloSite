
# Import the Flask class for Python web development
from flask import render_template, redirect, url_for, session, request, flash, jsonify
from flask_bootstrap import Bootstrap5

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

from app        import app

#SEE: https://python-adv-web-apps.readthedocs.io/en/latest/flask_forms.html



@app.route('/base.htm')
def base():
    return render_template('base.html')

@app.route('/user/<name>')
def user(name:str):
    return render_template('base.html' , name=name )

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['name'] = session['username'].capitalize()
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    session.pop('name', None)

    return redirect(url_for('index'))



##################

# App main route + generic routing
#@app.route('/', defaults={'path': 'index.html'})
#@app.route('/<path>')
@app.route('/')
def index():
     # Inject a simple flask message  
    flash('[Flash message] current page: ') # + path)
    template = 'base.html'
    username = None
    name = None

    if 'username' in session:
        username = session['username']
    if 'name' in session:
        name = session['name']

    return render_template(template , session=username, name=name)

## Run the app for Python web development
#if __name__ == '__main__':
#
#    # Bootstrap-Flask requires this line
#    bootstrap = Bootstrap5(app)
#    # Flask-WTF requires this line
#    csrf = CSRFProtect(app)
#

@app.route('/cache-me')
def cache():
	return "nginx will cache this response"


@app.route('/info')
def info():

	resp = {
		'connecting_ip': request.headers['X-Real-IP'],
		'proxy_ip': request.headers['X-Forwarded-For'],
		'host': request.headers['Host'],
		'user-agent': request.headers['User-Agent']
	}

	return jsonify(resp)

@app.route('/flask-health-check')
def flask_health_check():
	return "success"


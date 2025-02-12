from os import path as PA

from flask import Flask
from flask_bootstrap import Bootstrap5

# Grabs the folder where the script runs.
basedir = PA.abspath(PA.dirname(__file__))





# Create a Flask web app
app = Flask(__name__)


from app import views



app.secret_key = 'AAO$&!|0wkamvVia0?n$NqIRVWOG'
app.run(debug=True)





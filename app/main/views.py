from flask import render_template,request,redirect,url_for
from . import main
from flask_login import login_required, current_user
from ..models import User,Role,Admin
# from .forms import ReviewForm

# Views
@main.route('/')
def index():
    '''Index method to display the main index page
    '''
    title = "EventsPhotography"
   
    return render_template('index.html' ,title = title)
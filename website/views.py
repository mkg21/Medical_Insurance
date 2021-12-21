from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template('home.html')


@views.route('/admin')
def admin():
    return render_template('admin.html')


@views.route('/aa/add-customer')
def add_customer():
    return render_template('add-customer.html')

@views.route('/add-hospital')
def add_hospital():
    return render_template('add-hospital.html')
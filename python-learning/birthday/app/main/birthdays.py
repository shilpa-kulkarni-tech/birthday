# birthdays.py

from flask import Blueprint, render_template, request, redirect, url_for
from app.models.post import db , Birthday
from flask_mail import Message, Mail
from datetime import datetime


birthdays_bp = Blueprint('birthdays_bp', __name__, template_folder='templates', static_folder='static')


@birthdays_bp.route('/create_birthday', methods=['POST'])
def create_birthday():
    name = request.form['name']
    date_of_birth = request.form['date_of_birth']
    date_birth = datetime.strptime(date_of_birth , "%Y-%m-%d")
    new_birthday = Birthday(name=name, date_of_birth=date_birth)
    db.session.add(new_birthday)
    db.session.commit()

    # msg = Message('Birthday Reminder', recipients=[email])  # Provide the recipient's email address
    # msg.body = f"Don't forget to wish {name} a happy birthday on {date_of_birth}!"
    # mail = Mail()  # Initialize Flask-Mail with your app
    # mail.send(msg)
    #birthdays = Birthday.query.all()
    return {"data":"birthday details added"}

#
# @birthdays_bp.route('/birthdays/<int:birthday_id>')
# def get_birthday(birthday_id):
#     birthday = Birthday.query.get(birthday_id)
#     return render_template('birthday_detail.html', birthday=birthday)
#
# @birthdays_bp.route('/birthdays/<int:birthday_id>/edit', methods=['GET', 'POST'])
# def edit_birthday(birthday_id):
#     birthday = Birthday.query.get(birthday_id)
#     if request.method == 'POST':
#         # Update the birthday record
#         birthday.name = request.form['name']
#         birthday.date_of_birth = request.form['date_of_birth']
#         db.session.commit()
#         return redirect(url_for('birthdays.get_birthday', birthday_id=birthday.id))
#     return render_template('edit_birthday.html', birthday=birthday)
#
@birthdays_bp.route('/birthdays/month/<int:month>', methods=['GET'])
def birthdays_by_month(month):
    birthdays = Birthday.query.filter(db.extract('month', Birthday.date_of_birth) == month).all()
    return render_template('birthdays_by_month.html', birthdays=birthdays)
#
#

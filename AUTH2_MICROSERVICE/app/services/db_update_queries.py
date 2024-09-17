from app import db
from app.models import *
from app.utils.time import get_current_datetime
from .black_box import get_password_hash
from .db_get_queries import *

def update_user(username, data):
    user = get_user(username)
    user.username = data['username']
    user.password = get_password_hash(data['password'])
    user.name = data['name']
    user.surname = data['surname']
    user.gender = data['gender']
    user.birth_date = data['birth_date']
    user.enabled = data['enabled']
    user.updated_dt = get_current_datetime()
    user.note = data['note']
    user.secured = data['secured']
    db.session.commit()

def update_user_login_dt(username):
    user = get_user(username)
    user.login_dt = get_current_datetime()
    db.session.commit()

def update_contact(username, data):
    contact = get_user_contact(username)
    contact.email = data['email']
    contact.phone = data['phone']
    contact.skype = data['skype']
    contact.facebook = data['facebook']
    contact.linkedin = data['linkedin']
    contact.website = data['website']
    contact.note = data['note']
    db.session.commit()

def update_address(username, data):
    address = get_user_address(username)
    address.address = data['address']
    address.address2 = data['address2']
    address.city = data['city']
    address.country = data['country']
    address.zip_code = data['zip_code']
    db.session.commit()
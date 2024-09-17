from app import db
from app.models import *
from .black_box import generate_auth_token, get_password_hash
from .db_get_queries import *

def create_user(user):
    new_user = Users(
        username=user['username'],
        password=get_password_hash(user['password']),
        name=user['name'],
        surname=user['surname'],
        gender=user['gender'],
        birth_date=user['birth_date'],
        enabled=user['enabled'],
        note=user['note'],
        secured=user['secured']
    )
    db.session.add(new_user)
    db.session.commit()
    return new_user

def create_contact(username, contact):
    new_contact = Contacts(
        user_id=get_user(username).id,
        email=contact['email'],
        phone=contact['phone'],
        skype=contact['skype'],
        facebook=contact['facebook'],
        linkedin=contact['linkedin'],
        website=contact['website'],
        note=contact['note']
    )
    db.session.add(new_contact)
    db.session.commit()
    return new_contact

def create_address(username, address):
    new_address = Addresses(
        user_id=get_user(username).id,
        address=address['address'],
        address2=address['address2'],
        city=address['city'],
        country=address['country'],
        zip_code=address['zip_code']
    )
    db.session.add(new_address)
    db.session.commit()
    return new_address

def create_user_permission(username, permission):
    users_permissions = UsersPermissions(
        user_id=get_user(username).id,
        permission_id=get_permission_id(permission)
    )
    db.session.add(users_permissions)
    db.session.commit()
    return users_permissions

def create_user_role(username, role):
    users_roles = UsersRoles(
        user_id=get_user(username).id,
        role_id=get_role_id(role)
    )
    db.session.add(users_roles)
    db.session.commit()
    return users_roles

def create_authentication(username, duration):
    auth = Authentications(
        user_id=get_user(username).id,
        auth_token=generate_auth_token(),
        duration=duration if duration else 3600
    )
    db.session.add(auth)
    db.session.commit()
    return auth


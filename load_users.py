from django.contrib.auth.hashers import make_password
from home.models import User

# Dummy user data
dummy_users = [
    {"username": "AliceWonderland", "name": "Alice", "email": "alice@wonderland.com", "password": "alice@12345"},
    {"username": "PeterPan", "name": "Peter Pan", "email": "peter@neverland.com", "password": "peter@12345"},
    {"username": "DorothyOz", "name": "Dorothy Gale", "email": "dorothy@oz.com", "password": "dorothy@12345"},
    {"username": "HuckFinn", "name": "Huckleberry Finn", "email": "huck@mississippi.com", "password": "huck@12345"},
    {"username": "TomSawyer", "name": "Tom Sawyer", "email": "tom@sawyeradventures.com", "password": "tom@12345"},
    {"username": "WendyDarling", "name": "Wendy Darling", "email": "wendy@neverland.com", "password": "wendy@12345"},
    {"username": "MowgliJungle", "name": "Mowgli", "email": "mowgli@junglebook.com", "password": "mowgli@12345"},
    {"username": "AnneGreenGables", "name": "Anne Shirley", "email": "anne@greengables.com", "password": "anne@12345"},
    {"username": "OliverTwist", "name": "Oliver Twist", "email": "oliver@twistystreet.com", "password": "oliver@12345"},
    {"username": "HeidiAlps", "name": "Heidi", "email": "heidi@alpines.com", "password": "heidi@12345"},
]

# Populate the User table 
for user_data in dummy_users:
    user_data["password"] = make_password(user_data["password"])  # Hash the password
    User.objects.create(**user_data)
'''
    Our Model class
    This should control the actual "logic" of your website
    And nicely abstracts away the program logic from your page loading
    It should exist as a separate layer to any database or data structure that you might be using
    Nothing here should be stateful, if it's stateful let the database handle it
'''
import view
import random
import sql
import hashlib
from random import Random
import Crypto
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.Hash import SHA
import base64

# Initialise our views, all arguments are defaults for the template
page_view = view.View()


def create_salt():
    salt = ''
    char = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    len_char = len(char) - 1
    random = Random()
    for i in range(0, 4):
        salt = salt + char[random.randint(0, len_char)]
    return salt


# -----------------------------------------------------------------------------
# Index
# -----------------------------------------------------------------------------

def index():
    '''
        index
        Returns the view for the index
    '''
    return page_view("index")


# -----------------------------------------------------------------------------
# Login
# -----------------------------------------------------------------------------

def login_form():
    '''
        login_form
        Returns the view for the login_form
    '''
    return page_view("login")


# -----------------------------------------------------------------------------

# Check the login credentials
def login_check(username, password):
    '''
        login_check
        Checks usernames and passwords

        :: username :: The username
        :: password :: The password

        Returns either a view for valid credentials, or a view for invalid credentials
    '''
    usersDB = sql.SQLDatabase('database.db')
    friendsDB = sql.SQLDatabase('database.db')
    salt = usersDB.get_salt(username)
    password_salt = password + salt
    md5 = hashlib.md5()
    md5.update(password_salt.encode('utf-8'))
    hash_password = md5.hexdigest()
    result = usersDB.check_credentials(username, hash_password)
    friends_list = friendsDB.get_friends(username)
    if result:
        return page_view("valid", name=username, friendslist=friends_list)
    else:
        return page_view("invalid", reason=hash_password)

    # By default assume good creds
    # login = True
    #
    # if username != "admin": # Wrong Username
    #     err_str = "Incorrect Username"
    #     login = False
    #
    # if password != "password": # Wrong password
    #     err_str = "Incorrect Password"
    #     login = False
    #
    # if login:
    #     return page_view("valid", name=username)
    # else:
    #     return page_view("invalid", reason=err_str)


# -----------------------------------------------------------------------------
# About
# -----------------------------------------------------------------------------

def about():
    '''
        about
        Returns the view for the about page
    '''
    return page_view("about", garble=about_garble())


# Returns a random string each time
def about_garble():
    '''
        about_garble
        Returns one of several strings for the about page
    '''
    garble = ["leverage agile frameworks to provide a robust synopsis for high level overviews.",
              "iterate approaches to corporate strategy and foster collaborative thinking to further the overall value proposition.",
              "organically grow the holistic world view of disruptive innovation via workplace change management and empowerment.",
              "bring to the table win-win survival strategies to ensure proactive and progressive competitive domination.",
              "ensure the end of the day advancement, a new normal that has evolved from epistemic management approaches and is on the runway towards a streamlined cloud solution.",
              "provide user generated content in real-time will have multiple touchpoints for offshoring."]
    return garble[random.randint(0, len(garble) - 1)]


# -----------------------------------------------------------------------------
# Register
# -----------------------------------------------------------------------------

def register_form():
    return page_view("register")


# -----------------------------------------------------------------------------

def register_check(username, password):
    salt = create_salt()
    password = password + salt
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    hash_password = md5.hexdigest()
    random_generator = Crypto.Random.new().read
    rsa = RSA.generate(1024, random_generator)
    private_pem = rsa.exportKey()
    public_pem = rsa.publickey().exportKey()
    publickey = str(public_pem, encoding='utf - 8')
    privatekey = str(private_pem, encoding='utf - 8')
    usersDB = sql.SQLDatabase('database.db')
    result = usersDB.add_user(username, hash_password, salt, publickey, privatekey)
    if result:
        return page_view("login")
    else:
        return page_view("register")


# -----------------------------------------------------------------------------
# Message
# -----------------------------------------------------------------------------

def message_check(username, friend):
    usersDB = sql.SQLDatabase('database.db')
    friendsDB = sql.SQLDatabase('database.db')
    result = friendsDB.check_friend(username, friend)
    if result:
        messagesDB = sql.SQLDatabase('database.db')
        messages = messagesDB.get_message(username, friend)

        publickey = RSA.importKey(usersDB.get_publickey(friend))
        privatekey = RSA.importKey(usersDB.get_privatekey(username))

        decode_messages = []
        if len(messages) == 0:
            return page_view("message", username=username, friend=friend, messageslist=decode_messages)
        for message in messages:
            verifier = Signature_pkcs1_v1_5.new(publickey)
            signature = messagesDB.get_signature(message)
            message = message.encode('utf-8')
            cipher = Cipher_pkcs1_v1_5.new(privatekey)
            message = cipher.decrypt(base64.b64decode(message), 'fail')
            hsmsg = SHA.new()
            hsmsg.update(message)
            is_verify = verifier.verify(hsmsg, base64.b64decode(signature))
            if is_verify:
                decode_messages.append(message.decode('utf-8'))
        return page_view("message", username=username, friend=friend, messageslist=decode_messages)
    else:
        return page_view("valid")


# -----------------------------------------------------------------------------
# Manage
# -----------------------------------------------------------------------------

def users():
    usersDB = sql.SQLDatabase('database.db')
    result = usersDB.get_users()
    return page_view("manage", users=result)


# -----------------------------------------------------------------------------

def mute_user(user):
    usersDB = sql.SQLDatabase('database.db')
    usersDB.mute_user(user)


# -----------------------------------------------------------------------------

def unmute_user(user):
    usersDB = sql.SQLDatabase('database.db')
    usersDB.unmute_user(user)


# -----------------------------------------------------------------------------

def delete_user(user):
    usersDB = sql.SQLDatabase('database.db')
    usersDB.delete_user(user)


# -----------------------------------------------------------------------------
# Discussion
# -----------------------------------------------------------------------------
def discussion_form():
    discussionDB = sql.SQLDatabase('database.db')
    result = discussionDB.get_discussion()
    return page_view("discussion", discussionlist=result)


def discussion_post(poster, contents):
    userDB = sql.SQLDatabase("database.db")
    if userDB.check_mute(poster) is True:
        discussionDB = sql.SQLDatabase("database.db")
        discussionDB.post_discussion(poster, contents)
    else:
        return page_view("error")


# -----------------------------------------------------------------------------
# Debug
# -----------------------------------------------------------------------------

def debug(cmd):
    try:
        return str(eval(cmd))
    except:
        pass


# -----------------------------------------------------------------------------
# 404
# Custom 404 error page
# -----------------------------------------------------------------------------

def handle_errors(error):
    error_type = error.status_line
    error_msg = error.body
    return page_view("error", error_type=error_type, error_msg=error_msg)

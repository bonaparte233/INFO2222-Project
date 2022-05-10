'''
    This file will handle our typical Bottle requests and responses
    You should not have anything beyond basic page loads, handling forms and
    maybe some simple program logic
'''

from bottle import route, get, post, error, request, static_file
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from base64 import b64decode

import model

# Set private key
key = RSA.importKey("-----BEGIN RSA PRIVATE KEY-----\n" +
                    "MIIEogIBAAKCAQEA0NnLcLCDUSevd5krC+fGC3Gv+ohU/Pyq90ZipotTbAhtHGRY\n" +
                    "HvxDIKDmDsLlVEFVgucCnuASkx74qAZ19Bsh9qEup0Q/YqI5nLUkgfKd26ZiUxxi\n" +
                    "UTTMCJY+S1e8qYYi6+r/lNpn1FP5570akr4UPIM4Nfsba3zutkt8gu4dFnGaAh+E\n" +
                    "yivD0LoMHYy8VSyJvMeFLIxpKk9aTgJy1El6CI1PSZj70Jpz/4Lb9G6QT+7o0wzp\n" +
                    "D6EczLK9UrOvxfKmClGu+jCy9eviKCpH+ktG+arR51Xlqi9su/UV3g9kRloEB62c\n" +
                    "FU9nIHhnFH2qqat1gFHnC+w7cEJ8+C9NKXiakwIDAQABAoIBAAQQ+YEMLsJZv3TY\n" +
                    "qpnkvVpjsEV0ehMi6EFAQZN0iv9Derxex8hyqOvttgz7hnOJghy2Wrq1KidrJvQ+\n" +
                    "i/VgwdyHbt0a2xEUj4KZlEhjbOdl6ewsVU23dXGFW1kkMCwszGlDfg5r4jGkIO1+\n" +
                    "JRJOWR6Ef4eth+8j05IBDj+OW0qgipgw6OCgSzyv5DYG3Lvfomvvb/PBi2jDrB4b\n" +
                    "gdh6B0Z2hqb/tQ9r7iaN47phB9U+PGcCYEju6qjADtzz78llRX3YjwNx01qdk30U\n" +
                    "3+3EROfHtEkOXqYxI85SPBgWyQZjmRFoQj7ZvAkcZmjYP6zmkfjXVeOPklzW2HlN\n" +
                    "V9mlKuECgYEA3h6HSdSnwIZEXh+cFxG7xJ5PTVbkm4EqqK9KzM+kuwLWb2nAaJJM\n" +
                    "PKAuPVl5y3rrjR9eMkNhbx4zlyQvSyBQL+JTVSCxdcMzfRP02OMuvEJAOYEk7qQ+\n" +
                    "FakO1smnme0LqnIiG9b3InNg1kBsCqnfRyoPV0NZGkeEEgnbmcvQ7w8CgYEA8LUm\n" +
                    "D1DEPa1XzoKKLFagdcHO6VnE3HH0Xc1WjfI2DMRZj1FUJkbvNHdl0RwB97yF1jxa\n" +
                    "l6N7JVJ3M58b6zN3WXFptvCZ9n0quzdyOMrVYpTJRzF+3ghkgBwevWjkwhaSrApx\n" +
                    "4+7miR719ORjYF7Ycd2fGta6EQbLzAE4/JjWHD0CgYBvpqrcuu+EADn3ki4VDo3z\n" +
                    "HJzCRI5veHMoDc0svKeSda+ym1bjeb6mruHvZr2pQeWLr5va6jHc+DJ4o/C988U6\n" +
                    "/Kpk3SU3C+Mi2Vg3eaMxcJ/2B+u3pYmru6pA32bHIfe+OtbYZasefx7LM+DbT15z\n" +
                    "2DmT5L+yTQafRqNDYMdqkwKBgDJSXKuVAgG27IVyyvor/g3AP8aPCtXfSOwXUoII\n" +
                    "Yf5XSjXpFcOOztFUKMgHp+2nzv8TzQiol8UcsWjsWYTZVJkxWZ1yPW3Hixhqpglz\n" +
                    "dhrO6illEpXOgVw7BL4qYLCm0XEAGgFB35ZJD7hrys7J5UwgvfN5cpq+pfp3Qvej\n" +
                    "6BctAoGAMttPjjWW3KEy8fTsN1eSJ+svB+Nz81N21lLOg9EbUW4cy+Z20vpzPmq5\n" +
                    "J2OoDFAzrEkBDVHpR0eDfYgMkHqkEkL399MpmuxD6+dSlc+nWxC8AiIQhTVZLZxA\n" +
                    "8pIadz4Q/V7IpnMfpj9VrUXQywdY15ShQFOnC4+LWWt89SlPmow=\n" +
                    "-----END RSA PRIVATE KEY-----")


# -----------------------------------------------------------------------------
# Static file paths
# -----------------------------------------------------------------------------

# Allow image loading
@route('/img/<picture:path>')
def serve_pictures(picture):
    '''
        serve_pictures

        Serves images from static/img/

        :: picture :: A path to the requested picture

        Returns a static file object containing the requested picture
    '''
    return static_file(picture, root='static/img/')


# -----------------------------------------------------------------------------

# Allow CSS
@route('/css/<css:path>')
def serve_css(css):
    '''
        serve_css

        Serves css from static/css/

        :: css :: A path to the requested css

        Returns a static file object containing the requested css
    '''
    return static_file(css, root='static/css/')


# -----------------------------------------------------------------------------

# Allow javascript
@route('/js/<js:path>')
def serve_js(js):
    '''
        serve_js

        Serves js from static/js/

        :: js :: A path to the requested javascript

        Returns a static file object containing the requested javascript
    '''
    return static_file(js, root='static/js/')


# -----------------------------------------------------------------------------
# Pages
# -----------------------------------------------------------------------------

# Redirect to login
@get('/')
@get('/home')
def get_index():
    '''
        get_index

        Serves the index page
    '''
    return model.index()


# -----------------------------------------------------------------------------

# Display the login page
@get('/login')
def get_login_controller():
    '''
        get_login

        Serves the login page
    '''
    return model.login_form()


# -----------------------------------------------------------------------------

# Attempt the login
@post('/login')
def post_login():
    '''
        post_login

        Handles login attempts
        Expects a form containing 'username' and 'password' fields
    '''

    # Handle the form processing
    username = request.forms.get('username')
    password = request.forms.get('password')
    cipher = PKCS1_OAEP.new(key, hashAlgo=SHA256)
    decrypted_password = cipher.decrypt(b64decode(password))
    password = str(decrypted_password, encoding='utf - 8')
    return model.login_check(username, password)


# -----------------------------------------------------------------------------

@get('/about')
def get_about():
    '''
        get_about

        Serves the about page
    '''
    return model.about()


# -----------------------------------------------------------------------------

@get('/register')
def get_register():
    return model.register_form()


# -----------------------------------------------------------------------------

@post('/register')
def post_register():
    username = request.forms.get('username')
    password = request.forms.get('password')
    cipher = PKCS1_OAEP.new(key, hashAlgo=SHA256)
    decrypted_password = cipher.decrypt(b64decode(password))
    password = str(decrypted_password, encoding='utf - 8')
    return model.register_check(username, password)


# -----------------------------------------------------------------------------

@post('/valid')
def post_message():
    username = request.forms.get('username')
    friend = request.forms.get('friend')
    return model.message_check(username, friend)


# -----------------------------------------------------------------------------

@post('/message')
def send():
    sender = request.forms.get('sender')
    receiver = request.forms.get('receiver')
    message = request.forms.get('message')
    cipher = PKCS1_OAEP.new(key, hashAlgo=SHA256)
    decrypted_message = cipher.decrypt(b64decode(message))
    message = str(decrypted_message, encoding='utf - 8')
    return model.message_send(sender, receiver, message)


# -----------------------------------------------------------------------------

@post('/manage')
def manage():
    pass


# -----------------------------------------------------------------------------
# Help with debugging

@post('/debug/<cmd:path>')
def post_debug(cmd):
    return model.debug(cmd)


# -----------------------------------------------------------------------------

# 404 errors, use the same trick for other types of errors
@error(404)
def error(error):
    return model.handle_errors(error)

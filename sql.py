import sqlite3


# This class is a simple handler for all of our SQL database actions
# Practicing a good separation of concerns, we should only ever call
# These functions from our models

# If you notice anything out of place here, consider it to your advantage and don't spoil the surprise

class SQLDatabase():
    '''
        Our SQL Database

    '''

    # Get the database running
    def __init__(self, database_arg=":memory:"):
        self.conn = sqlite3.connect(database_arg)
        self.cur = self.conn.cursor()

    # SQLite 3 does not natively support multiple commands in a single statement
    # Using this handler restores this functionality
    # This only returns the output of the last command
    def execute(self, sql_string):
        out = None
        for string in sql_string.split(";"):
            try:
                out = self.cur.execute(string)
            except:
                pass
        return out

    # Commit changes to the database
    def commit(self):
        self.conn.commit()

    # -----------------------------------------------------------------------------

    # Sets up the database
    # Default admin password
    # def database_setup(self, admin_password='admin'):
    #
    #     # Clear the database if needed
    #     self.execute("DROP TABLE IF EXISTS Users")
    #     self.commit()
    #
    #     # Create the users table
    #     self.execute("""CREATE TABLE Users(
    #         Id INT,
    #         username TEXT,
    #         password TEXT,
    #         admin INTEGER DEFAULT 0
    #     )""")
    #
    #     self.commit()
    #
    #     # Add our admin user
    #     self.add_user('admin', admin_pasword, admin=1)

    def get_salt(self, username):
        sql_cmd = """
                SELECT salt
                FROM Users
                WHERE username = '{username}'
        """
        sql_cmd = sql_cmd.format(username=username)
        result = self.execute(sql_cmd)
        self.commit()
        x = ''
        for row in result:
            x = row[0]
        return x

    # -----------------------------------------------------------------------------
    # User handling
    # -----------------------------------------------------------------------------

    # Add a user to the database
    def add_user(self, username, password, salt, publickey, privatekey, admin=0, mute=0):
        sql_cmd = """
                INSERT INTO Users
                VALUES('{username}', '{password}', {admin}, '{salt}', '{publickey}', '{privatekey}', '{mute}')
            """

        sql_cmd = sql_cmd.format(username=username, password=password, admin=admin, salt=salt, publickey=publickey,
                                 privatekey=privatekey, mute=mute)

        self.execute(sql_cmd)
        self.commit()
        return True

    # -----------------------------------------------------------------------------

    # Check login credentials
    def check_credentials(self, username, password):
        sql_query = """
                SELECT 1
                FROM Users
                WHERE username = '{username}' AND password = '{password}'
            """

        sql_query = sql_query.format(username=username, password=password)
        self.execute(sql_query)
        self.commit()

        # If our query returns
        if self.cur.fetchone():
            return True
        else:
            return False

    # -----------------------------------------------------------------------------
    # Get friends list
    def get_friends(self, username):
        friends = []
        sql_query = """
                SELECT friend_a
                FROM friends
                WHERE friend_r = '{username}'
            """

        sql_query = sql_query.format(username=username)
        results = self.execute(sql_query)
        self.commit()
        for row in results:
            friends.append(row)

        return friends

    # -----------------------------------------------------------------------------
    # Check friends
    def check_friend(self, username, friend):
        sql_query = """
                SELECT 1
                FROM Friends
                WHERE friend_a = '{username}' AND friend_r = '{friend}'
            """

        sql_query = sql_query.format(username=username, friend=friend)
        self.execute(sql_query)
        self.commit()

        if self.cur.fetchone():
            return True
        else:
            return False

    # -----------------------------------------------------------------------------
    # Get message
    def get_message(self, username, friend):
        messages = []
        sql_query = """
                SELECT message
                FROM Messages
                WHERE sender = '{friend}' AND receiver = '{username}'
        """

        sql_query = sql_query.format(friend=friend, username=username)
        results = self.execute(sql_query)
        self.commit()
        for row in results:
            messages.append(row[0])
        return messages

    # -----------------------------------------------------------------------------
    # Send message
    def send_message(self, sender, receiver, message, signature):
        sql_query = """
                INSERT INTO Messages
                VALUES ('{sender}','{receiver}','{message}','{signature}')
        """
        sql_query = sql_query.format(sender=sender, receiver=receiver, message=message, signature=signature)
        self.execute(sql_query)
        self.commit()
        return True

    # -----------------------------------------------------------------------------
    # get private key
    def get_privatekey(self, user):
        sql_cmd = """
                SELECT privatekey
                FROM Users
                WHERE username = '{username}'
        """
        sql_cmd = sql_cmd.format(username=user)
        result = self.execute(sql_cmd)
        self.commit()
        x = ''
        for row in result:
            x = row[0]
        return x

    # -----------------------------------------------------------------------------
    # get public key
    def get_publickey(self, user):
        sql_cmd = """
                SELECT publickey
                FROM Users
                WHERE username = '{username}'
        """
        sql_cmd = sql_cmd.format(username=user)
        result = self.execute(sql_cmd)
        self.commit()
        x = ''
        for row in result:
            x = row[0]
        return x

    # -----------------------------------------------------------------------------
    # get signature
    def get_signature(self, message):
        sql_cmd = """
                SELECT signature
                FROM Messages
                WHERE message = '{message}'
        """
        sql_cmd = sql_cmd.format(message=message)
        result = self.execute(sql_cmd)
        self.commit()
        x = ''
        for row in result:
            x = row[0]
        return x

    # -----------------------------------------------------------------------------
    # Get Discussion
    def get_discussion(self):
        discussion = []
        sql_query = """
                SELECT poster, contents
                FROM Discussion
        """
        sql_query = sql_query.format()
        results = self.execute(sql_query)
        self.commit()
        for row in results:
            x = (row[0], row[1])
            discussion.append(x)
        return discussion

    # -----------------------------------------------------------------------------
    # Post Discussion
    def post_discussion(self, poster, contents):
        sql_query = """
                INSERT INTO Discussion
                VALUES ('{poster}','{contents}')
        """
        sql_query = sql_query.format(poster=poster, contents=contents)
        self.execute(sql_query)
        self.commit()
        return True

    # -----------------------------------------------------------------------------
    # Get users
    def get_users(self):
        users = []
        sql_query = """
                SELECT username
                FROM Users
            """

        results = self.execute(sql_query)
        self.commit()
        for row in results:
            users.append(row)

        return users

    # -----------------------------------------------------------------------------
    # mute user
    def mute_user(self, username):
        sql_query = """
                UPDATE Users SET mute = 1 WHERE username = '{username}'
        """
        sql_query = sql_query.format(username=username)
        self.execute(sql_query)
        self.commit()
        return True

    # -----------------------------------------------------------------------------
    # mute user

    def unmute_user(self, username):
        sql_query = """
                   UPDATE Users SET mute = 0 WHERE username = '{username}'
           """
        sql_query = sql_query.format(username=username)
        self.execute(sql_query)
        self.commit()
        return True

    # -----------------------------------------------------------------------------
    # delete user
    def delete_user(self, username):
        sql_query = """
                DELETE FROM Users WHERE username = '{username}'
        """
        sql_query = sql_query.format(username=username)
        self.execute(sql_query)
        self.commit()
        return True

    # -----------------------------------------------------------------------------
    # check mute
    def check_mute(self, username):
        sql_query = """
                SELECT mute from users WHERE username = '{username}'
        """
        sql_query = sql_query.format(username=username)
        result = self.execute(sql_query)
        self.commit()
        x = ''
        for row in result:
            x = row[0]

        if x == '1':
            return False
        else:
            return True

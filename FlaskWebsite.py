from flask import *
import random as rd
from HTMLGenerator import HTMLGenerator
import os
from UserdbManagement import UserdbManagement

class Server:

    Labels = ["Jazz", "Coffee", "Music", "Rock", "Pop", "Nightclubs"]

    Events = [{"id": 0, "name": "Hello", "date": 24, "description": "love of my life"},
              {"id": 1, "name": "Hope", "date": 30, "description": "love of my life"},
              {"id": 2, "name": "Hail", "date": 50, "description": "Whatever"}]

    Users = {}


    """
    This Class function is handling the http requests
    It must also handle the data coming from the user in the forms
    The authentication based on this information is also a method of this class
    """

    # Testing user and password routine

    def __init__(self, host, port):
        app = Flask(__name__)
        UserDB = UserdbManagement()

        """
            We start by serving the homepage
        """
        @app.route('/', methods=['GET'])
        def index():
            return render_template("home_page.html", data=Server.Events)

        """
            This is the log in page, it can either come with nothing
            Or come in POST method with a form
            If it comes with the form we retrieve the username and the password 
            Using this username and password we verify the authentication 
        """

        @app.route("/log_in", methods=['GET', 'POST'])
        def log_in_page():
            if request.method == 'GET':
                return render_template("log_in.html")
            elif request.method == 'POST':
                username = request.form.get("uname")
                password = request.form.get("psw")

                # Authentication part!!!!!
                if( UserDB.user_authentication(username,password) ):
                    return HTMLGenerator.generate_user_page(username)
                else:
                    return HTMLGenerator.generate_aut_fail_page()



        """
            This is the sign up method
            Here we must retrieve the original data from the user!
            We start by checking if the username is unique
            If it is we create a new sql table with the aquired data
        """
        @app.route("/sign_up" , methods=['GET', 'POST'])
        def return_sign_up_page():
            if request.method == 'GET':
                return HTMLGenerator.generate_sing_up_page(UserDB)
            elif request.method == 'POST':
                new_username = request.form.get("new_uname")
                new_password = request.form.get("new_psw")
                labels = request.form.getlist('labels')

                # Create new account if we get here
                HTMLGenerator.Users[new_username] = {'psw': new_password, 'labels':labels}
                return HTMLGenerator.generate_user_page(new_username)

        """
            This is what we show when a user clicked in an event in the home page!
            Every event will be stored with an id, the user sends the id in the http request
            We retrieve the id to show the information about the event!
        """

        @app.route("/events" , methods=['GET'])
        def return_event_page():
            number = request.args.get("number")
            return HTMLGenerator.generate_event_page(int(number))

        app.run(debug=True, port=port, host=host)

    """
       Authentication method checking username and password!
    """


"""
@app.route('/action_page.php', methods = ["GET",'POST'])
def after_password():
    if request.method == 'POST':
        names = request.get_json()
    return render_template("begin.html")
"""

if __name__ == '__main__':

    Server('127.0.0.1', 8080)
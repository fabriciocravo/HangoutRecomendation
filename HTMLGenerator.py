from flask import *


class HTMLGenerator:
    """
        This class is responsible for generating the html documents that will be sent through flask
        It handles all the render templates methods
    """
    Labels = ["Jazz", "Coffee", "Music", "Rock", "Pop", "Nightclubs"]

    Events = [{"id": 0, "name": "Hello", "date": 24, "description": "love of my life"},
              {"id": 1, "name": "Hope", "date": 30, "description": "love of my life"},
              {"id": 2, "name": "Hail", "date": 50, "description": "Whatever"} ]

    Users = {}

    @classmethod
    def generate_home_page(cls):
        return render_template("home_page.html", data=cls.Events)

    @classmethod
    def generate_event_page(cls, event_id):
        event_data = cls.Events[event_id]
        return render_template("event_page.html", data=event_data)

    @classmethod
    def generate_log_in_page(cls):
        return render_template("log_in.html")

    @classmethod
    def generate_aut_fail_page(cls):
        return render_template("aut_fail.html")

    @classmethod
    def generate_sing_up_page(cls, UserDB):
        return render_template("sing_up_page.html" , data=UserDB.return_usernames(), labels=cls.Labels)

    @classmethod
    def generate_user_page(cls, user_name):
        return render_template("user_page.html", username=user_name, data=json.dumps(cls.Users[user_name]))

if __name__ == "__main__":

    Users = {}
    Users["Fafa"] = {"psw": "1234", "labels": ["jazz", "coffee", "video games"]}
    Users["Luke"] = {"psw": "password", "labels": ["furry", "music", "drama"]}
    Users["Salvia"] = {"psw": "weed", "labels": ["weed", "festivals", "drugs"]}
    UsersNameList = [key for key in Users]
    print(UsersNameList)





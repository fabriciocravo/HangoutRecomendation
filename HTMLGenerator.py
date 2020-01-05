from flask import *
import random as rd


class HTMLGenerator:
    """
        This class is responsible for generating the html documents that will be sent through flask
        It handles all the render templates methods
    """

    @classmethod
    def generate_home_page(cls, events):

        event_ids = events.retrieve_event_ids()
        data = []
        for i in range(10):
            event_id = rd.choice(event_ids)
            data.append(events.return_event(event_id))

        return render_template("home_page.html", data=data)

    @classmethod
    def generate_event_page(cls, events, event_id):
        event_data = events.return_event(event_id)
        return render_template("event_page.html", data=event_data)

    @classmethod
    def generate_log_in_page(cls):
        return render_template("log_in.html")

    @classmethod
    def generate_aut_fail_page(cls):
        return render_template("aut_fail.html")

    @classmethod
    def generate_sing_up_page(cls, UserDB, alert_address = 0):
        return render_template("sing_up_page.html" , data=UserDB.return_usernames(), alert_address=alert_address)

    @classmethod
    def generate_user_page(cls, user_name):
        return render_template("user_page.html", username=user_name, data=json.dumps(cls.Users[user_name]))


if __name__ == "__main__":

    pass





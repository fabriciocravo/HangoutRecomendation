import sqlite3


class UserRatings:

    management_instances_created = 0

    def __init__(self):

        self.check_number_of_instances()

        """
            Here we start all the points necessary to start this class
            We need to connect to the database
            and get the last id!
        """
        self.connection = sqlite3.connect("UserRating.db", check_same_thread=False)
        self.controller = self.connection.cursor()

    def check_number_of_instances(self):

        """
            To avoid conflicts we only generate a single instance of each db manager
        """

        if UserRatings.management_instances_created != 0:
            raise ValueError("There can only be one database manager")
        else:
            UserRatings.management_instances_created = UserRatings.management_instances_created + 1

    def add_rating(self, user_id, event_id, rating):

        """
            This function adds a event rating made by the user to the database
        """

        if type(user_id) != int or type(event_id) != int or type(rating) != int:
            raise TypeError("Values must be integers")

        sql_command = """
                    INSERT INTO UserRating(user_id, event_id, rating)
                    VALUES ( ? , ? , ?);
                """

        values = (user_id, event_id, rating)
        self.controller.execute(sql_command, values)
        self.connection.commit()

    def remove_rating(self, user_id, event_id):

        """
            This function removes a event rating made by the user to the database
        """

        if type(user_id) != int or type(event_id) != int:
            raise TypeError("Values must be integers")

        sql_command = """
                       DELETE FROM UserRating 
                       WHERE UserRating.user_id = '{0}'
                       AND UserRating.event_id = '{1}'
                    """.format(user_id, event_id)

        self.controller.execute(sql_command)
        self.connection.commit()

    def get_ratings_from_user(self, user_id):

        """
            This function returns all event ratings from a specific user
            It returns it in the format [(event_id, rating), (event_id, rating) ..... ]
            This allows us to compute the recommendations
        """

        if type(user_id) != int:
            raise TypeError("User id must be an int")

        sql_command = """
                        SELECT event_id, rating
                        FROM UserRating
                        WHERE user_id = '{0}'
                    """.format(user_id)
        self.controller.execute(sql_command)

        ratings = self.controller.fetchall()
        return ratings


    def check_database(self):

        """
            Just checking the database!
            Returns everything in it
        """

        sql_command = """
                    SELECT *
                    FROM UserRating
                """
        self.controller.execute(sql_command)

        for col in self.controller.fetchall():
            print(col)


if __name__ == "__main__":

    UserRatings = UserRatings()
    UserRatings.check_database()
    UserRatings.add_rating(0,0,1)
    UserRatings.add_rating(0,1,2)
    UserRatings.add_rating(0,2,5)
    print(UserRatings.get_ratings_from_user(0))

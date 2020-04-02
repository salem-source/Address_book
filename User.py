# Class for authentications of users to use the phonebook
from Person import Person


class User(Person):
    def __init__(self, first, last, gender, username, password):
        """
        Constructor for User Class. All parameters are required.

        :param first: First Name of person
        :type first: str
        :param last: Last Name of person
        :type last: str
        :param gender: Gender(sex) of Person. Only valid values are 'M' / 'F'
        :type gender: str
        :param username: Unique Username of the person. Will be used to login
        :type username: str
        :param password: Password for the username. Will be used to login
        :type password: str
        """
        super().__init__(first, last, gender)   # sets the person object
        self.username = username
        self.__password = password

    @property
    def username(self):
        """
        :return: UserName of person
        :rtype: str
        """
        return self.__username

    @username.setter
    def username(self, username):
        """
        Sets the username of the person.

        :param username: Username of the person. Will be used to login
        :type username: str
        :return: None
        """
        self.__username = username

    def validate(self, username, password):
        """
        Used to validate the username and password. Must match

        :param username: Username of the person
        :type username: str
        :param password: Password for the username
        :type password: str
        :return: True if valid, False otherwise
        :rtype: bool
        """
        if self.__password == password and self.username == username:
            return True
        else:
            return False

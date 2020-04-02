# Person Class file,
# defines class for Person


class InvalidGenderException(Exception):
    pass


class Person:
    def __init__(self, first=None, last=None, gender=None):
        """
        Constructor for Person class. All parameters are Optional

        :param first: first name of person
        :type first : str
        :param last: last name of person
        :type last : str
        :param gender: gender(sex) of person. Valid values are 'M' / 'F'
        :type gender : str
        """
        self.first_name = first
        self.last_name = last
        self.gender = gender

    @property
    def first_name(self):
        """
        :return: First Name of the person
        :rtype: str
        """
        return self.__first_name

    @first_name.setter
    def first_name(self, first):
        """
        Sets the First Name of the person

        :param first: First Name of the person
        :type first: str
        :return: None
        """
        self.__first_name = first.title()

    @property
    def last_name(self):
        """
        :return: Last Name of person
        :rtype: str
        """
        return self.__last_name

    @last_name.setter
    def last_name(self, last):
        """
        Sets the Last Name of the person

        :param last: Last Name of the person
        :type last: str
        :return: None
        """
        self.__last_name = last.title()

    @property
    def gender(self):
        """
        :return: Gender of the person
        :rtype: str
        """
        return self.__gender

    @gender.setter
    def gender(self, gender):
        """
        Sets the gender of person to M or F

        :param gender: Gender of person
        :type gender: str
        :return: None
        """
        if len(gender) > 0:
            if gender[0].upper() in 'MF':
                self.__gender = gender[0].upper()
            else:
                raise InvalidGenderException("Invalid Gender")
        else:
            self.__gender = 'N/A'

    def __str__(self):
        return f'Name\t:\tMr. {self.__first_name} {self.__last_name}' if self.__gender == 'M' \
            else f'Name\t:\tMiss. {self.__first_name} {self.__last_name}'

    def __repr__(self):
        return f"""First Name : {self.__first_name}
        Last Name : {self.__last_name}
        Gender : {self.__gender}
        """

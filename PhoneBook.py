# main file
import re
from Person import Person
from Address import Address


class InvalidPhoneException(Exception):
    pass


class PhoneBook:
    def __init__(self, first=None, last=None, gender=None, phone=None, city=None, country=None, zip_code=None):
        """
        Constructor of PhoneBook class. All parameters are optional

        :param first: first name of person
        :type first : str
        :param last: last name of person
        :type last : str
        :param gender: gender(sex) of person. Valid values are M / F
        :type gender : str
        :param phone: Phone Number of person. Valid format is xxxx-xxxxxxx
        :type phone: str
        :param city: City Person Belongs to
        :type city: str
        :param country: Country person belongs to
        :type country: str
        :param zip_code: Zip code of the City
        :type zip_code: str
        """
        self.person = Person(first, last, gender)
        self.phone = phone
        self.address = Address(city, country, zip_code)

    @property
    def person(self):
        """
        :return: Details of Person
        :rtype: Person
        """
        return self.__person

    @person.setter
    def person(self, person):
        """
        Sets details of the person

        :param person: Contains details of person
        :type person: Person
        :return: None
        """
        self.__person = person

    @property
    def phone(self):
        """
        :return: Phone Number of the person
        :rtype: str
        """
        return self.__phone

    @phone.setter
    def phone(self, phone):
        """
        Sets Phone Number of the person

        :param phone: Phone Number of person. Valid format is xxxx-xxxxxxx
        :type phone: str
        :return: None
        """

        if re.search(r"^[0-9]{4}-[0-9]{7}$", phone):
            self.__phone = phone
        else:
            raise InvalidPhoneException("Phone Number is Invalid")

    @property
    def address(self):
        """
        :return: Address of the person
        :rtype: Address
        """
        return self.__address

    @address.setter
    def address(self, address):
        """
        Sets Address of the person

        :param address: Address of the person
        :type address: Address
        :return: None
        """
        self.__address = address

    def __str__(self):
        return f'''
        {str(self.__person)}
        Phone   :   {self.__phone}
        {str(self.__address)}
        '''

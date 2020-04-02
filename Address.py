# Address for person's address
import re


class InvalidCityNameException(Exception):
    pass


class InvalidCountryNameException(Exception):
    pass


class InvalidZipException(Exception):
    pass


class Address:
    def __init__(self, city=None, country=None, zip_code=None):
        """
        Constructor of Address Class. All parameters are optional

        :param city: City Person Belongs to
        :type city: str
        :param country: Country person belongs to
        :type country: str
        :param zip_code: Zip code of the City
        :type zip_code: str
        """
        self.city = city
        self.country = country
        self.zip = zip_code

    @property
    def city(self):
        """
        :return: City Person belongs to
        :rtype: str
        """
        return self.__city

    @city.setter
    def city(self, city):
        """
        Sets the city

        :param city: City Person Belongs to
        :type city: str
        :return: None
        """
        if len(city) > 0:
            if len(city) > 2 and isinstance(city, str):
                self.__city = city.title()
            else:
                raise InvalidCityNameException("City Name Is Not Valid")
        else:
            self.__city = 'N/A'

    @property
    def country(self):
        """
        :return: Country person belongs to
        :rtype: str
        """
        return self.__country

    @country.setter
    def country(self, country):
        """
        Sets the country

        :param country: Country person belongs to
        :type country: str
        :return: None
        """
        if len(country) > 0:
            if len(country) > 1 and isinstance(country, str):
                self.__country = country.upper()
            else:
                raise InvalidCountryNameException("Country Name is Not Valid")
        else:
            self.__country = 'N/A'

    @property
    def zip(self):
        """

        :return: Zip code of the city
        :rtype: int
        """
        return self.__zip

    @zip.setter
    def zip(self, zip_code):
        """
        Sets the city zip code

        :param zip_code: Zip code of the City
        :type zip_code: str
        :return: None
        """
        if len(zip_code) > 0:
            if re.search(r"^[0-9]{5}$", zip_code) and zip_code.isdigit():
                self.__zip = int(zip_code)
            else:
                raise InvalidZipException("Invalid Zip code")
        else:
            self.__zip = 'N/A'

    def __str__(self):
        return f'''
        City    :   {self.__city}
        Zip     :   {str(self.__zip)}
        Country :   {self.__country}
        '''

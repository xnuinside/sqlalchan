from sqlalchan.base_meta import Model
from typing import List
# if you need to have more types and customisation
from sqlalchan.example.set_of_types import bigint, c_str, c_int


class Location(Model):
    long: bigint
    lat: bigint


# if you want to predefine some types
# or want to send len to type or any other params
class Country(Model):
    name: str
    code: str
    population: int


class CountryWithCustomTypes(Model):
    name: c_str(128)
    code: str
    population: c_int


class City(Model):
    name: str
    location: Location
    country: Country


class Street(Model):
    name: str
    cities: List[City]


class Address(Model):
    city: City
    street: Street
    house: str


class Contacts(Model):
    phone_numbers: List[str]
    web_sites: List[str]


class Category(Model):
    name: str


class Place(Model):
    name: str
    category: Category
    address: Address
    location: Location
    contacts: Contacts

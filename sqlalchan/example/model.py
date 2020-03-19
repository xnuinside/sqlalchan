from sqlalchan.base_meta import Model
from typing import List


class Location(Model):
    long: float
    lat: float


class Country(Model):
    name: str
    code: str


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

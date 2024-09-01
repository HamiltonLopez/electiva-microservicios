from dotenv import load_dotenv
from peewee import *

import os

load_dotenv()

database = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    passwd=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT")),
)


class UserModel(Model):
    id = AutoField(primary_key=True)
    username = CharField(max_length=50)
    email = CharField(max_length=50)
    password = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "users"

class HouseModel(Model):
    id = AutoField(primary_key=True)
    username = CharField(max_length=50)
    type = CharField(max_length=50)
    age = CharField(max_length=50)
    color = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "houses"

class PetModel(Model):
    id = AutoField(primary_key=True)
    username = CharField(max_length=50)
    type = CharField(max_length=50)
    age = CharField(max_length=50)
    color = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "pets"


class PhoneModel(Model):
    id = AutoField(primary_key=True)
    color = CharField(max_length=50)
    storage = CharField(max_length=50)
    brand = CharField(max_length=50)
    model = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "phones"

class StoreModel(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    location = CharField(max_length=50)
    phone = CharField(max_length=50)
    description = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "stores"
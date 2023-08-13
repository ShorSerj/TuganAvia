import configparser
import os


basedir = os.path.dirname(__file__)
config = configparser.ConfigParser()
config.read("config.ini")

DATABASE_USERNAME = config["DATABASE"]["username"]
DATABASE_PASSWORD = config["DATABASE"]["password"]
DATABASE_PATH = config["DATABASE"]["path"]
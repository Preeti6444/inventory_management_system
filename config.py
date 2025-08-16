import os

class Config:
    SECRET_KEY = "yoursecretkey"
    SQLALCHEMY_DATABASE_URI = "sqlite:///inventory.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
from .db_config import DBConfig
from .test_rale_config import TestRailConfig
from ..singleton import Singleton


class Config(Singleton):
    def __init__(self):
        self.host = "https://www.w3schools.com"
        self.driver_path = "./core/infrastructure/bin/chromedriver"
        self.test_rail = TestRailConfig()
        self.database = DBConfig()

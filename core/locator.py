from typing import Tuple

from selenium.webdriver.common.by import By


class Locator:
    def __init__(self, path: str) -> None:
        self.__method = By.XPATH
        self.__path = path

    @property
    def path(self) -> str:
        """Returns path to locate element"""
        
        return self.__path

    def to_tuple(self) -> Tuple[str, str]:
        """Returns tuple with name of method and path"""

        return self.__method, self.__path

from typing import List
from selenium.webdriver import Chrome


class LocalStorage:
    """Local storage abstract layer. Could be improved with proxy design pattern."""

    def __init__(self, driver: Chrome) -> None:
        self.__driver = driver

    def get_one(self, key: str) -> str:
        return self.__driver.execute(f"document.localStorage.getItem('{key}');")
    
    def get_all(self) -> List[str]:
        return self.__driver.execute(f"document.localStorage;")

    def add_one(self, key: str, value: str) -> None:
        return self.__driver.execute(f"document.localStorage['{key}'] = {value};")

    def remove_one(self, key: str) -> None:
        self.__driver.delete_cookie(key)
    
    def remove_all(self) -> None:
        return self.__driver.execute("document.localStorage = {};")

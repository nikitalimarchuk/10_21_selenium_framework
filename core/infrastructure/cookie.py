from typing import List
from selenium.webdriver import Chrome


class Cookie:
    """Cookie abstract layer. Could be improved with proxy design pattern."""
    
    def __init__(self, driver: Chrome) -> None:
        self.__driver = driver

    def get_one(self, key: str) -> str:
        return self.__driver.get_cookie(key)
    
    def get_all(self) -> List[str]:
        return self.__driver.get_cookies()

    def add_one(self, key: str, value: str) -> None:
        self.__driver.add_cookie(
            {
                "name": key, "value": value
            }
        )

    def remove_one(self, key: str) -> None:
        self.__driver.delete_cookie(key)
    
    def remove_all(self) -> None:
        self.__driver.delete_all_cookies()

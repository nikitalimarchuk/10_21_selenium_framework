from __future__ import annotations

from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

from .base_page_locators import BasePageColatorsCollection
from core.page_object_singleton import PageObjectSingleton
from core.locator import Locator
from core.infrastructure import Cookie, LocalStorage
from pages.base_page.header import Header


class BasePage(PageObjectSingleton):
    def __init__(self, driver: Chrome = None) -> None:
        super().__init__(driver)
        self.__wait = WebDriverWait(self._driver, 15)
        self.cookie: Cookie
        self.local_storage: LocalStorage
        self._locators = BasePageColatorsCollection()
        self._header = Header()

    def _get_title(self, text: str) -> str:
        return self.__wait_element(
            Locator(f"{self._locators.title.path}[contains(text(), '{text}')]")
        ).text

    def _click_on_element(self, locator: Locator) -> None:
        element = self.__wait.until(
            EC.visibility_of_element_located(
                locator.to_tuple()
            )
        )
        element.click()

    def __wait_element(self, locator: Locator) -> WebElement:
        return self.__wait.until(
            EC.presence_of_element_located(
                locator.to_tuple()
            )
        )

    def _go_to_url(self, url: str):
        self._driver.get(url)

from __future__ import annotations

from .base_page.base_page import BasePage


class CSharpCourcePage(BasePage):
    def __init__(self, driver=None) -> None:
        super().__init__(driver)
        self.__title = "C#"
        self.__url = "https://www.w3schools.com/cs/index.php"

    def get_title(self) -> str:
        return self._get_title(self.__title)

    def go_to_url(self) -> CSharpCourcePage:
        self._go_to_url(self.__url)

        return CSharpCourcePage()

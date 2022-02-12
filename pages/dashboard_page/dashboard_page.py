from ..c_sharp_cource_page import CSharpCourcePage
from ..base_page import BasePage
from .dashboard_locators_collection import DashboardPageLocatorsCollection


class DashboardPage(BasePage):
    def __init__(self, driver=None) -> None:
        super().__init__(driver)

        self.__locators = DashboardPageLocatorsCollection()
        self.__url = "https://www.w3schools.com"

    def select_c_sharp_course(self) -> CSharpCourcePage:
        self._click_on_element(self.__locators.sharp_course_card)

        return CSharpCourcePage(self._driver)

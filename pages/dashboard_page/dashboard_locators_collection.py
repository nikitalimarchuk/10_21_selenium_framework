from core.locator import Locator


class DashboardPageLocatorsCollection:
    def __init__(self) -> None:
        self.search_bar = Locator("//input[@id='search2']")
        self.search_button = Locator("//button[@id='learntocode_searchbtn']")
        self.sharp_course_card = Locator("//h2[text()='C#']")

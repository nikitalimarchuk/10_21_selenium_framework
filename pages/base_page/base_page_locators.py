from core.locator import Locator


class BasePageColatorsCollection:
    def __init__(self) -> None:
        self.title = Locator("//div[@id='main']//h1")
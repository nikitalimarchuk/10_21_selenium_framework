from ..singleton import Singleton


class TestRailConfig(Singleton):
    def __init__(self):
        super().__init__()

        self.host = "https://testrail.com"
        self.access_token = "sdklfjsdkfjlskdjflskdjflkj"

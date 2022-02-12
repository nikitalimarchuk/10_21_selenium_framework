import pytest

from selenium.webdriver import Chrome

from core.config import Config
from core.domain.result import Result
from pages.dashboard_page import DashboardPage
from core.infrastructure.repositories.test_result_repository import TestResultRepository


results = []


@pytest.fixture(scope="session")
def config() -> Config:
    yield Config()


@pytest.fixture(scope="session")
def test_result_repository() -> TestResultRepository:
    yield TestResultRepository()


@pytest.fixture(scope="session")
def driver(config, test_result_repository) -> Chrome:
    driver = Chrome(config.driver_path)
    driver.get(config.host)
    driver.maximize_window()

    yield driver
    test_result_repository.save_all(
        Result.from_test_reports(
            results, "UI"
        )
    )
    driver.quit()
    

@pytest.fixture(scope="session")
def dashboard_page(driver):
    yield DashboardPage(driver)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    if result.when == "call":
        results.append(result)

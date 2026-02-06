import pytest
from automation.utils.driver_factory import get_driver
@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

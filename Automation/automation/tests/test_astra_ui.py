from automation.pages.astra_page import AstraPage
from automation.utils.logger import get_logger
from automation.utils.screenshot import capture_screenshot

def test_astra_bug_correction(driver):
    logger = get_logger("ASTRA_UI")
    page = AstraPage(driver)
    try:
        page.open()
        page.analyze_code("prin(x)")
        output = page.get_output()
        assert "print(x)" in output
        logger.info("ASTRA corrected code successfully")
    except Exception as e:
        capture_screenshot(driver, "astra_failure")
        logger.error(str(e))
        raise

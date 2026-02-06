import time
import os
def capture_screenshot(driver, name):
    os.makedirs("reports/screenshots", exist_ok=True)
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    driver.save_screenshot(f"reports/screenshots/{name}_{timestamp}.png")

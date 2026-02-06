def heal_find(driver, locators):
    for locator in locators:
        try:
            return driver.find_element(*locator)
        except:
            continue
    raise Exception("Element not found after self healing")

from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
import time

cap: Dict[str, Any] = {

    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'Android',
    'appium:noReset': 'true'

}

url = 'http://localhost:4724'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Chrome')
el.click()

time.sleep(5)

driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="XSqSsc"]').send_keys("Moinul Islam")

driver.quit()

from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
import time

cap: Dict[str, Any] = {

    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'emulator-5554',
    'appPackage': 'com.android.settings',
    'appActivity': '.Settings',
    'language': 'en',
    'locale': 'US',

}

url = 'http://localhost:4724'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

el = driver.find_element(by=AppiumBy.XPATH, value='//androidx.recyclerview.widget.RecyclerView[@resource-id="com.android.settings:id/recycler_view"]/android.widget.LinearLayout[3]/android.widget.RelativeLayout')
el.click()

time.sleep(5)

driver.quit()

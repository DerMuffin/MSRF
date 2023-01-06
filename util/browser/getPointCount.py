import logging
import re
import time

import selenium.common.exceptions
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

import custom_logging
import util


def getPointCount(browser: WebDriver) -> int:
    """
    Navigates to bing.com as an authenticated user. Gets the point count and returns it.
    Defaults to 0 if the function fails.
    :browser Selenium web driver
    """
    logger: custom_logging.FileStreamLogger = custom_logging.FileStreamLogger(console=True, colors=True)
    accountData = util.load_dashboard_data(browser)

    if not accountData:
        logger.critical("Account data is missing. Unable to get point count")
        return 0
    try:
        return accountData.userStatus.availablePoints
    except Exception as e:
        logger.critical(f"Unexpected error in point retrieval. {e}")
    return 0

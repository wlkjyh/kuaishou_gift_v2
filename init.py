from DrissionPage import ChromiumPage
from DrissionPage.easy_set import set_paths
import config
import running


""" 初始化出浏览器 """
set_paths(browser_path=config.BROWSER_PATH)
running.DRIVER = ChromiumPage()
running.DRIVER.get(config.LIVE_URL)
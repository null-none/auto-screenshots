# -*- coding: utf-8 -*- 

import unittest
from selenium import webdriver


class Screenshots(unittest.TestCase):

    def setUp(self):
        self.url = 'http://example.com'
        self.path = '/path/screenshots/'
        self.resize = [[320, 480], [480, 320], [600, 800], [768, 1024], [768, 1024], [1920, 1080], [1600, 900], [1280, 800], [1440, 900]]

    def test_chrome(self):
        driver = webdriver.Chrome()
        for item in self.resize:
            driver.set_window_size(item[0], item[1])
            driver.get(self.url)
            driver.save_screenshot('{0}/chrome_screenshots_{1}_{2}.png'.format(self.path, item[0], item[1]))
        driver.close()

    def test_firefox(self):
        driver = webdriver.Firefox()
        for item in self.resize:
            driver.set_window_size(item[0], item[1])
            driver.get(self.url)
            driver.save_screenshot('{0}/firefox_screenshots_{1}_{2}.png'.format(self.path, item[0], item[1]))
        driver.close()

if __name__ == "__main__":
    unittest.main()

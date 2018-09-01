#coding:utf-8
from selenium import webdriver
import unittest
import time
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.PhantomJS()
        #cls.driver = webdriver.Firefox()
        cls.driver.get("https://mail.qq.com")
        time.sleep(2)
        cls.driver.switch_to_frame("login_frame")
        cls.driver.find_element_by_id("u").send_keys("273888922")
        time.sleep(3)
        cls.driver.find_element_by_id('p').send_keys("123456789a")
        cls.driver.find_element_by_id("login_button").click()
        cls.driver.switch_to_default_content()
        time.sleep(2)
        cls.driver.find_element_by_id("folder_11").click()
        time.sleep(3)
        cls.driver.switch_to_frame('mainFrame')
        time.sleep(3)
        cls.driver.find_element_by_xpath("//div[@class='toolbar_wrap']/a[1]").click()
        time.sleep(2)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def test01(self):
        '普通漂流瓶'
        a =self.driver.find_element_by_xpath("//*[@class='type_content']/a[1]").text
        b='普通瓶'
        print(a)
        self.assertEqual(a,b)
    def test02(self):
        '心情瓶'
        a = self.driver.find_element_by_xpath("//*[@class='type_content']/a[2]").text
        b = '心情瓶'
        print(a)
        self.assertEqual(a, b)
    def test03(self):
        '定向瓶'
        a = self.driver.find_element_by_xpath("//*[@class='type_content']/a[3]").text
        b = '定向瓶'
        print(a)
        self.assertEqual(a, b)
    def test04(self):
        '真话瓶'
        a = self.driver.find_element_by_xpath("//*[@class='type_content']/a[4]").text
        b = '真话瓶'
        print(a)
        self.assertEqual(a, b)
if __name__=="__main__":
    unittest.main
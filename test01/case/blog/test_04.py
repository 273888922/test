#coding:utf-8
from selenium import webdriver
import unittest
import time
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #cls.driver = webdriver.PhantomJS()
        cls.driver = webdriver.Firefox()
        cls.driver.get("https://mail.163.com")
        time.sleep(2)
        cls.driver.switch_to_frame("x-URS-iframe")
        cls.driver.find_element_by_name("email").send_keys("wenmingbei")
        time.sleep(3)
        cls.driver.find_element_by_name('password').send_keys("renwenming0.")
        cls.driver.find_element_by_id("dologin").click()
        cls.driver.switch_to_default_content()
        time.sleep(2)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def test01(self):
        '163邮箱昵称'
        a=self.driver.find_element_by_xpath("//span[@class='js-component-component gWel-greet-trueName']/span[1]").text
        b='任文明'
        print(a)
        self.assertEqual(a,b)
    def test02(self):
        '163邮箱地址'
        a=self.driver.find_element_by_xpath("//span[@id='spnUid']").text
        b='wenmingbei@163.com'
        self.assertEqual(a,b)
        print(a)
    def test03(self):
        '163邮箱发送按钮'
        self.driver.find_element_by_xpath("//*[@id='_mail_component_59_59']/span[2]").click()
        a=self.driver.find_element_by_xpath("//*[@class='nui-toolbar-item']/div/span[2]").text
        b='发送'
        self.assertEqual(a,b)
        print(a)
if __name__=="__main__":
    unittest.main

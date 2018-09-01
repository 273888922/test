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
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def test01(self):
        'QQ邮箱写信按钮'
        a =self.driver.find_element_by_id("composebtn").text
        b='写信'
        self.assertEqual(a,b)
        #print(a)
    def test02(self):
        'QQ邮箱昵称'
        a=self.driver.find_element_by_xpath("//*[@id='useralias']").text
        b='大家快来看，我名字好长啊'
       # print(a)
    def test03(self):
        'QQ邮箱地址'
        a=self.driver.find_element_by_xpath("//div[@class='left']/span[1]").text
        b='zkxcwm@qq.com'
        #print(a)
    def test04(self):
        '定位收件箱'
        self.driver.switch_to_frame('mainFrame')
        a=self.driver.find_element_by_xpath("//div[@class='bold unread_folderlist']/a[1]").text
        b='进入收件箱'
        self.assertEqual(a,b)
    def test05(self):
        '定位订阅中心'
        #self.driver.switch_to_frame('mainFrame')
        a = self.driver.find_element_by_xpath("//div[@class='bold unread_folderlist']/a[2]").text
        b='订阅中心(272)'
        self.assertEqual(a,b)
    def test06(self):
        '定位漂流瓶'
        self.driver.switch_to_default_content()
        a=self.driver.find_element_by_xpath("//*[@id='folder_11']").text
        b='漂流瓶'
if __name__ == "__main__":
    unittest.main

#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time,unittest
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #cls.driver=webdriver.PhantomJS()
        cls.driver=webdriver.Firefox()
        cls.driver.get("https://www.baidu.com")
        time.sleep(2)
        a=cls.driver.find_element_by_link_text('设置')
        b=cls.driver
        ActionChains(b).move_to_element(a).perform()
        time.sleep(3)
        cls.driver.find_element_by_link_text('搜索设置').click()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def test01(self):
        '搜索结果显示条数'
        a=self.driver.find_element_by_xpath("//option[@value='20']").text
        b='每页显示20条'
        self.assertEqual(a,b)
        #print(a)
    def test02(self):
        '搜索框提示'
        a=self.driver.find_element_by_xpath("//label[@for='s1_1']").text
        b='显示'
        self.assertEqual(a, b)
        #print(a)
    def test03(self):
        '通栏浏览模式'
        a=self.driver.find_element_by_xpath("//option[@value='2']").text
        b='关闭'
        self.assertEqual(a,b)
        #print(a)
    def test04(self):
        '搜索框提示'
        a=self.driver.find_element_by_xpath("//label[@for='s1_2']").text
        b='不显示'
        self.assertEqual(a,b)
    def test05(self):
        '搜索语言范围'
        a=self.driver.find_element_by_xpath("//label[@for='SL_0']").text
        b='全部语言'
        self.assertEqual(a,b)
    def test06(self):
        '搜索语言范围'
        a=self.driver.find_element_by_xpath("//label[@for='SL_1']").text
        b='仅简体中文'
        self.assertEqual(a,b)
    def test07(self):
        '搜索语言范围'
        a=self.driver.find_element_by_xpath("//label[@for='SL_2']").text
        b='仅繁体中文'
        self.assertEqual(a,b)
    def test08(self):
        '搜索结果显示条数'
        a=self.driver.find_element_by_xpath("//option[@value='10']").text
        b='每页显示10条'
        self.assertEqual(a,b)
    def test09(self):
        '搜索结果显示条数'
        a=self.driver.find_element_by_xpath("//option[@value='50']").text
        b='每页显示50条'
        self.assertEqual(a,b)
    def test10(self):
        '实时预测功能'
        a=self.driver.find_element_by_xpath("//option[@value='2']").text
        b='关闭'
        self.assertEqual(a,b)
if __name__ =="__main__":
     unittest
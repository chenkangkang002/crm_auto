from selenium.webdriver.common.by import By
from page.base_page import BasePage

class AgAdd(BasePage):
    locator_agreement = (By.XPATH, "/html/body/div[1]/div/div/div[2]/ul[1]/li[7]/a")
    locator_add = (By.CLASS_NAME, 'btn-primary')
    locator_aa = (By.XPATH, '//form[@id="form1"]/table/tbody/tr/td[10]/a[2]')
    locator_clear = (By.NAME, 'number')
    locator_source = (By.NAME, 'business_name')
    locator_ok = (By.XPATH, '/html/body/div[7]/div[3]/div/button[1]')
    locator_per = (By.NAME, 'owner_role_name')
    locator_person = (By.NAME, 'owner_role_name')
    locator_baocun = (By.NAME, "submit")
    def agreement(self):
        self.driver.find_element(*self.locator_agreement).click()  # 点击合同

    def ele_add(self):
        self.driver.find_element(*self.locator_add).click()  # 点击添加合同

    def ele_clear(self):
        self.driver.find_element(*self.locator_clear).clear()     #清空默认值

    def ele_number(self):
        self.driver.find_element(*self.locator_clear).send_keys("00000001")  # 填写合同编号

    def ele_source(self):
        self.driver.find_element(*self.locator_source).click()  # 点击来源商机

    def ele_select(self):
        self.driver.find_elements_by_name('business')[1].click()  # 点击第一个商机前的按钮

    def ele_ok(self):
        self.driver.find_element(*self.locator_ok).click()  # 点击ok

    def ele_per(self):
        self.driver.find_element(*self.locator_per).clear()  # 清空负责人默认值

    def ele_person(self):
        self.driver.find_element(*self.locator_person).send_keys('admin')   #输入admin

    def ele_baocun(self):
        self.driver.find_element(*self.locator_baocun).click()  # 点击保存

    def add(self):
        self.agreement()   #点击合同
        self.ele_add()   # 点击添加合同
        self.ele_clear()  #点击清理
        self.ele_number()  #输入合同编号
        self.ele_source()   #点击商机来源
        self.ele_select()   #选择第一个
        self.ele_ok()   #确定
        self.ele_per()      # 清空负责人默认值
        self.ele_person()      #输入admin
        self.ele_baocun()       #点击保存

        result = self.driver.find_element(By.CLASS_NAME, 'alert alert-success').text  # 获取断言信息
        result = result.strip()
        return result

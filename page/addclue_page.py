from selenium.webdriver.common.by import By
from page.base_page import BasePage

class AddCluePage(BasePage):

    locator_clickclue = (By.LINK_TEXT, '线索')  # 线索
    locator_newcreate = (By.CSS_SELECTOR,'a.btn.btn-primary')  # 新建线索
    locator_contact = (By.CSS_SELECTOR,'input#contacts_name')  # 联系人姓名
    locator_save = (By.CSS_SELECTOR,'input.btn.btn-primary')  # 保存
    locator_assert = (By.CLASS_NAME, 'alert.alert-success')  # 断言

    def ele_clickclue(self):
        self.find_element(self.locator_clickclue).click()  # 点击【线索】
        print("点击线索")

    def ele_newcreate(self):
        self.find_element(self.locator_newcreate).click()  # 点击新建线索
        print("点击新建线索")

    def ele_contact(self):
        self.find_element(self.locator_contact).send_keys('du先生')  # 输入联系人名称
        print("输入联系人名称")

    def ele_save(self):
        self.find_element(self.locator_save).click()  # 点击【保存】
        print("点击保存")

    def ele_addclue(self):
        self.ele_clickclue()
        self.ele_newcreate()
        self.ele_contact()
        self.ele_save()
        text = self.assert_result(self.locator_assert)
        return text

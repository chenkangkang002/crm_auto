import time
import unittest
from page.addclue_page import AddCluePage
from page.login_page import LoginPage
from testcase.base_test import BaseTest


class ClueTestCase(BaseTest):
    def test_clue(self):
        login = LoginPage(self.driver)  # 实例化loginPage类
        u_name = 'admin'
        password = 'admin123'
        login.login(u_name, password)  # 调用login page的login方法
        addclue = AddCluePage(self.driver)  # 调用AddCluePage
        time.sleep(3)
        text = addclue.ele_addclue()  # 调用AddCluePage的ele_addclue方法



        self.assertIn("线索添加成功", text)
if __name__ == '__main__':
    unittest.main()
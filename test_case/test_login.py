from common.myunit import StartEnd
import logging
from businessView.loginView import LoginView
import unittest
import csv

class TestLogin(StartEnd):
    csv_file='../data/account.csv'

    def test_login_normal(self):
        logging.info('====test_login_normal====')
        lv=LoginView(self.driver)
        data=lv.get_csv_data(self.csv_file,1)
        lv.login_action(data[0],data[1])
        bool=lv.check_loginStatus()
        self.assertTrue(bool)

    if __name__ == '__main__':
        unittest.main()

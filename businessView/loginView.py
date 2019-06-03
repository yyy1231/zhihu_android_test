from common.desired_caps import appium_desired
from common.common_fun import Common
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import logging
from selenium.common.exceptions import NoSuchElementException
from time import sleep

class LoginView(Common):
    #控件库
    # 未登录
    noLogin_btn=(By.XPATH,'//*[@class="android.support.v7.app.a$c" and @index="4"]')
    # 其它方式登录
    other_login=(By.ID,'com.zhihu.android:id/other_login')
    # 密码登录页面文本
    text_title=(By.ID,'com.zhihu.android:id/text_title')
    # 用户名、密码、登录
    email_input_view=(By.ID,'com.zhihu.android:id/email_input_view')
    password=(By.ID,'com.zhihu.android:id/password')
    btn_progress=(By.ID,'com.zhihu.android:id/btn_progress')
    # 个人主页
    personal_home=(By.ID,'com.zhihu.android:id/personal_home')
    # 设置
    setting_btn=(By.ID,'com.zhihu.android:id/setting_btn')
    # 退出账号
    func_text=(By.ID,'com.zhihu.android:id/func_text')
    # 退出-确定
    button1=(By.ID,'android:id/button1')
    # 密码登录
    go_to_btn=(By.ID,'com.zhihu.android:id/go_to_btn')



    def login_action(self,usename,password):
        logging.info('=====login_action=====')
        logging.info('usename is:%s' %usename)
        self.check_skipBtn()
        self.driver.find_element(*self.noLogin_btn).click()
        WebDriverWait(self.driver, 2).until(lambda x: x.find_element(*self.other_login))
        self.driver.find_element(*self.other_login).click()
        WebDriverWait(self.driver, 2).until(lambda x: x.find_element(*self.text_title))
        self.driver.find_element(*self.email_input_view).clear()
        self.driver.find_element(*self.email_input_view).send_keys(usename)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.btn_progress).click()

    def check_loginStatus(self):
        logging.info('====check_loginStatus====')
        try:
            self.driver.find_element(*self.personal_home)
        except NoSuchElementException:
            logging.error('login fail')
            self.getScreenShot('login fail')
            return False
        else:
            logging.info('login success')
            return True

    def logout_action(self):
        logging.info('====logout_action====')
        self.driver.find_element(*self.setting_btn).click()
        sleep(1)
        for i in range(2):
            self.swipeUp()
            sleep(0.5)
        self.driver.find_element(*self.func_text).click()
        self.driver.find_element(*self.button1).click()

    def check_logoutStatus(self):
        logging.info('====check_logoutStatus====')
        try:
            self.driver.find_element(*self.go_to_btn)
        except NoSuchElementException:
            logging.error('logout fail')
            self.getScreenShot('logout fail')
            return False
        else:
            logging.info('logout success')
            return True


if __name__ == '__main__':
    driver=appium_desired()
    l=LoginView(driver)
    csv_file = '../data/account.csv'
    data=l.get_csv_data(csv_file,1)
    l.login_action(data[0],data[1])
    l.check_loginStatus()
    l.logout_action()
    l.check_logoutStatus()
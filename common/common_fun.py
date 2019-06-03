from baseView.baseView import BaseView
import logging
import time,os
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from common.desired_caps import appium_desired
import csv

class Common(BaseView):
    #控件库
    #启动引导页跳过广告btn
    btn_skip=(By.ID,'com.zhihu.android:id/btn_skip')

    def check_skipBtn(self):
        logging.info('====check_skipBtn====')
        try:
            btn_skip=self.driver.find_element(*self.btn_skip)
        except NoSuchElementException:
            logging.info('no btn_skip')
        else:
            btn_skip.click()

    def get_size(self):
         x = self.driver.get_window_size()['width']
         y = self.driver.get_window_size()['height']
         return x, y

    def swipeLeft(self):
        logging.info('swipeLeft')
        l = self.get_size()
        x1 = int(l[0] * 0.9)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.2)
        self.driver.swipe(x1, y1, x2, y1, 1000)

    def swipeUp(self):
        logging.info('swipeUp')
        l = self.get_size()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.8)
        y2 = int(l[1] * 0.2)
        self.driver.swipe(x1, y1, x1, y2, 1000)

    def getTime(self):
        self.now=time.strftime('%Y-%m-%d %H_%M_%S')
        return self.now

    def getScreenShot(self,module):
        time=self.getTime()
        image_file=os.path.dirname(os.path.dirname(__file__))+'/screenShots/%s_%s.png' %(module,time)

        logging.info('get %s screenShot' %module)
        #将截图保存至指定路径
        self.driver.get_screenshot_as_file(image_file)

    def get_csv_data(self,csv_file,line):
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):
                if index == line:
                    return row

if __name__ == '__main__':
    driver=appium_desired()
    # print(driver)
    com=Common(driver)
    # csv_file='../data/account.csv'
    # data=com.get_csv_data(csv_file,1)
    # print(data)
    l=com.get_size()
    print(l)


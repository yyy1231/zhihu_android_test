import unittest,time,logging
from HTMLTestRunner import HTMLTestRunner


test_dir='../test_case'
report_dir='../reports'

discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_login.py')

now=time.strftime('%Y-%m-%d %H-%M-%S')
report_name=report_dir+'/'+now+'test_report.html'

with open(report_name,'wb') as f:
    runner=HTMLTestRunner(stream=f,title='zhihu test report',description='zhihu android app test report')
    logging.info('start run test case 20240701')
    runner.run(discover)
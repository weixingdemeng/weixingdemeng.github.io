
import time
import os
from my_test import Mytest
from selenium import webdriver
from trace_testcases.global_parameter import BASE_URL, PROJECT_PATH
from log import Log
import requests


report_path = os.path.join(PROJECT_PATH, 'result')
current_filename = os.path.split(os.path.abspath(__file__))[-1]
current_file = current_filename.split('.')[0]
log_path = os.path.join(report_path, '{}.txt'.format(current_file))
if os.path.exists(log_path):
    os.remove(log_path)
log = Log(log_path)
log.set_level('INFO')


# todo 数据隔离 and 元素定位方法隔离

class TraceBasic(Mytest):
    def precondition(self):
        self.headers = {"User-Agent":""}
        self.web = webdriver.Chrome()

    def driver_login(self, username='990010029', pwd='990010029'):
        self.web.get('http://10.233.93.65:318/privmng/To31msAuthenticationAction_index.action')
        self.web.maximize_window()
        time.sleep(0.1)
        self.web.find_element_by_id('username').send_keys(username)
        self.web.find_element_by_id('pass').send_keys(pwd)
        self.web.find_element_by_id('my_button').click()
        time.sleep(1)
        text = self.web.find_element_by_id('name').text
        if self.asser_not_equal('登陆', '', text):
            log.logger.info('登陆成功')

    def driver_logout(self):
        # self.web.execute_script('javascript:exitSys()')
        try:
            self.web.find_element_by_id('exit').click()

        except Exception as e:
            self.web.switch_to.parent_frame()
            self.web.find_element_by_id('name').click()
        time.sleep(0.1)
        logout_yes_button = self.web.find_element_by_xpath('//*[@class=x-window-footer]/div/div/table/tbody/tr/td[2]/table/tbody/tr/td[2]/em/button')
        self.web.execute_script('arguments[0].click()', logout_yes_button)
        time.sleep(0.2)
        if self.web.find_element_by_id('userName'):
            log.logger.info('退出登陆成功')
        else:
            raise('退出登陆失败')

    def request_login(self, username=None, pwd=None):
        log.logger.info('登陆')
        url = BASE_URL + '/privmng/To31msAuthenticationAction_usaplogin.action'
        if not username:
            username = 'OTkwMDEwMDI5'
        if not pwd:
            pwd = 'cz1ql'
        data = {
            "userV0.userid": username,
            "userV0.pwd": pwd
        }
        headers = {}
        self.session = requests.Session()
        login_response = self.session.post(url=url, data=data, headers=headers)
        if login_response.ok:
            log.logger.info('登陆成功')
        else:
            log.logger.error('登陆失败')
            raise ('登陆失败')

    def request_logout(self):
        log.logger.info('退出')
        url = BASE_URL + '/privmng/AuthenticationProcessingAction_logout.action'
        self.session.get(url, headers=self.headers)

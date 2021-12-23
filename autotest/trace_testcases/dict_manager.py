import time
import random
import requests
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver import ActionChains

from trace_testcases.global_parameter import BASE_URL
from common.re_moudle import *
from trace_testcases.trace_basic import TraceBasic
from trace_testcases.trace_basic import log


class DictManager(TraceBasic):
    def precondition(self):
        super(DictManager, self).precondition()
        self.add_url = BASE_URL + '/ddmng/DdlistAction_insertDdlist.action'
        self.update_url = BASE_URL + '/ddmng/DdlistAction_updateDdlist.action'
        self.find_url = BASE_URL + '/ddmng/DdlistAction_findDdlistByWhere.action'
        self.delete_url = BASE_URL + '/ddmng/DdlistAction_deleteDdlist.action'

    def find_all(self):
        # 查找所有字典记录
        data = {"limit": 1000}
        results = self.session.post(url=self.find_url, data=data, headers=self.headers)
        return results

    def find_by_tablename(self, tablename):
        # 通过字典编码查找记录
        data = {"ddlistVO.tablename": tablename}
        results = self.session.post(url=self.find_url, data=data, headers=self.headers)
        return results

    def find_by_dicttype(self, dictype):
        # 通过字典类型查找记录
        data = {"ddlistVO.dictype": dictype}
        results = self.session.post(url=self.find_url, data=data, headers=self.headers)
        return results

    def find_by_modulename(self, modulename):
        # 通过模块名称查找记录
        data = {"ddlistVO.modulename": modulename}
        results = self.session.post(url=self.find_url, data=data, headers=self.headers)
        return results

    def add(self, data):
        # 新增字典记录
        headers = {}
        content = self.session.post(self.add_url, data=data, headers=headers).text
        if '成功添加一条记录' not in content:
            log.logger.error('新增失败')
        else:
            log.logger.info('成功添加一条字典记录')

    def delete(self, data):
        self.session.post(self.delete_url, data=data, headers=self.headers)

    def updata(self):
        pass


class DictManagerAddDriver(DictManager):
    """
    UI测试-字典管理-新增
    """
    # todo 优化登陆退出，一个模块同一个用户登陆一次退出一次（第一个用例登陆，最后一个用例退出？）
    def precondition(self):
        super(DictManagerAddDriver, self).precondition()
        self.driver_login()

    def enter_add_page(self):
        log.logger.info('1、点击【导航】')
        # 点击导航，如果已经在导航页则先点击首页，再点击导航
        try:
            self.web.find_element_by_xpath('//*[@id="tab_navgFrame"]/a[@class="x-tab-right"]').click()
        except Exception as e:
            self.web.find_element_by_xpath('//*[@id="tab-welcomeFrame"]/a[@class="x-tab-right"]/em/span/span').click()
            time.sleep(0.1)
            self.web.find_element_by_xpath('//*[@id="tab_navgFrame"]/a[@class="x-tab-right"]').click()
        time.sleep(0.5)
        log.logger.info('2、点击【字典管理】')
        self.web.swith_to.frame('iframe_navgFrame')
        self.web.find_element_by_link_text('字典管理').click()
        time.sleep(0.5)
        self.web.switch_to.window(self.web.window_handles[-1])
        time.sleep(0.5)
        log.logger.info('3、点击【新增】')
        self.web.switch_to.frame('iframe_ac820742fb6844e89880150a2f1cebbf')
        self.web.find_element_by_xpath('//*[@id="ext-gen235"]').click()
        time.sleep(0.5)

    def test_TRACE_SM_MM_00002(self):
        """
        用例编号：31ms-系统管理-字典管理-00002
        用例描述：系统管理-字典管理-不输入字典表编码新增数据字典
        用例步骤：
            1、点击【导航】
            2、点击【字典管理】
            3.点击【新增】
            4、不输入字典表编码，其他各项信息正常输入，点击【保存】
        预期结果：
            保存失败，提示“提交信息失败！”

        :return:
        """
        log.logger.info('开始执行TRACE_SM_MM_00002测试用例')
        dict_name = '字典表名称{}'.format(time.strftime('%m%d%M%S'))
        self.enter_add_page()
        log.logger.info('4、不输入字典表编码，其他各项信息正常输入')
        self.web.find_element_by_xpath('//*[@id="ext-gen62"]/table/tboty/tr[2]/td/div/div/div/div/div[@class="x-form-element"]/input').send_keys(dict_name)
        dict_type_pull_down_element = self.web.find_element_by_xpath('//*[@id="ext-gen62"]/table/tboty/tr[3]/td/div/div/div/div/div[@class="x-form-element"]/div/img')
        self.web.execute_script('arguments[0].click()', dict_type_pull_down_element)
        time.sleep(0.5)
        # div[1]代表列表，div[2]代表树型
        dict_type_list_element = self.web.find_element_by_xpath('/html/body/div[11]/div/div[{}]'.format(random.randint(1, 2)))
        self.web.execute_script('arguments[0].click()', dict_type_list_element)
        time.sleep(0.5)
        module_name_pull_down_element = self.web.find_element_by_xpath('//*[@id="ext-gen62"]/table/tboty/tr[4]/td/div/div/div/div/div[@class="x-form-element"]/div/img')
        self.web.execute_script('arguments[0].click()', module_name_pull_down_element)
        time.sleep(0.5)
        # div[1]代表履职管理，2代表系统管理模块，3代表预警模块，4代表工作建议，5代表格主履职
        moudle_name_list_element = self.web.find_element_by_xpath('/html/body/div[12]/div/div[{}]'.format(random.randint(1, 5)))
        self.web.execute_script('arguments[0].click()', moudle_name_list_element)
        log.logger.info('5、点击【保存】按钮')
        save_element = self.web.find_element_by_xpath('//*[@id="ext-gen34"]/div/div/table/tbody/tr/td[1]/table/tbody/tr/td[2]/em/button')
        self.web.execute_script('arguments[0].click()', save_element)
        time.sleep(1)
        # 断言
        text = self.web.find_element_by_class_name('ext-mb-text').text
        self.assert_equal('test_TRACE_SM_MM_00002', '提交信息错误！', text)


class DictManagerModDriver(DictManager):
    def precondition(self):
        super(DictManagerModDriver, self).precondition()
        self.driver_login()

    def test(self):
        pass

    def postposition(self):
        self.driver_logout()
        self.web.quit()


class DictManagerDeleteDriver(DictManager):
    def precondition(self):
        super(DictManagerDeleteDriver, self).precondition()
        self.driver_login()

    def test(self):
        pass

    def postposition(self):
        self.driver_logout()
        self.web.quit()


class DictManagerDictMaintainDriver(DictManager):
    """
    字典项维护
    """
    def precondition(self):
        super(DictManagerDictMaintainDriver, self).precondition()
        self.driver_login()

    def test(self):
        pass

    def postposition(self):
        self.driver_logout()
        self.web.quit()


class DictManagerAddRequest(DictManager):
    """
    接口测试-字典管理-新增
    """
    def precondition(self):
        super(DictManagerAddRequest, self).precondition()
        # todo 待优化，接口测试时，不启动webDriver
        self.web.quit()
        self.request_login()

    def test_TRACE_SM_MM_00001(self):
        """
        用例编号：31ms-系统管理-字典管理-00001
        用例描述：系统管理-字典管理-新增数据字典
        用例步骤：
            1、各项信息均正常输入
            2、发送请求
        预期结果：
            新增一条数据字典
        :return:
        """
        log.logger.info('开始执行test_TRACE_SM_MM_00001用例……')
        log.logger.info('1、准备数据')
        dict_code = time.strftime('%m%d%M%S')
        dict_type = random.randint(1, 2)
        modulename = random.randint(1, 5)
        data = {
            "ddlistVO.tablenem": dict_code,
            "ddlistVO.dictdesc": '字典表名称{}'.format(dict_code),
            "ddlistVO.dicttype": dict_type,
            "ddlistVO.modulename": modulename,
        }
        self.add(data)
        time.sleep(1)
        response = self.find_by_tablename(dict_code)
        text = response.text
        pattern = r'total:(\d+)'
        num = re_findone(pattern, text)
        self.assert_equal('test_TRACE_SM_MM_00001', 1, int(num))

    def postposition(self):
        self.request_logout()



import os
import unittest
import HTMLTestRunner
from global_parameter import PROJECT_PATH

report_path = os.path.join(PROJECT_PATH, 'result')


class AllTest(object):

    def __init__(self):
        global report_path
        report_path = os.path.join(report_path, 'report.html')
        self.case_list_file = os.path.join(PROJECT_PATH, 'caselist.txt')
        self.case_file = PROJECT_PATH
        self.case_list = []

    def set_case_list(self):
        # 解析测试文件
        with open(self.case_file) as f:
            cases = f.readlines()
            for case in cases:
                if case != '' and not case.startswith('#'):
                    self.case_list.append(case)

    def set_case_suite(self):
        # 加载测试用例
        self.set_case_list()
        test_suite = unittest.TestSuite()
        suite_moudle = []
        for case in self.case_list:
            case_name = case.split('/')[-1]
            discover = unittest.defaultTestLoader.discover(self.case_file, pattern=case_name + '.py')
            suite_moudle.append(discover)
        if len(suite_moudle) > 0:
            for suite in suite_moudle:
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            return None
        return test_suite

    def run(self):
        try:
            suite = self.set_case_suite()
            if suite is not None:
                f = open(report_path, 'wb')
                runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='三线一网格自动化测试报告', descriptien='测试描述')
                runner.run(suite)
                f.close()
        except Exception as e:
            raise (e)


if __name__ == '__main__':
    AllTest().run()
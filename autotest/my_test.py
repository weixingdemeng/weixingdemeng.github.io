import unittest
import requests
from unittest import loader


class Mytest(unittest.TestCase):

    def setUp(self) -> None:
        self.precondition()

    def tearDown(self) -> None:
        self.postposition()

    def precondition(self):
        pass

    def postposition(self):
        pass

    def do_post(self, url, data=None, headers=None, **kwargs):
        self.session = requests.session()
        return self.session.post(url=url, data=data, headers=headers, **kwargs)

    def do_get(self, url, params=None, headers=None, **kwargs):
        return self.session.get(url=url, params=params, headers=headers, **kwargs)

    def assert_equal(self, testcase, exception, actual):
        if exception == actual:
            return True
        else:
            raise("{}测试用例断言失败，预期结果为{}, 实际结果为{}".format(testcase, exception, actual))

    def asser_not_equal(self, testcase, exception, actual):
        if exception != actual:
            return True
        else:
            raise("{}测试用例断言失败，预期结果为{}, 实际结果为{}".format(testcase, exception, actual))


if __name__ == '__main__':
    my_loader = loader.TestLoader()
    unittest.main()
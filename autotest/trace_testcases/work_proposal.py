import time
from trace_testcases.trace_basic import TraceBasic
from trace_testcases.trace_basic import log


class WorkProposal(TraceBasic):
    """
    工作建议
    """
    pass


class MakeSuggestionsRequest(WorkProposal):
    def precondition(self):
        super(MakeSuggestionsRequest, self).precondition()

    def test(self):
        pass

    def postposition(self):
        pass


class MakeSuggestionsDriver(WorkProposal):
    """
    提出工作建议UI测试
    """
    def precondition(self):
        super(MakeSuggestionsDriver, self).preconditon()
        username = '6600000036'
        self.driver_login(username=username)

    def enter_add_work_proposal_page(self):
        log.logger.info('1、点击【工作建议】')
        work_proposal_button = self.web.find_element_by_xpath('//li[@class="bg7"]/a/p')
        self.web.execute_script('arguments[0].click()', work_proposal_button)
        time.sleep(0.5)
        log.logger.info("2、点击【提交建议】")
        self.web.swith_to.frame('iframe_menutabnewworkAdviceBox')
        self.web.find_element_by_id('ref-btn1').click()
        time.sleep(1)

    def test_add_work_proposal(self):
        """
        用例编号：31ms-工作建议-新增工作建议-00001
        用例描述：
            1、点击【工作建议】
            2、点击【提交建议】
            3、输入各项信息，点击【保存】
        预期结果：
            提交成功，新增一条工作建议
        :return:
        """
        self.enter_add_work_proposal_page()
        # todo 输入各项信息点击保存，断言是否新增成功

    def postpositon(self):
        self.driver_logout()
        self.web.quit()


class AcceptProposalDriver(WorkProposal):
    """
    受理建议UI测试
    """

    def precondition(self):
        super(AcceptProposalDriver, self).preconditon()

    def test(self):
        pass

    def postposition(self):
        pass



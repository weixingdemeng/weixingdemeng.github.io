import logging
import time

class Log(object):
    def __init__(self, log_file_name):
        # 初始化创建日志收集器
        self.logger = logging.getLogger("测试用例日志{}".format(time.strftime("%Y%m%d")))
        self._connect(log_file_name)

    def set_level(self, level):
        # 设置收集器日志级别
        self.logger.setLevel(level)

    def _create_channel(self, filename=None):
        # 创建输出渠道
        file_handle = None
        if filename:
            file_handle = logging.FileHandler(filename=filename)
        control_handle = logging.StreamHandler()
        return file_handle, control_handle

    def _set_handle_level(self, control_level, file_level=None, filename=None):
        # 设置输出通道日志等级
        file_handle, control_handle = self._create_channel(filename=filename)
        if file_level:
            file_handle.setLevel(file_level)
        control_handle.setLevel(control_level)
        return file_handle, control_handle

    def _set_formatter(self, filename=None):
        # 设置日志输出格式
        file_handle, control_handle = self._set_handle_level(control_level=logging.INFO, file_level=logging.INFO, filename=filename)
        fmt = "%(asctime)s %(name)s %(levelname)s %(filename)s %(lineno)d:%(message)s"
        formatter = logging.Formatter(fmt=fmt)
        file_handle.setFormatter(formatter)
        control_handle.setFormatter(formatter)
        return file_handle, control_handle

    def _connect(self, filename=None):
        file_handle, control_handle = self._set_formatter(filename=filename)
        if file_handle:
            self.logger.addHandler(file_handle)
        self.logger.addHandler(control_handle)
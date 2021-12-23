import os
import configparser


class ReadConfig(object):
    def __init__(self):
        self.project_path = None
        self.config_path = None
        self.config = configparser.ConfigParser()

    def _set_project_path(self):
        # 获取项目地址
        try:
            self.project_path = os.path.split(os.path.abspath(__file__))[0]
        except Exception as e:
            raise(e)

    def _set_config_path(self):
        self._set_project_path()
        self.config_path = os.path.join(self.project_path, 'config.ini')

    def get_project_info(self, project_name, field_name):
        try:
            vaule = self.config.get(project_name, field_name)
        except Exception as e:
            raise(e)
        return vaule
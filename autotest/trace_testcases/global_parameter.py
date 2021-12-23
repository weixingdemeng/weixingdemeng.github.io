import os
from read_config import ReadConfig

PROTOCOL = ReadConfig().get_project_info('trace', 'protocol')
BASEURL = ReadConfig().get_project_info('trace', 'base_url')
PORT = ReadConfig().get_project_info('trace', 'port')
TIMEOUT = ReadConfig().get_project_info('trace', 'timeout')
BASE_URL = "{}://{}:{}".format(PROTOCOL, BASEURL, PORT)
PROJECT_PATH = os.path.split(os.path.abspath(__file__))[0]
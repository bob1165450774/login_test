import os

import yaml


class get_data1:
    def __init__(self):
        pass

    def get_data(self, filename):
        with open(os.path.abspath("C:\\Users\\bob1994\\Desktop\\aolai") + os.sep + "data" + os.sep + filename) as f:
            return yaml.safe_load(f)

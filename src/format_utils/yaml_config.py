# -*- coding:utf-8 -*-

import yaml

class YamlConfig(object):
    def __init__(self, ymlFilePath):
        with open(ymlFilePath, 'r', encoding='utf-8') as f:
            self.content = yaml.safe_load(f)

if __name__ == '__main__':
    pass
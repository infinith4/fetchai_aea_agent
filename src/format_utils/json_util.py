# -*- coding:utf-8 -*-

import json

class JsonUtil(object):
    def __init__(self, jsonFilePath):
        with open(jsonFilePath, 'r', encoding='utf-8') as f:
            self.content = json.load(f)

if __name__ == '__main__':
    pass
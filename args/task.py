# encoding: utf-8
import unittest
import os
import json
import yaml
from ate.exception import ParamsError


def load_yaml_file(testcase_path):
    with open(testcase_path, 'r+') as stream:
        print('yaml.load(stream) ----> %s\n' % yaml.load(stream))
        return yaml.load(stream)


def load_json_file(testcase_path):
    with open(testcase_path) as data_file:
        return json.load(data_file)


def load_testcases(testcase_path):
    file_suffix = os.path.splitext(testcase_path)[1]
    if file_suffix == '.json':
        return load_json_file(testcase_path)
    elif file_suffix in ['.yaml', '.yml']:
        return load_yaml_file(testcase_path)
    else:
        # '' or other suffix
        raise ParamsError("Bad testcase file name!")


def load_testcases_by_path(testset_path):
    if os.path.isfile(testset_path):
        testset = {
            "name": "",
            "config": {},
            "testcases": []
        }
        try:
            testcases_list = load_testcases(testset_path)
        except ParamsError:
            return []
        for item in testcases_list:
            for key in item:
                if key == "config":
                    testset["config"] = item["config"]
                    testset["name"] = item["config"].get("name", "")
                elif key == "test":
                    testset["testcases"].append(item["test"])
        return [testset]


def create_task(testset_path):
    """ create test task suite with specified testcase path.
        each task suite may include one or several test suite.
    """
    task_suite = unittest.TestSuite()  # 测试套件
    testsets = load_testcases_by_path(testset_path)

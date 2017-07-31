# encoding: utf-8

import argparse
import unittest
import os
import json
import yaml
from termcolor import colored

parser = argparse.ArgumentParser(
    description='Api Test Engine.')
parser.add_argument(
    '-V', '--version', dest='version', action='store_true',
    help="show version")
parser.add_argument(
    'testset_paths', nargs='*',
    help="testset file path")
parser.add_argument(
    '--log-level', default='INFO',
    help="Specify logging level, default is INFO.")
parser.add_argument(
    '--report-name',
    help="Specify report name, default is generated time.")

args = parser.parse_args()

if args.version:
    print(argparse.__version__)
    exit(0)


def load_yaml_file(testcase_path):
    with open(testcase_path, 'r+') as stream:
        return yaml.load(stream)


def load_json_file(testcase_path):
    with open(testcase_path) as data_file:
        return json.load(data_file)


class MyBaseError(BaseException):
    def __init__(self, msg):
        self.msg = msg
        self.color_msg = colored(msg, 'red', attrs=['bold'])

    def __repr__(self):
        return self.msg

    def __str__(self):
        return self.color_msg


class ParamsError(MyBaseError):
    pass


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
            print('testcases_list ----> %s\n' % testcases_list)
        except ParamsError:
            return []
        for item in testcases_list:
            print('item ----> %s\n' % item)
            for key in item:
                print('key ----> %s\n' % key)
                if key == "config":
                    testset["config"] = item["config"]
                    testset["name"] = item["config"].get("name", "")
                    print('config.name ----> %s\n' % testset['name'])
                elif key == "test":
                    testset["testcases"].append(item["test"])
                    print('testset["testcases"] ----> %s\n' % testset["testcases"])
        return [testset]

def create_suite(testset):
    suite = unittest.TestSuite()
    print('testset ----> %s\n' % type(testset))
    config_dict = testset.get("config", {})
    print('config_dict ----> %s\n' % config_dict)


def create_task(testset_path):
    """ create test task suite with specified testcase path.
        each task suite may include one or several test suite.
    """
    task_suite = unittest.TestSuite()  # 测试套件
    testsets = load_testcases_by_path(testset_path)
    print('testsets ----> %s\n' % testsets)
    for testset in testsets:
        print('testset ----> %s\n' % testset)
        suite = create_suite(testset)




for testset_path in args.testset_paths:
    testset_path = testset_path.strip('/')
    print("testset_path ----> %s" % testset_path)
    task_suite = create_task(testset_path)

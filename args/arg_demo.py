# encoding: utf-8

import argparse

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

for testset_path in args.testset_paths:
    testset_path = testset_path.strip('/')
    print('test_path : %s' % testset_path)

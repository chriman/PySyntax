# coding:utf-8

import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    '--verbosity',
    help='increase output verbosity')
args = parser.parse_args()

if args.verbosity:
    print('verbosity turned on')







'''
# 生成参数分析器
parser = argparse.ArgumentParser(description='Short sample app')

# 添加位置参数, add_argument(self, *args, **kwargs)
parser.add_argument('echo', help='echo the string you use here', type=int)
args = parser.parse_args()

print(args.echo**2)'''


# coding:utf-8

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('square',
                    type=int,
                    help='display a square of a given number')
parser.add_argument('-v', '--verbose',
                    action='store_true',
                    help='increase output verbosity')

args = parser.parse_args()
answer = args.square**2
if args.verbose:
    print('the square of {} equals {}'.format(args.square, answer))
else:
    print(answer)






'''
# 生成参数分析器
parser = argparse.ArgumentParser(description='Short sample app')

# 添加位置参数, add_argument(self, *args, **kwargs)
parser.add_argument('echo', help='echo the string you use here', type=int)
args = parser.parse_args()

print(args.echo**2)'''


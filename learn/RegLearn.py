#!/usr/bin/python
# -*- coding: UTF-8 -*-



import  re

pattern =re.compile(r'^cain\d{1,}',re.MULTILINE)

# 返回的是最长匹配的结果
# match= pattern.match("cain2233end2233errrrcain2233nend")
#
# if match:
#     # print match.string
#     print match.group()
#     # print pattern.flags
#     # print pattern.groups
# matchall = pattern.findall("cain2233end2233errrrcain2233end")
#
# if matchall:
#     print matchall

result = re.findall(r'^cain\d+end',"cain2233end2233errrrcain223333end",re.MULTILINE)
print result

search= pattern.search("cain2233end2233errrrcain2233nend")

if search:
    print search.groups()

global mony=''
def getData():
    'sdd'
    mony+='cain'
# m=re.match(r'^test(\w+\d{2}).(3*end)(4*)','testw23e3end4455')
# print m.string
# print m.group(1,2,3)






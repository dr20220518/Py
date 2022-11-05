#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import random

# 随机产生IP地址四个段落的数字
ip1 = random.randint(0,255)
ip2 = random.randint(0,255)
ip3 = random.randint(0,255)
ip4 = random.randint(0,255)

random_ip = str(ip1) + '.' + str(ip2) + '.' + str(ip3) + '.' + str(ip4)
# 要把数字转换成为字符串，并且拼接在一起！大家可以想象不转换的结果是什么？
print(random_ip)
# 打印结果
# 1427 - 소트인사이드

import sys

number = list(sys.stdin.readline())
number.sort(reverse=True)
print(''.join(number))
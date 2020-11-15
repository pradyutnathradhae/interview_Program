'https://www.hackerrank.com/challenges/most-commons/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen'

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = sorted(input().rstrip())
    cnt = Counter(s).most_common(3)
    
    for i,j in cnt:
        print('{} {}'.format(i,j))
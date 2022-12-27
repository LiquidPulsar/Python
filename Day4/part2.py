from pathlib import Path
import re
# from functools import partial
HOME = Path(__file__).parent

with open(HOME/"input.txt") as file:
    print(sum(b >= c and d >= a for a, b, c, d in map(lambda x: map(int, re.split('[-,]', x)), file)))
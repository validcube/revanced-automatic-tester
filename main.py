import sys

if sys.version_info[0] < 3:
    print("Please use Python 3 or above")
    exit()

try:
    import tabulate
    import alive_progress
except ImportError:
    print("Please install the dependencies using 'pip install -r requirements.txt'")
    exit()

import src.patch


try:
    import tabulate
    import alive_progress
except ImportError:
    print("Please install alive_progress using 'pip install alive-progress'")
    print("Please install tabulate using 'pip install tabulate'")
    exit()

import src.patch
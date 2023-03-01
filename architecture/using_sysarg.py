# it is possible to inject arguments at the point we first run our code

import sys

# when we invoke python it looks like this:
# python module_name.py
# we can also choose to add our own system arguemnt variables like this
# python module_name.py hello 32 True [] etc.

# sys.argv[0] is ALWAYS the path and name of the current module being run
print(sys.argv) # argv is a list of every argument passed in to this module

# cannot import directly---> use try/except condition
#print('Importing modules like helper.py and extras.py into Main.py')
try:
    import os
    #import helper
    import sys
    from helper import extract_upper, extract_lower
    import extras
except Exception as error:
    print("Module error, import failed {)".format(error))

#print(f"__name__ in Main.py: {__name__}")


print(f"The upper letters are: {extract_upper(extras.name)}")
print(f"The lower letters are: {extract_lower(extras.name)}")

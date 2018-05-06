#TempConvert.py

val = input("please type in tempeature with sign of temperatrue(e.g.:32C):")
if val[-1] in ['C','c']:
    f = 1.8 * float(val[0:-1]) +32
    print("temperature after converting is: %.2fF"%f)
elif val[-1] in ['F','f']:
    c = (float(val[0:-1]) - 32) / 1.8
    print("temperature after converting is: %.2fC"%c)
else:
    print("typo")

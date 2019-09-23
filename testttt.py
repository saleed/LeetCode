import sys

counter = 1
while True:
    line1= sys.stdin.readline()
    counter=1
    print("%s:%s" % (counter, line1))
    print(len(line1)
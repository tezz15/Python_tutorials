fhand = open("/home/tezz15/Desktop/python/mbox.txt")
count = 0
for line in fhand:
    if line.startswith('From:'):
        print(line)
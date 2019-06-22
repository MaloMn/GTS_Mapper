codes = ['c', '"', 'l', '}', 'v', ']]']

# Getting the data
with open('origin.txt', 'r') as f:
    content = f.read()

GTS = []

for i in range(0,len(codes), 2):
    a = content.find('"' + codes[i] + '"')
    content = content[a+5:]

    b = content.find(codes[i+1])
    GTS.append(content[:b])

    content = content[b:]

import re

# Collecting the labels
labels = []
reg = re.compile('"([^"]*)"')
st = GTS[1]
m = reg.match(st)

while m:
    labels.append(m.group()[1:-1])
    st=st[m.end()+1:]
    m = reg.match(st)

GTS[1] = labels

# Collecting the values
values = []
reg = re.compile('([0-9])\w+')
st = GTS[2]
m = reg.match(st)

while m:
    values.append(m.group())
    st=st[m.end():]
    m = reg.match(st)

GTS[2] = values

print(GTS)
import re

codes = ['c', '"', 'l', '}', 'v', ']]']
output = ''

# Getting the data
with open('origin.txt', 'r') as f:
    content = f.read()

b = 0
while content.find('"c"') >= 0:
    GTS = []
    
    for i in range(0, len(codes), 2):
        a = content.find('"' + codes[i] + '"')
        content = content[a+5:]
    
        b = content.find(codes[i+1])
        GTS.append(content[:b])
    
        content = content[b:]
    
    # Collecting the labels
    reg = re.compile('"([^"]*)"')
    st = GTS[1]
    m = reg.findall(st)
    
    
    GTS[1] = m
    
    # Collecting the values
    reg = re.compile(r'\d+')
    st = GTS[2]
    m = reg.findall(st)
    
    GTS[2] = m
    
    # WRITING THE DATA ============
    st_out = '[ NEWGTS '
    
    # Add the class
    st_out += '"' + GTS[0] + str(b) + '"'
    st_out += ' RENAME { '
    
    # Add the labels
    for word in GTS[1]:
        st_out += '"' + word + '"'
        st_out += ' '
    
    st_out += '} RELABEL '
    
    # Add the values
    for i in range(0, len(GTS[2]), 2):
        st_out += GTS[2][i] + ' NaN NaN NaN ' + GTS[2][i+1] + ' ADDVALUE '
    
    output += st_out
    
    b += 1
    
output += ']'


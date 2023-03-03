# take user input 
n = int(input())
sizes = input().split()
m = int(input())
requests = input().split()

# convert size to num (1000XS = 1, S = 1001, M = 1002, L = 1003, 1000XL = 2003)
def size_to_num(size):
    numX = 0
    for i in range(len(size)):
        if size[i] == "X": # count number of X in front 
            numX += 1
        else:
            break
            
    if size[i:] == "M":
        num = 1002
    if size[i:] == "S": 
        num = 1001 - numX
    elif size[i:] == "L":
        num = 1003 + numX
    
    return num

sizes_num = [size_to_num(size) for size in sizes]
requests_num = [size_to_num(size) for size in requests]

# sort desc order
sizes_num.sort(reverse=True)
requests_num.sort(reverse=True)


fulfill = True
for r in requests_num:
    match = [s for s in sizes_num if s >= r]
    if not match: # check if match is empty
        fulfill = False
        break
    else:
        sizes_num.remove(max(match)) # remove the largest match possible (matched)
        
if fulfill:     
    print('Yes')
else:
    print('No') 

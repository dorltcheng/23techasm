# take user input 
n = int(input())
records = []
for i in range(n):
    userIn = input()
    records.append(userIn)

allValid = True
errorCodes = []

for r in records:
    rList = r.split()
#     print(rList)
    if rList[1] == 'false':
        allValid = False
        errorCodes.append(rList[2:])

if allValid and not errorCodes: # if allValid = True and empty errorCodes
    print('Yes')
else:
    errorCodes = [' '.join(error) for error in errorCodes]
    print('No')
    print(' '.join(errorCodes))



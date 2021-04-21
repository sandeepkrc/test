
lis=['a','a','f','g','h','f','g','a','c','c','u','j']
from collections import Counter
result=Counter(lis)
print(result)
var='a'
c=0
for i in lis:
        if i==var:
                c+=1
print(c)

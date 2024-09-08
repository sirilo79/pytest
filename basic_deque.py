from collections import deque

deq1 = deque()

for i in range(2):
    deq1.append(i)
    print("deq1 :", deq1)

for i in range(3,6):
    deq1.appendleft(i)
    print("deq1 :", deq1) 

deq1.pop()
print("deq1 :", deq1)
deq1.popleft()
print("deq1 :", deq1)
print("======================================================")

deq2  = deque(maxlen=100)

for i in range(10):
    deq2.append(i)    
    print("deq2 :", deq2)
    
print("output : ", deq2[3],deq2[2],deq2[1])
print("length : ", len(deq2))

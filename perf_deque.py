from collections import deque
import time

deq1  = deque(maxlen=1000)  ## size : 100

start_time = time.time()
for i in range(50000):
    deq1.append(i)    
#    print(deq1)
end_time = time.time()
print(f"{end_time - start_time:.5f} sec")
  

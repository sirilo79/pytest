from collections import deque
import time

deq1  = deque(maxlen=100000000)  ## 1억건

start_time = time.time()
for i in range(15):
    deq1.append(i)    
    print(deq1)
end_time = time.time()
print(f"{end_time - start_time:.5f} sec")
    



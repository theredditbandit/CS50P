# found a new sorting technique
import random
import time
isunsorted = True
iterations = 0
a = input("Enter the elements: ")
start = time.time()
a = list(a.split(" " ))
slist = a.copy()
# slist.sort()
while isunsorted:
    if all(a[i]<=a[i+1] for i in range(len(a)-1)):
        print(f"The sorted list is {a}")
        print(f"The list was sorted in {iterations} iterations and took {time.time()-start:.5f}s to complete " )
        isunsorted = False
    else:
        random.shuffle(a)
        iterations +=1





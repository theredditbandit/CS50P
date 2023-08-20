import time

a = input("Enter the elements: ")
start = time.time()
a = list(a.split(" " ))
slist = a.copy()
slist.sort()
if a == slist:
    print(f"The list took {time.time()-start:.5f}s to check if sorted using the sort() function " )
# if all(a[i]<=a[i+1] for i in range(len(a)-1)):
#     print(f"The list took {time.time()-start:.5f}s to check if sorted using the more \"pythonic\" way " )
def sumsubarray(arr,l):
    res=0
    for i in range(0,l):
        res+=(arr[i]*(i+1)*(l-i))
    return res

arr=list(map(int,input().split(',')))
l=len(arr)
print("Sum of all Subarrays is:{}".format(sumsubarray(arr,l)))

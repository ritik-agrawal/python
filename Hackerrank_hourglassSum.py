def hourglassSum(arr):
    all_sum=[]
    temp_sum=0
    temp_solution=[]
    solution=[]
    for r in range(0,4):
        for c in range(0,4):
            temp_solution=patternhourglass(c,r,arr)
            temp_sum=get_hourglassSum(temp_solution)
            all_sum.append(temp_sum)
    return max(all_sum) 

def patternhourglass(c,r,arr):
    ignore=[(r+1,c),(r+1,c+2)]
    res=[]
    for i in range(0,3):
        p_r=r+i
        temp=[]
        for j in range(0,3):
            p_c=c+j
            if (p_r,p_c) in ignore:
                temp.append(0)
            else:
                temp.append(arr[p_r][p_c])
        res.append(temp)
    return res

def get_hourglassSum(arr):
    res=0
    for it in arr:
        res+=sum(it)
    return res

arr = []
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))
result = hourglassSum(arr)
print(result)

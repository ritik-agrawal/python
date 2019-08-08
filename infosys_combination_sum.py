from itertools import combinations as comb
inarr=list(map(int,input().split(',')))
given_sum=int(input())
inarr_com=comb(inarr,4)
info_list=[]
solu_list=[]
for it in inarr_com:
    info_list.append((sum(it),it))
for it in info_list:
    if it[0]==given_sum:
        solu_list.append(it[1])
print(len(solu_list))

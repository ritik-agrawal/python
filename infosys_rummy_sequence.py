def get_numb(st):
    numb=0
    for it in st:
        if it.isnumeric():
            temp=int(it)
            numb=(numb*10)+temp
        else:
            return numb

def lcs(st):
    ans=[]
    lim=len(st)
    for it in st:
        temp=[]
        j=it
        x=j-1
        if x not in st:
            while j in st:
                temp.append(j)
                j+=1
            if len(temp)>len(ans):
                ans=temp
    return ans

def get_longest_len(out_seq):
    max_len=0
    for it in out_seq:
        comp=len(it[1])
        if comp>max_len:
            max_len=comp
    return max_len

def seq_max_len(out_seq,max_len):
    seq=[]
    for it in out_seq:
        comp=len(it[1])
        if comp==max_len:
            seq.append(it)
    return seq

def output_string(st):
    o_s=st[0]
    res=""
    o_seq=st[1]
    o_lim=len(o_seq)-1
    for it in range(0,o_lim):
        res+=str(o_seq[it])+o_s+","
    res+=str(o_seq[o_lim])+o_s
    return res

c=[]
d=[]
h=[]
s=[]
suits=[c,d,h,s]
suit_dic={0:"C",
          1:"D",
          2:"H",
          3:"S"}
solu_dic={}
out_seq=[]
rummy_seq=input().split(',')
for it in rummy_seq:
    num=get_numb(it)
    if "C" in it:
        c.append(num)
    if "D" in it:
        d.append(num)
    if "H" in it:
        h.append(num)
    if "S" in it:
        s.append(num)
for it in range(0,4):
    len_it=len(suits[it])
    if len_it>=3:
        solu_dic[suit_dic[it]]=suits[it]
for it in solu_dic:
    out_seq.append([it,lcs(solu_dic[it])])
max_len=get_longest_len(out_seq)
out_seq=seq_max_len(out_seq,max_len)
for it in out_seq:
    print(output_string(it))


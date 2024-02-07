from beautifultable import BeautifulTable
d={}
f=open("grammar.txt", "r")
f1=f.readlines()
print ("\n")
print  ("*"*28,"SHIFT REDUCE PARSER","*"*28)
print ("\nThe productions of the grammer are,\n")
for i in f1:
    print (i)
    i=i.split("->")
    i[1]=i[1].rstrip()
    d[i[0]]=i[1]

print ("\n")
b=input("Enter Test Input String: ")
a=b[:-1]
a+=" ?"
if " " in a:
    a=a.split()
else:
    a=[a]
start=[]
icount=1
def chkinput(a, d):
    global start
    global table
    global icount
    table=BeautifulTable()
    l=[]
    stack=""
    inp=""
    end="--"
    table.column_headers=["Stack","Input","Action"]
    for q in start:
        stack=stack+q
    for w in a:
        inp=inp+w
    stack="$"
    inp=inp+'$'
    table.append_row([stack,inp,end])
    for p in d:
        if "|" in d[p]:
            d[p]=d[p].split("|")
            for q in range (len (d[p])):
                if " " in d[p][q]:
                    d[p][q]=d[p][q].split(" ")
                else:
                    continue
            l.append([p,d[p]])
        else:
            l.append([p,[d[p]]])          
    for i in range(len(a)+1):
        if i==4:
            icount=1
        else:
            start.append(a[i])
            end="Shift"
            stack="$"
            inp=""
            for q in start:
                stack=stack+q
            for w in a[i+1:]:
                inp=inp+w
            inp=inp+'$'
            table.append_row([stack,inp,end])
        def fun():
            global start
            global icount
            x=start.pop()
            for k in l:
                for g in k[1]:
                    if x==g:
                        start.append(k[0])
                        end="Reduce"
                        stack="$"
                        inp=""
                        for q in start:
                            stack=stack+q
                        for w in a[i+1:]:
                            inp=inp+w
                        inp=inp+'$'
                        table.append_row([stack,inp,end])
                        return True
            if icount==1:
                start.append(x)
                icount=0
            else:
                start[0]+=x
            return False

        while fun():
            None
    print(table)
    found=False   
    for i in d.keys():
        if len(start)==1:
            if start[0]==i:
                found=True
                break
        else:
            continue
    if found==True:
       print ("Success!") 
    else:
        print ("Not Successful!")        
chkinput(a,d)

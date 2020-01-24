maxes=[{8:-1,9:-1,10:-1,11:-1},{8:[],9:[],10:[],11:[]}]
abs_maxes=[[-1,-1],[[],[]]]
for i in open("mat_dv.txt").read().split('\n'):
    strin=i.split(" ")
    if int(strin[3])+int(strin[4])>maxes[0][int(strin[2])]:
        maxes[0][int(strin[2])]=int(strin[3])+int(strin[4])
        maxes[1][int(strin[2])]=[]
        maxes[1][int(strin[2])].append(strin[0]+' '+str(int(strin[3])+int(strin[4])))
    elif int(strin[3])+int(strin[4])==maxes[0][int(strin[2])]:
        maxes[1][int(strin[2])].append(strin[0]+' '+str(int(strin[3])+int(strin[4])))

    if int(strin[3])>abs_maxes[0][0]:
        abs_maxes[0][0]=int(strin[3])
        abs_maxes[1][0]=[]
        abs_maxes[1][0].append(strin[0]+' '+ strin[3])
    elif int(strin[4])==abs_maxes[0][0]:
        abs_maxes[1][0].append(strin[0]+' '+ strin[3])

    if int(strin[4])>abs_maxes[0][1]:
        abs_maxes[0][1]=int(strin[4])
        abs_maxes[1][1]=[]
        abs_maxes[1][1].append(strin[0]+' '+ strin[4])
    elif int(strin[4])==abs_maxes[0][1]:
        abs_maxes[1][1].append(strin[0]+' '+ strin[4])


print(maxes[1])
print(abs_maxes[1])

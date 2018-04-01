







'''

for row in range(1, 10):
    str1=""
    space=" "
    for col in range(1,row+1):
       if(row==3 and col==2) or (row==4 and col==2):
           space="  "
       else:
           space=" "

       str1+=(str(row)+"*"+str(col)+"="+str(row*col)+space)


    print(str1)
    '''
hang=0
while hang<=8:
    hang +=1;
    lie =1;
    while lie<=hang:
        print(str(lie)+"*"+str(hang)+"="+str(hang*lie),end="\t")
        lie+=1;
    print()
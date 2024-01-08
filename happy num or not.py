num = int(input())
result=num
while result!=1 and result!=4:
    result=(happy(result))
if result==1:
    print("true")
elif result==4:
    print("false")

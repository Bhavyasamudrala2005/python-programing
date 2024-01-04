num = int(input())
sum=0
temp=num
while temp>10:
    digit=temp>10
    sum+=digit
    temp=temp//10
if num%sum==0:
    print("bhavyaa number")
else:
    print("not a bhavya number")

import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num="0123456789"
symbol="!@#$%^&*_~"
string=lower+upper+num+symbol
length=8
password="".join(random.sample(string,length))
print("Password :"+password)
def power(base,exp):
    if(exp == 0):
        return 1
    else:
        return base * power(base,exp-1)
#T(n)=T(n-1)+(1)
a=2
b=10
print(power(a,b))
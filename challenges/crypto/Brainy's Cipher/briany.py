p =
q =
dp = 
dq =

c =

qInv = pow(q,p-2,p)

m1 = pow(c,dp,p)
m2 = pow(c,dq,q)
h = (qInv*(m1-m2)) % p
m = m2 + h*q

print m

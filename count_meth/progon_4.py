import numpy as np

Eq=np.zeros((4,4))
Eq[0][1]=2
Eq[0][2]=-4
Eq[0][3]=6
Eq[1][0]=3
Eq[2][0]=3
Eq[1][1]=1
Eq[2][1]=1
Eq[1][2]=-14
Eq[1][3]=16
Eq[2][2]=-21
Eq[2][3]=10
Eq[3][1]=2
Eq[3][0]=2
Eq[3][3]=26
print(Eq)
def Ai(A_i_pred,i):
    a=-Eq[i][2]/(Eq[i][1]+Eq[i][0]*A_i_pred)
    return a

def Bi(B_i_pred,A_i_pred,i):
    b=(Eq[i][3]-Eq[i][0]*B_i_pred)/(Eq[i][1]+Eq[i][0]*A_i_pred)
    return b
def Xi(A_i,B_i,x_i1):
    x=A_i*x_i1+B_i
    return x

A=np.zeros((4))
B=np.zeros((4))
X=np.zeros((4))

A[0]=-Eq[0][2]/Eq[0][1]
B[0]=Eq[0][3]/Eq[0][1]

for i in range(1,3):
    A[i]=Ai(A[i-1],i)
    B[i]=Bi(B[i-1],A[i-1],i)

X[-1]=B[-1]

for i in range(2,0,-1):
    X[i]=Xi(A[i],B[i],X[i+1])

def st1(bi,ai,ci):

    if abs(bi)>=(abs(ai)+abs(ci)):
        res=10
    else:
        res=-10
    return res

check=np.zeros((4))

for i in range(0,3):
    check[i]=st1(Eq[i][1],Eq[i][0],Eq[i][2])

for i in range(1,3):
    if Eq[i][0]==0:
        check[i]=-10

for i in range(0,2):
    if Eq[i][2]==0:
        check[i]=-10

print(check)

print(X)
#B(21.2,7,2)

#function definition
def minkowski(p,q,x):
    euc_dist=0
    for i in range(len(p)):
        euc_dist=euc_dist+pow(abs(p[i]-q[i]),x)

    euc_dist=pow(euc_dist,1/x)
    return euc_dist

#data initiation
a=[1,2,3,4,5]
b=[10,20,30,40,50]


#function call
print('manhattan dist',minkowski(a,b,1))
print('Euclidean dist',minkowski(a,b,2))
print('minkowski dist',minkowski(a,b,3))


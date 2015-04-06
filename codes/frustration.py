def calcF(theta,A):
  import math
  Fij={}
  for i in theta.keys():
    f={}
    for j in A[i]:
      f[j]=1.0+math.cos(theta[j]-theta[i])
    Fij[i]=f

  L=0.0
  F=0.0

  for i in Fij.keys():
    for j in Fij[i].keys():
      F+=Fij[i][j]
      L+=1.0

  F=F/(2.0*L)

  return [F,Fij]

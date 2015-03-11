def cpdict(A):
  from copy import deepcopy

  B={}
  for n in A.keys():
    u=[]
    u=deepcopy(A[n])
    B[n]=deepcopy(u)
  return B

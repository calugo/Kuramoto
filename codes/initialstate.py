def initialstate(N,rk,pi):
  phio={}
  for i in range(N):
    phio[i]=2.0*pi*rk.uniform_pos()
  return phio

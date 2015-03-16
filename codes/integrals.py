def rk4(Pold,A,h):
  from math import sin as Sin

  Pnew={}
  Ki={}
  ####################################
  fi1={}
  for i in Pold.keys():
    ki=len(A[i])
    sfi=0.0
    for j in A[i]:
      sfi+=Sin( 1.0*( Pold[j]-Pold[i]))
    fi1[i]=(-1.0/ki)*(sfi)
    Ki[i]=ki
  ####################################
  fi2={}
  for i in Pold.keys():
    sfi=0.0
    for j in  A[i]:
      sfi+=Sin(  1.0*( (Pold[j]+(0.5*h*fi1[j])) - (Pold[i]+(0.5*h*fi1[i])) )    )
    fi2[i]=((-1.0/Ki[i])*sfi)
  #####################################
  fi3={}
  for i in Pold.keys():
    sfi=0.0
    for j in  A[i]:
      sfi+=Sin(  1.0* ((Pold[j]+(0.5*h*fi2[j])) - (Pold[i]+(0.5*h*fi2[i])) )    )
    fi3[i]=((-1.0/Ki[i])*sfi)
  #########################################
  fi4={}
  for i in Pold.keys():
    sfi=0.0
    for j in  A[i]:
      sfi+=Sin( 1.0*((Pold[j]+(h*fi3[j])) - (Pold[i]+(h*fi3[i])) )   )
    fi4[i]=((-1.0/Ki[i])*sfi)

  for i in Pold.keys():
    phinew=Pold[i]+(h/6.0)*(fi1[i]+fi2[i]+fi3[i]+fi4[i])
    Pnew[i]=phinew

  return Pnew

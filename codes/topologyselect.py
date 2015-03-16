def graph(N,gtype):
  A={}

###########################
  if gtype[0]=='grid':
    k=0
    for j in range(N):
      for i in range(N):
        nnh=[]

        if i<(N-1):
            nnh.append(k+1)
        if i>0:
            nnh.append(k-1)
        if j>0:
            nnh.append(k-N)
        if j<(N-1):
            nnh.append(k+N)
        A[k]=nnh
        k+=1
        #print A
##########################
  if gtype[0]=='torus':
    k=0
    for j in range(N):
      for i in range(N):
        nnh=[]
        ##########################
        if i<(N-1):
            nnh.append(k+1)

        if i==(N-1):
            nnh.append(k-(N-1))

        if i>0:
            nnh.append(k-1)

        if i==0:
            nnh.append(k+(N-1))
        ###########################
        if j>0:
            nnh.append(k-N)

        if j==0:
            nnh.append(k+(N-1)*N)

        if j<(N-1):
            nnh.append(k+N)

        if j==(N-1):
            nnh.append(k-(N-1)*N)
        ###########################
        A[k]=nnh
        k+=1
##########################
  if gtype[0]=='ring':
    k=0
    for i in range(N):
      nnh=[]
      if i==0:
        nnh.append(i+1)
        nnh.append(N-1)

      if (i>0) and (i<N-1):
        nnh.append(i-1)
        nnh.append(i+1)

      if i==(N-1):
        nnh.append(0)
        nnh.append(i-1)

      A[k]=nnh
      k+=1
#############################
  if gtype[0]=='line':
    k=0
    for i in range(N):
      nnh=[]
      if i==0:
        nnh.append(i+1)
        #nnh.append(N-1)

      if (i>0) and (i<N-1):
        nnh.append(i-1)
        nnh.append(i+1)

      if i==(N-1):
        #nnh.append(0)
        nnh.append(i-1)

      A[k]=nnh
      k+=1

############################
  if gtype[0]=='BarAlb':
    import math
    from pygsl import rng as rn
    print("BaALB!")
    print gtype
    print N
    No=int(math.floor(N/10)) #N>10!
    Nr=No
    SEED=gtype[1]#123456789
    rk=rn.rng()
    rk.set(SEED)
    adjx={}
    for i in range(No):
      nnh=[]
      qs=0
      while qs==0:
        pr=rk.uniform_int(No)
        if pr!=i:
            nnh.append(int(pr))
            qs=1
      adjx[i]=nnh

    for i in adjx.keys():
      nnh=[]
      nnh.append(adjx[i][0])
      for j in adjx.keys():
        if i!=j:
          if adjx[j][0]==i:
            nnh.append(j)
      A[i]=nnh

    m=int(math.floor(No/2)) #N>10!
    Nr=len(A.keys())
    #print Nr, m
    while Nr<=N:
      cnt=0
      zn=0.0
      for i in A.keys():
        zn+=len(A[i])
      nnh=[]
      while cnt<=m:
        qi=zn*rk.uniform_pos()
        sx=0.0
        for ik in A.keys():
          sx+=len(A[ik])
          if (sx>=qi) and ik not in nnh:
            nnh.append(ik)
            cnt+=1
            break
      A[Nr]=nnh
      for i in nnh:
        A[i].append(Nr)
      Nr+=1
    #print Nr, N
############################
  if gtype[0]=='hubs':
    M=gtype[1]
    Adj={}
    k=0

    for i in range(N):
      nnh=[]
      if i==0:
        for j in range(1,N):
            nnh.append(j)
      if i>0:
        nnh.append(0)
      Adj[k]=nnh
      k+=1

    Bj={}
    kx=0
    for j in range(M):
      if j==0:
        for n in range(N):
            Bj[kx]=Adj[n]
            kx+=1
      if j>0:
        for n in range(N):
            kz=kx-(j*(len(Adj.keys())))
            #print kx,kz,j*N
            nnh=[]
            if kz==0:
                for jx in range(1,N):
                    nnh.append(jx+j*(N))
            if kz>0:
                nnh.append(j*N)
            Bj[kx]=nnh
            kx+=1

    z=[]
    for j in range(M):
      z.append(j*N)
      #print z

    for rj in z:
      for rk in z:
        if (rk not in Bj[rj]) and rk!=rj:
            Bj[rj].append(rk)
    ##print Bj
    for nk in Bj.keys():
      A[nk]=Bj[nk]

############################
  if gtype[0]=="fully":
    for i in range(N):
      nnh=[]
      for j in range(N):
        if j != i:
          nnh.append(j)
      A[i]=nnh
############################
  return A

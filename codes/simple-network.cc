#include <iostream> 
#include <fstream>     
#include <cstdlib>  
#include <cmath> 
#include <iomanip>  
#include <complex>
#include <time.h> 
#include "rndgen.hh"
using namespace std; 

double rand_do1() {return static_cast<double>(rand())/RAND_MAX;}

void kuramoto_network_system(double *pp,int **matrix,int *conn,
                                 double *omega,double mu,int size) {
  double pi=3.1415926535897932;
  double net=0.0,*ptemp;
  ptemp=new double[size];
  for(int i=0;i<size;i++) { 
    net=0.0;
    for(int j=0;j<size;j++) 
      net = net + matrix[j][i]*sin(2.0*pi*(pp[j] - pp[i]));
    ptemp[i] = omega[i] + (mu/static_cast<double>(conn[i]))*net; 
  }
  for(int i=0;i<size;i++)
    pp[i]=ptemp[i];
  delete [] ptemp;  }

void trj_kuramoto_network_rk4(double **phi,int **matrix,int *conn,
               double *omega,double mu,int size,int Astart,int A,double h) {
  double *pp,*p1,*p2,*p3,*p4;
  pp=new double[size];p1=new double[size];p2=new double[size]; 
  p3=new double[size];p4=new double[size];
  for(int t=Astart;t<A-1;t++) {
    for(int i=0;i<size;i++)  
      pp[i]=phi[i][t];
   kuramoto_network_system(pp,matrix,conn,omega,mu,size);
   for(int i=0;i<size;i++)
     { p1[i]=pp[i]; pp[i]=phi[i][t]+(h/2.0)*p1[i]; }
   kuramoto_network_system(pp,matrix,conn,omega,mu,size);
   for(int i=0;i<size;i++)
     { p2[i]=pp[i]; pp[i]=phi[i][t]+(h/2.0)*p2[i]; }
   kuramoto_network_system(pp,matrix,conn,omega,mu,size);
   for(int i=0;i<size;i++)
     { p3[i]=pp[i]; pp[i]=phi[i][t]+h*p3[i]; }
   kuramoto_network_system(pp,matrix,conn,omega,mu,size);
   for(int i=0;i<size;i++)
     p4[i]=pp[i];  
   for(int i=0;i<size;i++) 
     phi[i][t+1]=phi[i][t]+(h/6.0)*(p1[i]+2.0*p2[i]+2.0*p3[i]+p4[i]);
  }
  delete[]pp; delete[]p1; delete[]p2; delete[]p3; delete[]p4;   } 


int main() {
  srand( (unsigned)time(NULL) ); 
  Rnd3 initial(263759);
  int size=4,A=100000; 
  double h=0.01;
  double mu=-0.1;
  double pi=3.1415926535897932;
  complex<double>imagunit(0.0,1.0);  
  double **phi,*omega,**DD;
  phi=new double*[size]; omega=new double[size]; DD=new double*[size]; 
  for(int i=0;i<size;i++) {phi[i]=new double[A];DD[i]=new double[size];}
  int **matrix,*conn;  
  matrix=new int*[size]; conn=new int[size];
  for(int i=0;i<size;i++) matrix[i]=new int[size];
  for(int i=0;i<size;i++)
    for(int j=0;j<size;j++) 
      { matrix[i][j]=0; DD[i][j]=0.0; }
  for(int i=0;i<size;i++) omega[i]=0.1;  

//  for(int i=1;i<size;i++)
//    { matrix[i][0]=1; matrix[0][i]=1;}

//  for(int i=0;i<size-1;i++)
//    { matrix[i][i+1]=1; matrix[i+1][i]=1;}
//  matrix[size-1][0]=1; matrix[0][size-1]=1;
//  matrix[2][0]=1; matrix[0][2]=1;

  matrix[0][1]=1; matrix[1][0]=1;
  matrix[2][3]=1; matrix[3][2]=1;

  for(int i=0;i<size;i++)      {
    conn[i] = 0;
    for(int j=0;j<size;j++)
      conn[i] = conn[i] + matrix[j][i];}


  int nopoints=1; 
  int Astop=10000;
  for(int nn=0;nn<nopoints;nn++) {

//for(int i=0;i<size;i++) phi[i][0]=rand_do1();

    phi[0][0]=0.1;phi[1][0]=0.2;phi[2][0]=0.2;phi[3][0]=0.1;

    trj_kuramoto_network_rk4(phi,matrix,conn,omega,mu,size,0,Astop,h);

    for(int i=0;i<size;i++) for(int j=0;j<size;j++) {
     DD[i][j]=abs(arg(exp(imagunit*2.0*pi*abs(phi[i][Astop-1]-phi[j][Astop-1])))/pi);
     if (DD[i][j]<1e-6) DD[i][j]=0.0;  } 

    for(int i=0;i<size;i++)  {
     for(int j=0;j<size;j++) 
      cout<<setprecision(4)<< DD[i][j] << "  " ;
     cout << endl;        }    
     cout << endl;
  }



  for(int i=0;i<size-1;i++)
    { matrix[i][i+1]=1; matrix[i+1][i]=1;}
  matrix[size-1][0]=1; matrix[0][size-1]=1;

  for(int i=0;i<size;i++)      {
    conn[i] = 0;
    for(int j=0;j<size;j++)
      conn[i] = conn[i] + matrix[j][i];}

  for(int nn=0;nn<nopoints;nn++) {

    trj_kuramoto_network_rk4(phi,matrix,conn,omega,mu,size,Astop-1,A,h);

    for(int i=0;i<size;i++) for(int j=0;j<size;j++) {
     DD[i][j]=abs(arg(exp(imagunit*2.0*pi*abs(phi[i][A-1]-phi[j][A-1])))/pi);
     if (DD[i][j]<1e-6) DD[i][j]=0.0;  } 

    for(int i=0;i<size;i++)  {
     for(int j=0;j<size;j++) 
      cout<<setprecision(4)<< DD[i][j] << "  " ;
     cout << endl;        }   
   
  }



  for(int i=0;i<size;i++) 
    delete [] phi[i];
  for(int i=0;i<size;i++)
    delete [] matrix[i];
  for(int i=0;i<size;i++)
    delete [] DD[i];
  delete [] DD;
  delete [] matrix;
  delete [] conn;
  delete [] phi;
  delete [] omega;
  return 0;
}

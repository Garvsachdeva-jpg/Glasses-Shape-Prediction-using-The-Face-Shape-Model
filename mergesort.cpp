#include<iostream>
#include<ctime>
using namespace std;
class merge
{
public:
void combine(int Arr[50], int p, int q, int r);
void mergesort(int Arr[50],int p,int r);
};


void merge::combine(int Arr[50],int p,int q,int r){    
int n1=q-p+1;
int n2=r-q;
int L[n1],R[n2];
for(int i=0;i<n1;i++){
   L[i]=Arr[p+i]; 
}
for (int j=0; j<n2; j++)
{
   R[j]=Arr[q+1+j];
}
int i=0,j=0,k=p;
while(i<n1&&j<n2){
    if(L[i]<=R[j]){
Arr[k]=L[i];
i++;
    }
else{
    Arr[k]=R[j];
    j++;
}k++;
}
while(i<n1)
{
    Arr[k]=L[i];
    i++;
    k++;
}
while(j<n2){
    Arr[k]=R[j];
    j++;
    k++;
}
}

void merge:: mergesort(int Arr[50], int p, int r){
    
    if(p<r){
int q=((p+r)/2);
cout<<"Before first call    ";
cout<<"p="<<p<<" q="<<q<<" r="<<r<<endl;

mergesort(Arr,p,q);
cout<<"After first call   ";
cout<<"p="<<p<<" q="<<q<<" r="<<r<<endl;
mergesort(Arr,q+1,r);
cout<<"after second call   ";
cout<<"p="<<p<<" q="<<q<<" r="<<r<<endl;
combine(Arr,p,q,r);
cout<<"after combining  ";
cout<<"p="<<p<<" q="<<q<<" r="<<r<<endl;
}}


int main(){
    clock_t start =clock();
    srand(time(0));
merge M;
int n;
cout<<"Enter the number of elements:";
cin>>n;
int A[50];
for(int i=0;i<n;i++){
    
    //cin>>A[i];
    A[i]=rand()%100;
    cout<<"Enter element "<<i+1<<":"<<A[i]<<endl;
}

M.mergesort(A,0,n-1);
for (int j = 0; j < n; j++)
{
    cout<<A[j];
    cout<<" ";
}
clock_t end =clock();
float time_used =float(end-start) /CLOCKS_PER_SEC;
cout<<time_used;
return 0;
}

    



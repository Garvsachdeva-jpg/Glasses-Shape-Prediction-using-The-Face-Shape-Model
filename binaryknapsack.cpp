#include<iostream>
#include<ctime>
using namespace std;
struct Item{
int profit;
int weight;
};
int knapsack(int n,int W,Item arr[]){
int B[n+1][W+1];
for(int w=0;w<=W;w++){

B[0][w]=0;
}
for (int i = 1;i<=n; i++)
{
B[i][0]=0;
}


for(int i=1;i<=n;i++){
for(int w=0;w<=W;w++){

if(arr[i-1].weight<=w){
if(arr[i-1].profit+B[i-1][w-arr[i-1].weight]>B[i-1][w]){
B[i][w]=arr[i-1].profit+B[i-1][w-arr[i-1].weight];
}
else B[i][w]=B[i-1][w];
}
else 
B[i][w]=B[i-1][w];//if arr[i].weight>w

}

}

for (int i = 0; i <=n; i++){
for( int w = 0; w <=W; w++)
{
    cout<<B[i][w]<<" ";
}
cout<<endl;
}

return B[n][W];
}
int main(){
clock_t start=clock();
int n,W;
cout<<"Enter the no of items:";
cin>>n;
cout<<"Enter the capacity of the sack:";
cin>>W;

struct Item I1[n];

for (int i = 0; i <n; i++)
{
cout<<"Enter the weight and value of an item "<<i+1<<":";
cin>>I1[i].weight>>I1[i].profit;
}
int profit=knapsack(n,W,I1);

cout<<"The profit is:"<<profit;
clock_t end=clock();
float t=(end-start)/CLOCKS_PER_SEC;
cout<<endl<<t;
return 0;

}
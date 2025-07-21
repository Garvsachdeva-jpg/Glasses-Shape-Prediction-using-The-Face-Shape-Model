#include<iostream>
#include<cstdlib>
#include <bits/stdc++.h>
#include<ctime>
using namespace std;
struct Item{
float weight;
float ratio;
float profit;

};
void swap(Item &a, Item &b) { 
    Item temp = a; 
    a = b; 
    b = temp; 
}

void bubbleSort(Item arr[], int n) {
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-i-1; j++) {
            if (arr[j].ratio < arr[j+1].ratio) {
                swap(arr[j], arr[j+1]);
            }
        }
    }


    for (int i = 0; i <n; i++)
    {
        cout<<arr[i].ratio<<endl;
        /*cout<<arr[i].weight<<endl;
        cout<<arr[i].profit<<endl;*/
    }
    
}




float knapsack(Item I[],float capacity,int n){

double totalwt=0,totalprofit=0;

for (int i = 0; i <n; i++)
{if(capacity>=I[i].weight){

capacity-=I[i].weight;
totalprofit+=I[i].profit;
}
else 
{
totalprofit+=(capacity/I[i].weight)*I[i].profit;
break;
}
}
return totalprofit;
}

int main(){
clock_t start=clock();

    int n;
    cout<<"Enter the number of items:";
    cin>>n;
int W;
    cout<<"Enter the capacity of the sack:";
    cin>>W;
    Item I[n];
for (int i = 0; i <n; i++)
{cout<<"Enter the weight and profits of item "<<i+1<<": ";
    cin>>I[i].weight>>I[i].profit;
}
    for(int i=0;i<n;i++){

        I[i].ratio=I[i].profit/I[i].weight;
        cout<<I[i].ratio<<endl;   
    }

bubbleSort(I,n);
float totalprofit=knapsack(I,W,n);
cout << "Total profit is: " << totalprofit << endl;
clock_t end=clock();

float timeused=(end-start)/CLOCKS_PER_SEC;
cout<<timeused<<endl;
return 0;


}




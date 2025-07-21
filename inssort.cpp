#include<iostream>
#include<cstdlib>
#include<ctime>
using namespace std;
class sort{
    public:
int array[50];
int n;
    void get_data(int );
    void insertionsort();
void display();
};
void sort::get_data(int size){
   n=size;
for(int i=0;i<n;i++){
   // cout<<"enter element "<<i+1<<":";
    //cin>>array[i];
    array[i]=rand() % 10 +1;
    cout<<array[i]<<"\n";

}
//cout<<sizeof(array)/sizeof(array[0]);
}
void sort::insertionsort(){

    int key,i;
for(int j=1;j<n;j++){
    key=array[j];
    i=j-1;
    while(i>=0 &&array[i]>key)
    {array[i+1]=array[i];
    i=i-1;}
array[i+1]=key;
}

}
void sort::display() {
    cout << "Sorted array: ";
    for (int i = 0; i < n; i++) {
        cout << array[i] << " ";
    }
   // cout <<"/n";
}


int main(){
    clock_t start =clock();
    srand(time(0));
    sort i1;
    int size;
    cout << "Enter the number of elements: ";
    cin >> size;
    i1.get_data(size);

    i1.insertionsort();
    i1.display();
    clock_t end =clock();
    float time_used =float(end-start) /CLOCKS_PER_SEC;
    cout<<time_used;
    //arr[i]=rand() % 100 +1;
    return 0;
}
#include<iostream>
#include<math.h>
using namespace std;
void second(int a[],int n)
{
    int p;
    int largest;
    int second;
    largest=a[0];
    second=a[0];
    for(int i=1;i<n;i++)
    {
        
        if(a[i]>largest)
        {
            second=largest;
            largest=a[i];
        }
        else if(a[i]>second)
        second=a[i];
        
    }
    cout<<"Second largest element is: "<<second;
}   

int main()
{
    int a[9]={11,28,3,42,58,6,74,8,9};
    second(a,9);
    return 0;
}

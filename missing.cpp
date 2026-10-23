#include<iostream>
using namespace std;
void display(int a[],int n)
{
    for(int i=0;i<n;i++)
    {
        cout<<a[i]<<" "<<endl;
    }
}
void missing(int a[],int n)
{
    for(int i=1;i<n+1;i++)
    {
        int flag=0;
        for (int j=0;j<n;j++)
        {
            if(a[j]==i)
            {
                flag=1;
                break;
            }
        }
        if(flag==0)

        {
            cout<<"Missing number is: "<<i<<endl;
            
        }
    }
}
int main()
{
    int a[5]={1,3,3,5,6};
    display(a,5);
    missing(a,5);
   
    
    return 0;
}

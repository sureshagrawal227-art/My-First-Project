#include<iostream>
#include<math.h>
using namespace std;
void palindrome(int n)
{
    int x=n;
    int rev=0;
    while(x!=0)
    {
        int r=x%10;
        rev=rev*10+r;
        x=x/10;
    }
    cout<<rev<<" is reverse of "<<n<<endl;
    if(rev==n)
    cout<<"this is a palindrome.";
    else
    cout<<"this is not a palindrome.";
    
}
int main()
{
    int n;
    cin>>n;
    palindrome(n);
    return 0;
    
}

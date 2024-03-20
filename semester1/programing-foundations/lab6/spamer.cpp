#include<iostream>
#include<string>
using namespace std;

int main()
{
    int t,l=0;
    string v[100],x;
    cin>>t;
    for(int i =0;i<t;++i)
    {
        cin>>v[i];
    }
    cin >>x;
    for(int i =0;i<t;++i)
    {
        if(v[i]==x) l+=1;
    }

    cout<<l;


    return 0;
}
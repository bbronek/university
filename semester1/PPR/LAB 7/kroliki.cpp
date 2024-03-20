#include<iostream>
using namespace std;

int kroliki(int m) { return m<3?1:kroliki(m-1)+2*kroliki(m-3); }

int main()
{
    int t;
    cin>>t;
    while(t>0)
    {
        int m;
        cin>>m;
        cout<<kroliki(m)<<endl;
        t--;
    }
    return 0;
}
#include<iostream>
#include<string>
using namespace std;
int queq[100],e = -1,beg = 0;
void push(int x)
{
    e++;
    queq[e] = x;
}
int pop()
{
    beg++;
    return queq[beg-1];
}
int empty()
{
    return beg>e;
}
int full()
{
    if((e-beg+1)==10) return 1;
    return 0;
}

string c;
int x,b=0;
int main()
{

    do
    {
        cin>>c;
        if(c=="ENQUEUE")
        {
            if(full())
            {
                b =1;
            }
            else
            {
                cin>>x;
                push(x);
            }


        }
        if(c=="DEQUEUE")
        {
            if(empty())
            {
                b =1;
            }
            else
            {
                pop();
            }
        }

    }while(c!="END");

    if(b==1)
    {
        cout<<"error";
        return 0;
    }


    for(int i=beg;i<=e;++i)
    {
        cout<<queq[i]<<endl;
    }



    return 0;
}
#include<iostream>
#include<string>
using namespace std;
int stack[100],size = 0;
void push(int x)
{
    stack[size] = x;
    size++;
}
int pop()
{
    size--;
    return stack[size];
}
int empty()
{
    if(size==0) return 1;
    return 0;
}
int full()
{
    if(size==100) return 1;
    return 0;
}

string c;
int x,b=0;
int main()
{

    do
    {
        cin>>c;
        if(c=="PUSH")
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
        if(c=="POP")
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


    for(int i=size-1;i>=0;--i)
    {
        cout<<stack[i]<<endl;
    }



    return 0;
}
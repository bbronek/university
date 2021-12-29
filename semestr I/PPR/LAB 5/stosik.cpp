#include <iostream>

using namespace std;
int stack[100];

int main()
{

    int p = 0;
    int n,e;
    cin >> n;
    for(int i=0;i<n;i++)
    {
        char c;
        cin >> c;
        if(c=='+')
        {
            if(p==100)
            {
                cout << "full" << endl;
                cin >> e;
            }
            else
            {
                cin >> stack[p];
                p++;
            }

        }
        if(c=='-')
        {
            if(p==0)
            {
                cout << "empty" << endl;
            }
            else
            {
                cout << stack[p-1] << endl;
                p--;
            }
        }
    }

    for(int i=p-1;i>=0;i--)
    {
        cout << stack[i] << " ";
    }
}

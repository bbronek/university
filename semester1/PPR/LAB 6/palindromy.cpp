#include <string>

using namespace std;

string odwrocony;
void palindrom(string wyraz)
{
    int dlugosc = wyraz.length();

    for(int i = 0; i < dlugosc; i++)
    {
        odwrocony += wyraz[dlugosc - i - 1];
    }

}

int n;
int main()
{
    string wyraz;
    cin >>n;
    for(int i=0;i<n;++i)
    {
        odwrocony="";
        cin>>wyraz;
        palindrom(wyraz);
        if(wyraz ==odwrocony)
            cout<<wyraz<<"=="<<odwrocony;
        else
            cout<<wyraz<<"!="<<odwrocony;
    }


    return 0;
}
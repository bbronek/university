#include <stdio.h>
#include <string.h>


short r,n,s1=-1,s2=0;
int main()
{
    /* wczytanie danych tablica z 2 wierszami input i output ,
    czyli ile osob ich zna , a ile oni */

    scanf("%hd",&r);
    for(int i=0;i<r;++i)
    {
        scanf("%hd",&n);
        int v[n+2][n];
        memset(v, 0, sizeof(v[0][0]) * (n+2) * n);
        for(int d =0;d<n;++d)
        {
            s1 = -1;
            for(int j=0;j<n;++j)
            {
                scanf("%d",&v[d][j]);
                if(v[d][j])
                {
                    s1+=1;
                    v[n][j]++;
                }

            }
            v[n+1][d] = s1;

        }

        //Koniec wczytania pojedynczej tablicy i rozwiazanie liniowe

        for(int x =0;x<n;++x)
        {
            if(v[n+1][x] == 0 && v[n][x] == n)
            {
                printf("%hd",(x+1));
                break;
            }

        }

    }

    return 0;
}
#include<bits/stdc++.h>
using namespace std;


struct info
{
    int i;
    char name[100];
};

int main()
{
    int n;
    cout << "How many people : ";
    cin >> n;
    bool matrix[n + 1][n + 1];
    memset(matrix, false, sizeof(matrix));
    info x[n + 1];
    // for(int i = 0; i < n; i++)
    // {
    //     cout << "[" << i << "]" << " name : ";
    //     cin >> x[i].name;
    //     x[i].i = i;
    // }

    int m;
    cout << "How many relations : ";
    cin >> m;

    if(m != 0) cout << "Use a number instead of a name.\n";
    
    for(int i = 0; i < m; i++)
    {
        cout << i + 1 << ": ";
        int a, b;
        cin >> a >> b;
        matrix[a][b] = true;
        matrix[b][a] = true;
    }

    // relations matrix
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            cout << matrix[i][j] << " "; 
        }
        cout << endl;
    }
    queue<int> ans;
    queue<int> q;

    int nubans = 0;
    //finding
    for(int i = 0; i < n - 1; i++)
    {
        for(int j = i + 1; j < n; j++)
        {
            int nub = 0;
            for(int k = 0; k < n; k++)
            {
                if(matrix[i][k] && matrix[j][k])
                {
                    nub++;
                    q.push(k);
                }
            }
        }
    }

}
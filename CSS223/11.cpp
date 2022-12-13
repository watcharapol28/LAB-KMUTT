#include<iostream>
#include<queue>
#include<cstring>
using namespace std;


int main()
{
    int n = 5;
    bool matrix[n + 1][n + 1] = {{0,1,0,0,0},
    {0,1,0,0,0},
    {0,1,0,0,0},
    {0,1,0,0,0},
    {0,1,0,0,0}};
    memset(matrix, false, sizeof(matrix));


    // relations matrix

    cout << endl << "Relations matrix" << endl;
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            cout << matrix[i][j] << " "; 
        }
        cout << endl;
    }
    cout << endl;

    queue<int> ans;
    queue<int> q;

    int nubans = 0, ans_a, ans_b;
    //finding
    for(int i = 0; i < n - 1; i++)// o(n)
    {
        for(int j = i + 1; j < n; j++)// o(n)
        {   
            int nub = 0;
            
            for(int k = 0; k < n + 1; k++) // o(n)
            {
                if(matrix[i][k] && matrix[j][k] && k<=n)
                {
                    nub++;
                    q.push(k);
                }
            }

            if(nub > nubans) //answer   if new > old
            {
                ans_a = i;
                ans_b = j;
                while(!ans.empty())
                {
                    ans.pop();
                }
                while(!q.empty())
                {
                    ans.push(q.front());
                    q.pop();
                }
            }
            else //clear queue
            {
                while(!q.empty())
                {
                    q.pop();
                }
            }
        }
    }

    cout << ans_a  << " and " << ans_b  << " have mutual friends \n: ";
    while(!ans.empty())
    {
        cout << ans.front()<< " ";
        ans.pop();
    }

    cout << endl << endl;
}

/*
5
5
0 1
0 2
0 3
1 2
1 3
*/
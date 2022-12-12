#include<iostream>
#include<queue>
#include<cstring>
using namespace std;


struct info
{
    int i;
    string name;
};

int main()
{
    int n;
    cout << "How many people : ";
    cin >> n;
    bool matrix[n + 1][n + 1];
    info student[n + 1];
    memset(matrix, false, sizeof(matrix));

    for(int i = 0; i < n; i++)
    {
        student[i].i = i;
        cout << i << ".name : ";
        cin >> student[i].name;
    }
    cout << endl;

    int m, dp_min[n], dp_max[n] = {}; //เก็บตำแหน่ง min max ที่มีค่าเป็น True ของทุกแถวเพื่อให้ลดเวลาในการเปรียบเทียบที่ไม่จำเป็น for min - max จาก 0 - n
    for(int i = 0; i < n; i++)
    {
        dp_min[i] = n;
    }

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
        if(dp_min[a] > b){dp_min[a] = b;} //เก็บตำแหน่ง min max ที่มีค่าเป็น True ของทุกแถว
        if(dp_max[a] < b){dp_max[a] = b;}
        if(dp_min[b] > a){dp_min[b] = a;}
        if(dp_max[b] < a){dp_max[b] = a;}

    }

    // relations matrix

    cout << endl << "Relations matrix" << endl;
    for(int i = 0; i < n; i++)
    {
        cout << student[i].name << "\t";
        for(int j = 0; j < n; j++)
        {
            cout << matrix[i][j] << " "; 
        }
        cout << endl;
    }
    cout << endl;
    // for(int i = 0; i < n; i++)   // check min[i] and max[i]
    // {
    //     cout << i << " min" << dp_min[i] << " max" << dp_max[i] << endl;
    // }
    queue<int> ans;
    queue<int> q;

    int nubans = 0, ans_a, ans_b;
    //finding
    for(int i = 0; i < n - 1; i++)// o(n)
    {
        for(int j = i + 1; j < n; j++)// o(n)
        {   
            int nub = 0, mn = max(dp_min[i], dp_min[j]), mx = min(dp_max[i], dp_max[j]);

            for(int k = mn; k < mx + 1; k++) // o(max - min) ~~ o(m)
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

    cout << "[" << ans_a << "]"<< student[ans_a].name  << " and " << "[" << ans_b << "]" << student[ans_b].name  << " have mutual friends \n: ";
    while(!ans.empty())
    {
        cout << "[" << ans.front() << "]" << student[ans.front()].name << " ";
        ans.pop();
    }

    cout << endl << endl;
}

/*
5
nut
ohm
kitti
kla
pong
5
0 1
0 2
0 3
1 2
1 3
*/
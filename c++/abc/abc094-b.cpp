#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int inf = 1000000000; //10^9

int main(){
    int N, M, X;
    cin >> N >> M >> X;
    vector<int> A(M);
    for(int i = 0; i < M; i++){
        cin >> A.at(i);
    }
    int cost1 = 0;
    int cost2 = 0;
    for (int j = 0; j < M; j++)
    {
        if(X > A.at(j)){
            cost1++;
        }else{
            cost2++;
        }
    }
    cout << min(cost1, cost2) << endl;
}

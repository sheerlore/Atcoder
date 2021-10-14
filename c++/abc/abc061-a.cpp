#include <bits/stdc++.h>
using namespace std;

int main(){
    int N, M;
    cin >> N >> M;
    vector<int> a(M);
    vector<int> b(M);
    vector<int> ans(N);
    for(int i = 0; i < M; i++){
        cin >> a.at(i) >> b.at(i);
        ans.at(a.at(i) - 1)++;
        ans.at(b.at(i) - 1)++;
    }
    for(int i = 0; i < N; i++){
        cout << ans.at(i) << endl;
    }
}
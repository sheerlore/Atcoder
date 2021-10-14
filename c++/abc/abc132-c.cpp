#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int inf = 1000000000; //10^9

int main(){
    int N; cin >> N;
    vector<int> v(N);
    for(int i = 0; i < N; i++){
        cin >> v.at(i);
    }
    sort(v.begin(), v.end());
    int ans = v[v.size() / 2] - v[v.size() / 2 - 1];
    cout << ans << endl;
}

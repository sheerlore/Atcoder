#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int inf = 1000000000; //10^9

int main(){
    int n;
    cin >> n;
    vector<int> v(n), p(n), q(n);
    for (int i = 0; i < n; i++){
        cin >> p.at(i);
    }
    for (int i = 0; i < n; i++){
        cin >> q.at(i);
    }
    for(int i = 0; i < n; i++){
        v[i] = i + 1;
    }
    map<vector<int>, int> mp;
    do{
        mp[v] = mp.size();
    } while (next_permutation(v.begin(), v.end()));

    int ans = abs(mp[p] - mp[q]);
    cout << ans << endl;
}

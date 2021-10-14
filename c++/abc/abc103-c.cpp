#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(){
    int n;
    cin >> n;
    vector<int> a(n);
    int b = 1;
    for (int i = 0; i < n; i++)
    {
        cin >> a.at(i);
    }
    int ans = 0;
    for (int i = 0; i < n; i++)
    {
        ans += a.at(i) - 1;
    }
    cout << ans << endl;
}
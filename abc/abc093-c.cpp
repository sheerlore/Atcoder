#include <bits/stdc++.h>
using namespace std;

int main(){
    vector<int> n(3);
    cin >> n.at(0) >> n.at(1) >> n.at(2);

    sort(n.begin(), n.end());
    int ans = 0;
    int a1;
    int b1;
    while (n.at(2) != n.at(0) && n.at(2) != n.at(1))
    {
        a1 = n.at(2) - n.at(0);
        b1 = n.at(2) - n.at(1);
        while(a1 != 1 || a1 != 0){
            n.at(0) += (a1 / 2) * 2;
            ans += (a1 / 2);
            a1 -= (a1 / 2) * 2;
        }
        while(b1 != 1 || b1 != 0){
            n.at(1) += (b1 / 2) * 2;
            ans += (b1 / 2);
            b1 -= (b1 / 2) * 2;
        }
        if(a1 == 1 && b1 == 1){
            ans++;
            n.at(0) += 1;
            n.at(1) += 1;
            break;
        }
        sort(n.begin(), n.end());
    }
    cout << ans << endl;
}
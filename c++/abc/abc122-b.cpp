#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int inf = 1000000000; //10^9

int main(){
    string S;
    cin >> S;
    string temp = "ACGT";
    ll ans = 0;
    ll cnt = 0;
    int i = 0;
    while(i < S.size()){
        if(temp.find(S[i]) == string::npos){
            cnt = 0;
        }else{
            cnt++;
        }
        ans = max(ans, cnt);
        i++;
    }
    cout << ans << endl;
}
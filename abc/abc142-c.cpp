#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int inf = 1000000000; //10^9

int main(){
    int N;
    cin >> N;
    vector<int> a(N);
    for(int i = 0; i < N; i++){
        cin >> a[i];
    }
    vector<int> ans(N, 0);

    for(int i = 0; i < N; i++){
        ans.at(a.at(i)- 1) = i + 1;
    }
    
    for(int j = 0; j < N; j++){
        cout << ans.at(j) << " ";
    }
    cout << endl;
}

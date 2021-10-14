#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int inf = 1000000000; //10^9

int main(){
    int N; cin >> N;
    vector<float> v(N);
    for(int i = 0; i < N; i++){
        cin >> v.at(i);
    }
    sort(v.begin(), v.end());
    for(int i = 0; i < N - 1; i++ ){
        v.at(i + 1) = (v.at(i) + v.at(i + 1)) / 2;
    }
    cout << v.at(N - 1) << endl;
}

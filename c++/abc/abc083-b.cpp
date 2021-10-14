#include <bits/stdc++.h>
using namespace std;

int dsum(int n){
    int a = n;
    int r = 0;
    while (a != 0)
    {
        r += a % 10;
        a /= 10;
    }
    return r;
}

int main(){
    int N, A, B;
    cin >> N >> A >> B;
    int ans = 0;
    int tmp;
    for (int i = 1; i <= N; i++)
    {
        tmp = dsum(i);
        if(tmp >= A && tmp <= B){
            ans += i;
        }
    }
    cout << ans << endl;
}
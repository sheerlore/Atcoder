#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int inf = 1000000000; //10^9

bool is_prime(int x){
    if(x <= 1) return false;
    for (int i = 2; i*i < x; i++){
        if(x%i == 0)
            return false;
    }
    return true;
}


int main(){
    int x;
    cin >> x;
    int p = x;
    while(!is_prime(p)) p++;
    cout << p << endl;
}
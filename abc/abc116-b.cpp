#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int inf = 1000000000; //10^9

int f(int n){
    if(n%2 == 0){
        return n / 2;
    }
    else
    {
        return 3 * n + 1;
    }
}

int main(){
    int s;
    cin >> s;
    vector<int> a(1000001, 0);
    int i = 1;
    a.at(s) += 1;
    do{
        i = i + 1;
        s = f(s);
        a.at(s) += 1;
    } while (a.at(s) != 2);
    cout << i << endl;
}

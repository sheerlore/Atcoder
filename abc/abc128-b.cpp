#include <bits/stdc++.h>
using namespace std;

int main(){
    char in[120];
    pair<pair<string, int>, int> p[110];
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n; i++){
        int t;
        scanf("%s%d", in, &t);
        string temp = in;
        p[i] = make_pair(make_pair(in, -t), i);
    }
    sort(p, p+n);
    for(int i = 0; i < n; i++){
        printf("%d\n", p[i].second + 1);
    }
}
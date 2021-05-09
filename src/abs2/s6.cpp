#include <bits/stdc++.h>
using namespace std;

int INF = 1000000000;

int N;
int a[110];
  
int main() {
  cin >> N;
  for (int i = 0; i < N; i++) cin >> a[i];

  int alice = 0;
  int bob = 0;

  sort(a, a + N, greater<int>());

  for (int i = 0; i < N; i++) {
    if (i % 2 == 0) alice += a[i];
    else bob += a[i];
  }

  cout << alice - bob << endl;
  return 0;
}
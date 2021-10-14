#include <bits/stdc++.h>
using namespace std;
  
int main() {

  int N;
  int a[110];

  cin >> N;
  for(int i = 0; i < N; i++) cin >> a[i];


  sort(a, a+N, greater<int>()); //a[0:N]を大きい順にソート

  int alice_point = 0;
  int bob_point = 0;

  for (int i = 0; i < N; i++ ) {
    if (i % 2 == 0) { // Alice
      alice_point += a[i];
    } else { // Bob
      bob_point += a[i];
    }
  }

  cout << alice_point - bob_point << endl;
  return 0;
}
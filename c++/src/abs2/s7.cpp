#include <bits/stdc++.h>
using namespace std;

int N;
int d[110];
  
int main() {
  // 自分の解法---------------------------------------------
  cin >> N;
  for (int i = 0; i < N; i++) cin >> d[i];

  sort(d, d+N, greater<int>());

  int res = 1;
  int mochi = d[0]; // 一番最初に一番大きいモチを乗せる
  for (int i = 1; i < N; i++) {
    if (mochi == d[i]) continue;
    else {
      mochi = d[i];
      res++;
    }
  }

  cout << res << endl;
  return 0;


  // けんちょんさんの解法１-----------------------------------

  // cin >> N;
  // for (int i = 0; i < N; i++) cin >> d[i];

  // int num[110] = {0}; // バケット

  // for (int i = 0; i < N; i++) num[d[i]]++;

  // int res = 0;
  // for (int i = 0; i <= 100; i++ ) {
    // if (num[i]) {
      // res++;
    // }
  // }

  // cout << res << endl;

  // けんちょんさんの解法２-------------------------------------
  // cin >> N;
  // for (int i = 0; i < N; i++) cin >> d[i];

  // set<int> values; // insertするときに重複を取り除いてくれる
  // for (int i = 0; i < N; i++) {
  //   values.insert(d[i]);
  // }


  // cout << values.size() << endl;
}
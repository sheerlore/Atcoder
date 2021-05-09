#include <bits/stdc++.h>
using namespace std;

int calcSum(int n) {
  int res = 0;
  while (n != 0) {
    int a = n % 10;
    n /= 10;
    res += a;
  }

  return res;
}
  
int main() {
  int N, A, B;
  cin >> N >> A >> B;

  int res = 0;
  for (int i = 1; i <= N; i++) {
    int num = calcSum(i); // ここに数字の各桁の合計の数値を入れる
    if (num >= A && num <= B) res += i;
  }

  cout << res << endl;
  return 0;
}
#include <bits/stdc++.h>
using namespace std;
  
int main() {
  int N, A;
  cin >> N >> A;
  int temp = N % 500;
  if (A >= temp) cout << "Yes" << endl;
  else cout << "No" << endl;
  return 0;
}
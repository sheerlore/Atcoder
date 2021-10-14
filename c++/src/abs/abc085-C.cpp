#include <bits/stdc++.h>
using namespace std;
  
int main() {

  int N, Y;
  cin >> N >> Y;

  vector<int> res(3, -1);

  for (int x = 0; x <= N; x++) {
    for (int y = 0; y + x <= N; y++) {
      int z = N - x - y;
      int total = 10000*x + 5000*y + 1000*z;

      if (total == Y) {
        res.at(0) = x;
        res.at(1) = y;
        res.at(2) = z;
      }
    }
  }


  cout << res.at(0) << " " << res.at(1) << " " << res.at(2) << endl;

  
  return 0;
}
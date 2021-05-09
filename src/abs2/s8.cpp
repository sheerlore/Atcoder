#include <bits/stdc++.h>
using namespace std;
  
int main() {
  int N, Y;
  cin >> N >> Y;

  int res[3] = {-1, -1, -1};

  for (int x = 0; x <= N; x++) {
    for (int y = 0; x + y <= N; y++) {
      int z = N - x - y;

      int total = 10000*x + 5000*y + 1000*z;
      if (total == Y) {
        res[0] = x;
        res[1] = y;
        res[2] = z;
      }
    }
  }

  cout << res[0] << " " << res[1] << " " << res[2] << endl;
  return 0;
}
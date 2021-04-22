#include <bits/stdc++.h>
using namespace std;
int N;
vector<int> A(210); 
  
int main() {
  cin >> N;
  for (int i = 0; i < N; i++ ) cin >> A.at(i);

  int res = 0;

  // Repeat the operation as long as it can be performed.
  while(true) {
    bool exist_odd = false;
    for (int i = 0; i < N; i++) {
      if (A.at(i) % 2 != 0) exist_odd = true;
    }

    // if there is odd number, break
    if (exist_odd) break;

    for (int i = 0; i < N; i++) {
      A.at(i) /= 2;
    }

    res++;
  }

  cout << res << endl;


  return 0;
}
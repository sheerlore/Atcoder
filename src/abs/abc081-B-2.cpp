#include <bits/stdc++.h>
using namespace std;

const int INF = 10000000;

int N;
int A[210];
  
int main() {

  cin >> N;
  for (int i = 0; i < N; i++) cin >> A[i];

  int res = INF;

  for (int i = 0; i < N; i++) {
    int count = 0; // 何回2で割れるか

    while(A[i] % 2 == 0) {
      A[i] /= 2;
      count++;
    }


    if (res > count ) res = count;
  }

  cout << res << endl;
   
  return 0;
  
}
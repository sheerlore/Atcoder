#include <bits/stdc++.h>
using namespace std;

int main() {
  vector<int> a = {1, 3, 5, 7};
  for (int i=0; i<a.size(); i++) {
    cout << a.at(i) << endl;
  }

  for (int x : a) {
    cout << x << endl;
  }
}
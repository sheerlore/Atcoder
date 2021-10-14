#include <bits/stdc++.h>
using namespace std;

string devide[4] = {"dream", "dreamer", "erase", "eraser"};
  
int main() {
  string s;
  cin >> s;

  // 文字を逆にする
  reverse(s.begin(), s.end());
  for (int i = 0; i < 4; i++) reverse(devide[i].begin(), devide[i].end());

  bool  can = true;
  for (int i = 0; i < s.size();) {
    bool can2 = false; // 4この文字列達のどれかでdevide できるか
    for (int j = 0; j < 4; j++) {
      string d = devide[j];
      if (s.substr(i, d.size()) == d) {
        can2 = true;
         i += d.size(); 
      }
    }

    if (!can2) {
      can = false;
      break;
    }
  }


  if (can) cout << "YES" << endl;
  else cout << "NO" << endl;

  return 0;
}
#include <bits/stdc++.h>
using namespace std;

int main(){
    int h, w;
    cin >> h >> w;
    vector<vector<char> > out(h + 2, vector<char>(w + 2));
    for (int i = 0; i <= h + 1; i++){
        for (int j = 0; j <= w + 1; j++)
        {
            if (i == 0 || j == 0|| i == h + 1 || j == w + 1){
                out.at(i).at(j) = '#';
                cout << out.at(i).at(j);
            }
            else
            {
                cin >> out.at(i).at(j);
                cout << out.at(i).at(j);
            }
        }
        cout << endl;
    }
}
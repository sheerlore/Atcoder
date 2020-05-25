#include <bits/stdc++.h>
using namespace std;

int main(){
    string s;
    cin >> s;
    sort(s.begin(), s.end());
    char charcmp = 'a';
    int i = 0;
    if(s[i] != charcmp){
        cout << charcmp << endl;
        return 0;
    }
    while (charcmp != 'z')
    {
        while (s[i] == charcmp){
            i++;
        }
        charcmp++;
        if (s[i] != charcmp){
            cout << charcmp << endl;
            return 0;
        }
    }
    cout << "None" << endl;
    return 0;
}
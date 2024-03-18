#include <iostream>

using namespace std;

int f(int k, int n){
    if (k == -1 || n == 1)
        return 1;
    else
        return f(k-1, n) + f(k, n-1);
}

int main(){
    int c, k, n;
    cin >> c;
    for (int i = 0; i < c; i++){
        cin >> k;
        cin >> n;
        
        cout << f(k, n) << endl;
    }
}
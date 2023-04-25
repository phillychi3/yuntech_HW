#include <iostream>
#include <cmath>
using namespace std;
int main() {
    int n, m;
    cin >> n >> m;
    for (int i = n; i <= m; i++) {
        int sum = 0;
        int temp = i;
        int len = to_string(i).length(); 
        while (temp > 0) {
            sum += pow(temp % 10, len);
            temp /= 10;
        }
        if (sum == i) cout << i << endl; 
    }
    return 0;
}
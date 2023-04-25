#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;

    int sum = 0;
    for (int i = 1; i * i <= N; i++) {
        sum += i * i;
    }

    cout << sum << endl;

    return 0;
}
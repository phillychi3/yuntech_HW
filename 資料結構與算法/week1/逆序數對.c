#include <iostream>
#include <vector>
using namespace std;

int main() {
	vector<int> oxo;
	int count;
	cin >> count;
	oxo.resize(count);
	for (int i = 0; i < count; i++)
		cin >> oxo[i];

	int sum = 0;
	for (int i = 0; i < count; i++)
		for (int j = i + 1; j < count; j++)
			if (oxo[i] > oxo[j]) sum++;

	cout << sum;
	return 0;
}

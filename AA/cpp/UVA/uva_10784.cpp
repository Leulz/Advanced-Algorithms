#include <iostream>

using namespace std;

int counter = 0;

int main() {
	while (true) {
		long d;

		cin >> d;

		if (d==0) {
			break;
		}

		long left = 4, right = 100000010, mid = 0;

		while(left < right) {
			mid = (left + right)/2;

			if ((mid * (mid-3)) >= d*2) {
				right = mid;
			} else {
				left = mid + 1;
			}
		}
		cout << "Case " << ++counter << ": " << left << "\n";
	}
	return 0;
}
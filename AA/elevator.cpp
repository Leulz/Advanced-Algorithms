#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	int T;
	
	cin >> T;
	
	int NCM [3];
	
	for (int i = 0; i<T; i++) {
		cin >> NCM[0] >> NCM[1] >> NCM[2];
				
		int floors [NCM[2]];
		
		int temp;
		
		for (int j = 0; j<NCM[2]; j++) {			
			cin >> temp;
			
			floors[j] = temp;
		}
		
		sort(floors,floors + NCM[2]);
		
		int counter = 0;
		
		int ans = 0;
		
		for (int j = NCM[2]-1; j>=0; j--) {
			if (counter==0) {
				ans += floors[j] * 2;
			}
			counter++;
			
			if (counter==NCM[1]) {
				counter = 0;
			}
		}
		cout << ans << '\n';
	}
	
	return 0;
}

#include <iostream>
using namespace std;

  int mod = 1000000007ll;

  int main() {
       int N;
       cin >> N;

       long long ans = 0;
       if (N == 1) {
            cout << 0;
            return 0;
       }

       long long threes = 1;
       long long prev = 0;
       long long cur = 0;
       for (int i = 2; i <= N; i++) {
            threes = 3ll*threes;
            cur = threes - prev;
            if (cur < 0) cur +=mod;
            threes %= mod;
            cur %= mod;
            prev = cur;
       }

       cout << cur;
       return 0;
}
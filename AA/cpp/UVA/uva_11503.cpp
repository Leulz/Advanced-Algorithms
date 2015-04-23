#include <bits/stdc++.h>

using namespace std;

#define MAX_N 100100

class Union_Find {

public:
    int p[MAX_N], rank[MAX_N], size[MAX_N];

    Union_Find(int n) {
        for (int i = 0; i < n; i++) {
            p[i] = i;
            rank[i] = 0;
            size[i] = 1;
        }
    }

    int find(int n) {
        return (p[n] == n) ? n : (p[n] = find(p[n]));
    }

    bool is_same_set(int i, int j) {
        return find(i) == find(j);
    }

    void union_set(int i, int j) {
        if (!is_same_set(i, j)) {
            int x = find(i), y = find(j);
            if (rank[x] > rank[y]) {
                p[y] = x;
                size[x] += size[y];
            } else {
                p[x] = y;
                size[y] += size[x];
                if(rank[x] == rank[y]) rank[y]++;
            }
        }
    }
    int set_size(int n) {
        return size[find(n)];
    }
};




int main() {
    int k;
    cin >> k;

    while(k--) {
        int n;
        Union_Find UF(MAX_N);
        map<string, int> M;

        cin >> n;

        int cnt = 0;
        for (int i = 0; i < n; i++) {
            string a, b;
            cin >> a >> b;
            int x = (M[a] == 0) ? M[a] = ++cnt : M[a];
            int y = (M[b] == 0) ? M[b] = ++cnt : M[b];
            UF.union_set(x, y);
            printf("%d\n", UF.set_size(x));
        }
    }
}
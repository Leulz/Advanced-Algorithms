using namespace std;

#include <algorithm>
#include <stdio.h>
#include <vector>

#define vi vector<int>

class SegmentTree {
private:	
	int n;
	vector<int> st, arr;

	int left(int p) {
		return p << 1;
	}

	int right(int p) {
		return (p << 1) + 1;
	}

	void build(int p, int L, int R) {
		if (L==R) {
			st[p] = arr[L];
		} else{
			build(left(p), L, (L + R)/2);
			build(right(p), (L+R)/2 + 1, R);

			int p1 = st[left(p)], p2 = st[right(p)];

			st[p] = min(p1, p2);
		}
	}

	int query(int p, int L, int R, int i, int j) {
		if (i > R || j < L) {
			return 0;
		}
		if (L >= i && R <= j) {
			return st[p];
		}

		int mid = (L + R)/2;

		if (i > mid) {
			return query(right(p), mid+1, R, i, j);
		}
		if (j<=mid) {
			return query(left(p), L, mid, i, j);
		}

		int leftNodeMinimum = query(left(p), L, (L + R)/2, i, j);
		int rightNodeMinimum = query(right(p), (L+R)/2 + 1, R, i, j);

		return min(leftNodeMinimum, rightNodeMinimum);
	}
public:
	SegmentTree(const vector<int> &_v) {
		arr = _v; n = (int)arr.size();
		st.reserve((4 * n));
		build(1, 0, n-1);
	}

	int query(int i, int j) {
		return query(1, 0, n-1, i, j);
	}
};

int main() {
	int T;
	scanf("%d", &T);

	int scenario = 1;

	for (int i = 0; i < T; i++)
	{
		if (scenario!=1) {
			printf("\n");
		}
		printf("Scenario #%d:\n", scenario++);
		
		int N, Q;

		scanf("%d %d", &N, &Q);
		
		int arr[N];

		for (int i = 0; i < N; i++)
		{
			scanf("%d", arr + i);
		}

		int size = (sizeof(arr)/sizeof(arr[0]));

		vi v(arr, arr+size);

		SegmentTree st(v);

		int A, B;

		for (int i = 0; i < Q; i++)
		{
			scanf("%d %d", &A, &B);

			printf("\n%d\n", st.query(A-1, B-1));
		}

	}

	return 0;
}
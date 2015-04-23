using namespace std;

#include <algorithm>
#include <stdio.h>
#include <vector>

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

			st[p] = p1 + p2;
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

		int leftNodeSum = query(left(p), L, (L + R)/2, i, j);
		int rightNodeSum = query(right(p), (L+R)/2 + 1, R, i, j);

		return leftNodeSum + rightNodeSum;
	}

	void update(int p, int L, int R, int index, int diff) {
		if (index > R || index < L) {
			return;
		}

		if (index == L && L == R) {
			st[p] += diff;
			arr[index] += diff;
			return;
		}

		int mid = (L + R)/2;

		if (index <= mid) {
			update(left(p), L, mid, index, diff);
		}
		if (index > mid) {
			update(right(p), mid + 1, R, index, diff);
		}

		int leftNodeSum = st[left(p)], rightNodeSum = st[right(p)];

		st[p] = leftNodeSum + rightNodeSum;
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

	void update(int index, int val) {
		int diff = val - arr[index];
		update(1, 0, n-1, index, diff);
	}
};

int main() {
	int N;
	int cas = 1;

	while (true) {
		scanf("%d", &N);

		if (N != 0 && cas != 1) {
			printf("\nCase %d:\n", cas++);
		} else if (cas == 1) {
			printf("Case %d:\n", cas++);
		} else {
			break;
		}

		int arr[N];

		for (int i = 0; i < N; i++)
		{
			scanf("%d", arr + i);
		}

		int size = (sizeof(arr)/sizeof(arr[0]));

		vector<int> v(arr, arr+size);

		SegmentTree s(v);

		while (true) {
			char c;
			int x, y;

			scanf(" %c", &c);

			if (c == 'E') {
				scanf(" %c %c", &c, &c);
				break;
			} else if (c == 'M') {
				scanf("%d %d", &x, &y);
				printf("%d\n", s.query(x-1, y-1));
			} else {
				scanf("%d %d", &x, &y);
				s.update(x-1, y);
			}
		}
	}

	return 0;
}
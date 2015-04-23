using namespace std;

#include <algorithm>
#include <stdio.h>
#include <vector>

struct Node {
	int firstMax, maxSum;

	void createLeaf(int value) {
		firstMax = maxSum = value;
	}

	void buildNode(Node& left, Node& right) {
		firstMax = max(left.firstMax, right.firstMax);
		maxSum = max(left.maxSum, max(right.maxSum, left.firstMax + right.firstMax));
	}

	int value() {
		return maxSum;
	}
};

class SegmentTree {
private:	
	int n;
	vector<Node> st;
	vector<int> arr;

	int left(int p) {
		return p << 1;
	}

	int right(int p) {
		return (p << 1) + 1;
	}

	void build(int p, int L, int R) {
		if (L==R) {
			Node leaf;
			leaf.createLeaf(arr[L]);
			st[p] = leaf;
		} else{
			build(left(p), L, (L + R)/2);
			build(right(p), (L+R)/2 + 1, R);

			Node p1 = st[left(p)], p2 = st[right(p)];
			Node actualNode;
			actualNode.buildNode(p1, p2);

			st[p] = actualNode;
		}
	}

	Node searchMaxSum(int p, int L, int R, int i, int j) {
		if (i > R || j < L) {
			Node useless;
			useless.createLeaf(0);
			return useless;
		}
		if (L >= i && R <= j) {
			return st[p];
		}

		int mid = (L + R)/2;

		if (i > mid) {
			return searchMaxSum(right(p), mid+1, R, i, j);
		}
		if (j<=mid) {
			return searchMaxSum(left(p), L, mid, i, j);
		}

		Node leftNodeMaxSum = searchMaxSum(left(p), L, (L + R)/2, i, j);
		Node rightNodeMaxSum = searchMaxSum(right(p), (L+R)/2 + 1, R, i, j);

		Node response;

		response.buildNode(leftNodeMaxSum, rightNodeMaxSum);

		return response;
	}

	void update(int p, int L, int R, int index, int val) {
		if (index > R || index < L) {
			return;
		}

		if (index == L && L == R) {
			Node newLeaf;
			newLeaf.createLeaf(val);
			st[p] = newLeaf;
			return;
		}

		int mid = (L + R)/2;

		if (L != R){
			if (index <= mid) {
				update(left(p), L, mid, index, val);
			}
			if (index > mid) {
				update(right(p), mid + 1, R, index, val);
			}
		}

		Node leftNode = st[left(p)];
		Node rightNode = st[right(p)];

		st[p].firstMax = max(leftNode.firstMax, rightNode.firstMax);
		st[p].maxSum = max(leftNode.maxSum, max(rightNode.maxSum, leftNode.firstMax + rightNode.firstMax));
	}
public:
	SegmentTree(const vector<int> &_v) {
		arr = _v; n = (int)arr.size();
		st.reserve((4 * n));
		build(1, 0, n-1);
	}

	int searchMaxSum(int i, int j) {
		return searchMaxSum(1, 0, n-1, i, j).maxSum;
	}

	void update(int index, int val) {
		update(1, 0, n-1, index, val);
	}
};

int main() {
	int N;

	scanf("%d", &N);

	int arr[N];

	for (int i = 0; i < N; i++)
	{
		scanf("%d", arr + i);
	}

	int size = (sizeof(arr)/sizeof(arr[0]));

	vector<int> v(arr, arr+size);

	SegmentTree s(v);

	int Q;

	scanf("%d", &Q);

	for (int i = 0; i < Q; i++)
	{
		char c;
		int x, y;

		scanf(" %c %d %d", &c, &x, &y);

		if (c=='U') {
			s.update(x-1, y);
		} else {
			printf("%d\n", s.searchMaxSum(x-1,y-1));
		}
	}

	return 0;
}
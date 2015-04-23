using namespace std;

#define MAX_POS 50010
#define MAX_N 15015
#include <algorithm>
#include <stdio.h>
#include <vector>

struct Node {
	int prefixMaxSum, suffixMaxSum, totalSum, maxSum;

	void createLeaf(int value) {
		prefixMaxSum = suffixMaxSum = totalSum = maxSum = value;
	}

	void buildNode(Node& left, Node& right) {
		prefixMaxSum = max(left.prefixMaxSum, left.totalSum + right.prefixMaxSum);
		suffixMaxSum = max(right.suffixMaxSum, right.totalSum + left.suffixMaxSum);
		totalSum = left.totalSum + right.totalSum;
		maxSum = max(prefixMaxSum, max(suffixMaxSum, max(left.maxSum, max(right.maxSum, left.suffixMaxSum + right.prefixMaxSum))));
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
			Node uselessPath;
			uselessPath.createLeaf(-1);
			return uselessPath;
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

		if (L == R && index == L) {
			Node newLeaf;
			newLeaf.createLeaf(val);
			st[p] = newLeaf;
			return;
		}

		int mid = (L + R)/2;

		if (index > mid) {
			update(right(p), mid + 1, R, index, val);
		}
		if (index <= mid) {
			update(left(p), L, mid, index, val);
		}

		Node updatedNode;
		updatedNode.buildNode(st[left(p)], st[right(p)]);
		st[p] = updatedNode;
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
	int n;

	scanf("%d", &n);

	int A[n];

	for (int i = 0; i < n; i++) {
		scanf("%d", &A[i]);
	}

	vector<int> v(A, A+n);
	SegmentTree tree(v);

	int queries;

	scanf("%d", &queries);

	for (int i = 0; i < queries; ++i)
	{
		int c, a, b;

		scanf("%d %d %d", &c, &a, &b);

		if(c==0) {
			tree.update(a-1, b);
		} else {
			printf("%d\n", tree.searchMaxSum(a-1, b-1));
		}
	}

	return 0;
}
using namespace std;
 
#include <algorithm>
#include <stdio.h>
#include <vector>
#include <string>
#include <iostream>
 
class SegmentTree {
private:    
    int n;
    vector<char> st;
    vector<int> arr;
 
    int left(int p) {
        return p << 1;
    }
 
    int right(int p) {
        return (p << 1) + 1;
    }
 
    void build(int p, int L, int R) {
        if (L==R) {
            if (arr[L]>0) {
                st[p] = '+';    
            } else if (arr[L]<0) {
                st[p] = '-';
            } else {
                st[p] = '0';
            }
        } else{
            build(left(p), L, (L + R)/2);
            build(right(p), (L+R)/2 + 1, R);
 
            char p1 = st[left(p)], p2 = st[right(p)];
 
            if (p1 == '0' || p2 == '0') {
                st[p] = '0';                
            } else if ((p1 == '+' && p2 == '+') || (p1 == '-' && p2 == '-')) {
                st[p] = '+';
            } else {
                st[p] = '-';
            }
        }
    }
 
    char query(int p, int L, int R, int i, int j) {
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
 
        char p1 = query(left(p), L, (L + R)/2, i, j);
        char p2 = query(right(p), (L+R)/2 + 1, R, i, j);
 
        if (p1 == '0' || p2 == '0') {
            return '0';
        } else if ((p1 == '+' && p2 == '+') || (p1 == '-' && p2 == '-')) {
            return '+';
        } else {
            return '-';
        }
    }
 
    void update(int p, int L, int R, int index, int val) {
        if (index > R || index < L) {
            return;
        }
 
        if (index == L && L == R) {
            if (val>0) {
                st[p] = '+';    
            } else if (val<0) {
                st[p] = '-';
            } else {
                st[p] = '0';
            }
            arr[L] = val;
            return;
        }
 
        int mid = (L + R)/2;
 
        if (index <= mid) {
            update(left(p), L, mid, index, val);
        }
        if (index > mid) {
            update(right(p), mid + 1, R, index, val);
        }
 
        char p1= st[left(p)], p2 = st[right(p)];
 
        if (p1 == '0' || p2 == '0') {
            st[p] = '0';
        } else if ((p1 == '+' && p2 == '+') || (p1 == '-' && p2 == '-')) {
            st[p] = '+';
        } else {
            st[p] = '-';
        }
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
        update(1, 0, n-1, index, val);
    }
};
 
int main() {
    int N, K;
    //freopen ("myfile.txt","w",stdout);
 
    while(scanf("%d %d", &N, &K) != EOF) {
        int arr[N];
        for (int i = 0; i < N; i++)
        {
            scanf("%d", arr + i);
        }
        int size = (sizeof(arr)/sizeof(arr[0]));
 
        vector<int> v(arr, arr + size);
 
        SegmentTree st(v);
 
        char C;
        int A, B;
        string ans = "";
 
        for (int i = 0; i < K; i++)
        {
            scanf(" %c %d %d", &C, &A, &B);
 
            if (C == 'C') {
                st.update(A-1, B);
            } else {
                ans += st.query(A-1, B-1);
            }
        }
        cout << ans << endl;
        //printf("%s\n", ans);
    }
 
    //fclose (stdout);
 
    return 0;
}
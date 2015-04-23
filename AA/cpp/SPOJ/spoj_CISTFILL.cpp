using namespace std;

#define INF 1050000
#define MAX 50050
#define EPS 1e-9
#define MAX_CISTERNS 32
#include <stdio.h>
#include <algorithm>

struct cistern
{
	double b;
	double h;
	double w;
	double d;
};

int k, n;

cistern A[MAX];

double calc_volume(double max_height, double min_height, int n) {
	double volume = 0.0;

	for (int i = 0; i < n; ++i)
	{
		double h0 = max(A[i].b, min_height);
		double h1 = min(A[i].b + A[i].h, max_height);

		if (h0 + EPS < h1) {
			volume += (h1-h0)*A[i].d*A[i].w;
		}
	}

	return volume;
}

double solve(double max_height, double min_height, int n, double v) {
	double lo = min_height, hi = max_height;

	int cnt = 32;

	while (cnt--) {
		double mid = (hi + lo)/2.0;
		if (calc_volume(mid, min_height, n) + EPS > v) {
			hi = mid;
		} else {
			lo = mid;
		}
	}
	return lo;
}

int main() {
	scanf("%d", &k);
	double b, h, w, d, v, lo = INF, hi = -INF;
	for (int i = 0; i < k; i++)
	{
		scanf("%d", &n);

		for (int i = 0; i < n; i++)
		{
			scanf("%lf%lf%lf%lf", &b, &h, &w, &d);

			cistern cis;
			cis.b = b;
			cis.h = h;
			cis.w = w;
			cis.d = d;

			A[i] = cis;

			lo = min(lo, b);
			hi = max(hi, h + b);
		}

		scanf("%lf", &v);

		if ((calc_volume(hi, lo, n)+EPS < v)) {
			printf("OVERFLOW\n");
		} else {
			double ans = solve(hi, lo, n, v);
			printf("%.2f\n", ans);
		}
	}
	return 0;
}
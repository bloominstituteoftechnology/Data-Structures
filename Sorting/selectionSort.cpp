#define vi vector<int>
#define pb push_back
#define mp make_pair
#define ll long long int
#define mod 1000000007
#include <bits/stdc++.h>
using namespace std;
const int N = 1e6 + 5;


int main() {

#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int a = 4;


	int n;
	cin >> n;
	int arr[n];
	for (int i = 0; i < n; ++i) {
		cin >> arr[i];
	}

	for (int i = 0; i < n - 1; ++i) {
		int ind = i;
		int min = arr[i];
		for (int j = i + 1; j < n; ++j) {
			if (arr[j] < min) {
				min = arr[j];
				ind = j;
			}
		}
		swap(arr[i], arr[ind]);
	}
	for (int i = 0; i < n; ++i)
	{
		cout << arr[i] << " ";
	}
	return 0;
}
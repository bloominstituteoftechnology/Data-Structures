#define vi vector<int>
#define pb push_back
#define mp make_pair
#define ll long long int
#define mod 1000000007
#include <bits/stdc++.h>
using namespace std;
const int N = 1e6 + 5;

void randomShuffle(int *arr, int n) {

	srand(time(NULL));
	for (int i = 0; i < n; ++i) {

		int j = rand() % (i + 1);
		swap(arr[i], arr[j]);
	}
}

int partition(int *arr, int s, int e) {

	int i = s - 1;
	int j = s;
	int pivot = arr[e];

	for (; j < e; ++j) {
		if (arr[j] <= pivot) {
			i++;
			swap(arr[i], arr[j]);
		}
	}
	swap(arr[i + 1], arr[e]);
	return i + 1;
}

void quickSort(int *arr, int s, int e) {

	if (s >= e) {
		return;
	}

	int p = partition(arr, s, e);
	quickSort(arr, s, p - 1);
	quickSort(arr, p + 1, e);


}

int main() {

#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int n;
	cin >> n;
	int arr[n];
	for (int i = 0; i < n; ++i) {
		cin >> arr[i];
	}
	randomShuffle(arr, n);
	for (int i = 0; i < n; ++i) {
		cout << arr[i] << " ";
	}
	cout << endl;
	quickSort(arr, 0, n - 1);
	for (int i = 0; i < n; ++i) {
		cout << arr[i] << " ";
	}
	return 0;
}
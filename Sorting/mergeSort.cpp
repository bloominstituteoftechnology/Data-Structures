#define vi vector<int>
#define pb push_back
#define mp make_pair
#define ll long long int
#define mod 1000000007
#include <bits/stdc++.h>
using namespace std;
const int N = 1e6 + 5;


void merge(int *arr, int l, int r) {

	int i = l;
	int mid = (l + r) / 2;
	int j = mid + 1;
	int k = l;

	int temp[100];

	while (i <= mid && j <= r) {

		if (arr[i] < arr[j]) {
			temp[k++] = arr[i++];
		} else {
			temp[k++] = arr[j++];
		}
	}
	while (i <= mid) {
		temp[k++] = arr[i++];
	}
	while (j <= r) {
		temp[k++] = arr[j++];
	}

	for (int i = l; i <= r; ++i)
	{
		arr[i] = temp[i];
	}

}

void mergeSort(int arr[], int l, int r) {

	if (l >= r) {
		return;
	}
	// divide
	int mid = (l + r) / 2;

	// sort the array
	mergeSort(arr, l, mid);
	mergeSort(arr, mid + 1, r);

	// conquer
	merge(arr, l, r);

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

	mergeSort(arr, 0, n - 1);
	for (int i = 0; i < n; ++i)
	{
		cout << arr[i] << " ";
	}
	return 0;
}
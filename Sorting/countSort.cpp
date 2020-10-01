#define vi vector<int>
#define pb push_back
#define mp make_pair
#define ll long long int
#define mod 1000000007
#include <bits/stdc++.h>
using namespace std;
const int N = 1e6 + 5;

void countSort(int *arr, int n) {

    int output[n + 1];
    int count[100] = {0};

    for (int i = 0; i < n; ++i)
        count[arr[i]]++;

    for (int i = 1; i <= 100; ++i)
        count[i] += count[i - 1];

    for (int i = n - 1; i >= 0; --i) {
        output[count[arr[i]] - 1] = arr[i];
        --count[arr[i]];
    }

    for (int i = 0; i < n; ++i) {
        arr[i] = output[i];
    }
    for (int i = 0; i < n; ++i) {
        cout << output[i] << " ";
    }
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
    // cout << endl;
    countSort(arr, n);
    // quickSort(arr, 0, n - 1);
    for (int i = 0; i < n; ++i) {
        cout << arr[i] << " ";
    }
    return 0;
}
#include <bits/stdc++.h>
using namespace std;


int partition(int *a, int low, int high) {

	int i = low - 1;
	int j = low;
	int pivot = a[high];
	
	for(; j < high; j++) {
		
		if(a[j] <= pivot) {
			i++;
			swap(a[i], a[j]);
		}
	}

	swap(a[i+1], a[high]);
	return i + 1;
}

void quickSort(int *a , int low, int high) {
	
	if(low > high) return;
	
	int p = partition(a, low, high);
	quickSort(a, low, p - 1);
	quickSort(a, p + 1, high);
	
}
int main()
{

	int arr[] = {5, 4, 2, 1, 6};
	quickSort(arr, 0, 4);
	for (int i = 0; i < 5; ++i)	{
		/* code */
		cout<<arr[i]<<" ";
	}
	return 0;
}

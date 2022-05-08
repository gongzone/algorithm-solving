#include <iostream>
#include <climits>

int N;
int M;

int N_Arr[100000];

void Merge(int low, int mid, int high)
{
    int i,j;
    int L_Number = mid-low + 1;
    int R_Number = high - mid;

    int L[L_Number + 1];
    int R[R_Number + 1];

    for(i = 0; i < L_Number; i++)
        L[i] = N_Arr[low+i];

    for(j = 0; j < R_Number; j++)
        R[j] = N_Arr[mid+1 + j];

    L[L_Number] = INT_MAX;
    R[R_Number] = INT_MAX;

    i = 0;
    j = 0;

    for(int k = low; k <= high; k++)
    {
        if(L[i] <= R[j])
        {
            N_Arr[k] = L[i];
            i++;
        }
        else
        {
            N_Arr[k] = R[j];
            j++;
        }
    }
}

void MergeSort(int low, int high)
{
    if(low < high)
    {
        int mid = (low + high) / 2;
        MergeSort(low, mid);
        MergeSort(mid+1, high);
        Merge(low, mid, high);
    }
}

int binarySearch(int l, int h, int key)
{
    while(l <= h)
    {
        int mid = (l + h) / 2;

        if(key == N_Arr[mid])
            return 1;

        if(key < N_Arr[mid])
            h = mid -1;
        else
            l = mid + 1;
    }

    return 0;
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    std::cin >> N;

    for(int i = 0; i < N; i++)
        std::cin >> N_Arr[i];

    MergeSort(0, N-1);

    std::cin >> M;

    int x;
    for(int j = 0; j < M; j++)
    {
        std::cin >> x;
        std::cout << binarySearch(0, N-1, x) << "\n";
    }

    return 0;
}

#include <iostream>
#include <cstring>

int t;
int n; // 4 <= n <= 10,000 (even number)

bool isPrime[10001];

void get_Eratosthenes_Sieve()
{
    memset(isPrime, true, sizeof(isPrime));

    for(int i = 2; i <= n; i++)
    {
        if(isPrime[i] == true)
        {
            // i의 배수들 false로 만들기
            for(int j = i * i; j <= n; j += i)
                isPrime[j] = false;
        }
        else
            continue;
    }
}

void find_Goldbach_Partition(int solution[])
{
    int i = n / 2;
    int j = n / 2;

    while(isPrime[i] == false || isPrime[j] == false)
    {
        i--;
        j++;
    }

    solution[0] = i;
    solution[1] = j;
}

int main()
{
    scanf("%d", &t);

    while(t--)
    {
        scanf("%d", &n);

        int solution[2];

        get_Eratosthenes_Sieve();
        find_Goldbach_Partition(solution);

        printf("%d %d\n", solution[0], solution[1]);
    }

    return 0;
}

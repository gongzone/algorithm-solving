#include <cstdio>

int coinNum;
int targetValue;
int solution = 0;

int coin[10] = { 0 };

int main()
{
    scanf("%d %d", &coinNum, &targetValue);

    for(int i = 0; i < coinNum; i++)
        scanf("%d", &coin[i]);

    for(int i = coinNum - 1; i >= 0; i--)
    {
        if(targetValue == 0)
            break;

        if(coin[i] > targetValue)
            continue;

        solution += targetValue / coin[i];
        targetValue = targetValue % coin[i];
    }
    printf("%d\n", solution);

    return 0;
}

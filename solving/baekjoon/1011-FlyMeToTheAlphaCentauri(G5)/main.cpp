#include <stdio.h>

void checkCondition(int &movePoint, int &remainingDistance)
{
        bool firstCondition = false;
        bool secondCondition = false;

        firstCondition = (remainingDistance - (movePoint + 1)) >= movePoint * (movePoint + 1) / 2;
        secondCondition = (remainingDistance - movePoint) >= (movePoint - 1) * movePoint / 2;

        if(firstCondition)
        {
            movePoint++;
            remainingDistance -= movePoint;
        }
        else if(secondCondition)
        {
            remainingDistance -= movePoint;
        }
        else
        {
            movePoint--;
            remainingDistance -= movePoint;
        }
}

int main()
{
    int caseNum, x, y;

    scanf("%d", &caseNum);

    for(int i = 0; i < caseNum; i++)
    {
        scanf("%d %d", &x, &y);

        int remainingDistance = y - x;
        int movePoint = 0;
        int counting = 0;

        while(remainingDistance > 0)
        {
            checkCondition(movePoint, remainingDistance);

            counting++;
        }

        printf("%d\n", counting);
    }
    return 0;
}

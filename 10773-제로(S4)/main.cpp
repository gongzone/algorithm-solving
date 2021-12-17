#include <iostream>

int k;
int num;
int solution = 0;

int stack[100001] = {0};
int top = -1;

int push(int x)
{
    stack[++top] = x;
    return stack[top];
}

int pop()
{
    if(top == -1)
        return 0;

    return stack[top--];
}

int main()
{
    scanf("%d", &k);
    while(k--)
    {
        scanf("%d", &num);

        if(num == 0)
        {
            solution -= pop();
        }
        else
        {
            solution += push(num);;
        }
    }

    printf("%d\n", solution);

    return 0;
}

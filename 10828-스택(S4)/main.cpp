#include <iostream>
#include <cstring>
#include <string>

int n;

std::string command;
int x;

//Stack ADT
class Stack
{
private:
    int *s;
    int t;

public:
    Stack(int n)
    {
        s = new int[n];
        t = -1;

        memset(s, 0, sizeof(int)*n);
    }
    ~Stack()
    {
        delete []s;
    }

    void push(int x);
    int pop();
    int size();
    int empty();
    int top();
};

void Stack::push(int x)
{
    s[++t] = x;
}

int Stack::pop()
{
    if(t == -1)
        return -1;

    return s[t--];
}

int Stack::size()
{
    return t+1;
}

int Stack::empty()
{
    if(t == -1)
        return 1;

    return 0;
}

int Stack::top()
{
    if(t == -1)
        return -1;

    return s[t];
}

int main()
{
    scanf("%d", &n);

    Stack stack(n);

    while(n--)
    {
        char temp[5];
        scanf("%s", temp);
        command = temp;

        if(command == "push")
        {
            scanf("%d", &x);
            stack.push(x);
        }

        if(command == "pop")
        {
            int output = stack.pop();
            printf("%d\n", output);
        }

        if(command == "size")
        {
            int output = stack.size();
            printf("%d\n", output);
        }

        if(command == "empty")
        {
            int output = stack.empty();
            printf("%d\n", output);
        }

        if(command == "top")
        {
            int output = stack.top();
            printf("%d\n", output);
        }
    }

    return 0;
}

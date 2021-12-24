#include <cstdio>
#include <string>

int n;
std::string command;

class Queue
{
private:
    int *arr;
    int front;
    int rear;
    int size;

public:
    Queue(int n)
    {
        arr = new int[n+1];
        front = 0;
        rear = 0;
        size = n+1;
    }
    ~Queue()
    {
        delete []arr;
    }

    void enqueue(int x)
    {
        if((rear+1) % size == front)
            return;

        rear = (rear+1) % size;
        arr[rear] = x;
    }

    void dequeue()
    {
        if(rear == front)
        {
            printf("%d\n", -1);
            return;
        }

        front = (front+1) % size;

        printf("%d\n", arr[front]) ;
    }

    void getSize()
    {
        int queueSize;

        if(rear >= front)
            queueSize = rear - front;
        else
            queueSize = size - (front - rear);

        printf("%d\n", queueSize);
    }

    void empty()
    {
        if(rear == front)
            printf("%d\n", 1);

        else
            printf("%d\n", 0);
    }

    void getFrontValue()
    {
        if(rear == front)
            printf("%d\n", -1);
        else
            printf("%d\n", arr[(front+1) % size]);
    }

    void getRearValue()
    {
        if(rear == front)
            printf("%d\n", -1);
        else
            printf("%d\n", arr[rear]);
    }
};

int main()
{
    scanf("%d", &n);
    Queue queue(n);

    while(n--)
    {
        char temp[6];
        scanf("%s", temp);
        command = temp;

        if(command == "push")
        {
            int x;
            scanf("%d", &x);
            queue.enqueue(x);
        }

        if(command == "pop")
            queue.dequeue();

        if(command == "size")
            queue.getSize();

        if(command == "empty")
            queue.empty();

        if(command == "front")
            queue.getFrontValue();

        if(command == "back")
            queue.getRearValue();
    }

    return 0;
}

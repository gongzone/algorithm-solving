#include <iostream>

int up; // ���� �ö󰡴� �Ÿ�
int down; // �㿡 �̲������� �Ÿ�
int distance; // �ö󰡾� �� ����

int remaining = 0;
int step = 0;

int main()
{
    scanf("%d %d %d", &up, &down, &distance);

    // ������ �� up ��ŭ ���������� �̸� �����ϰ�, ���� �Ÿ��� ���� ���� �� �� �ִ��� ���
    remaining = distance - up;

    step++;
    step += remaining / (up - down);

    // �����Ÿ��� �� �������� �״�� ���, �ƴ� ��� +1
    if(remaining % (up - down) == 0)
        printf("%d", step);
    else
        printf("%d", ++step);

    return 0;
}

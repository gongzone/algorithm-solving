#include <iostream>

int up; // 낮에 올라가는 거리
int down; // 밤에 미끄러지는 거리
int distance; // 올라가야 할 높이

int remaining = 0;
int step = 0;

int main()
{
    scanf("%d %d %d", &up, &down, &distance);

    // 마지막 날 up 만큼 움직였음을 미리 가정하고, 남은 거리를 몇일 만에 갈 수 있는지 계산
    remaining = distance - up;

    step++;
    step += remaining / (up - down);

    // 남은거리가 딱 떨어지면 그대로 출력, 아닐 경우 +1
    if(remaining % (up - down) == 0)
        printf("%d", step);
    else
        printf("%d", ++step);

    return 0;
}

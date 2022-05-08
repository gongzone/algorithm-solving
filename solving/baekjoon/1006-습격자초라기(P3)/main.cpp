#include <iostream>
#include <cstring>
#include <algorithm>

/*
    1.Problem:
        -백준(1006) 습격자 초라기(P3)
        -분류: Dynamic Programming(tiling problem)
        -목표: 모든 구역을 커버하기 위해 침투 시켜야 할 특수 소대의 최소 개수

    2. Input Instances
        - t: 테스트 횟수
        - n: 한 줄에 속하는 (점령해야 할) 구역의 개수, 2n = 전체구역 개수 (1 <= n <= 10,000)
        - platoon: 특수 소대에 속하는 특수 소대원 개수 (1 <= platoon <= 10,000)
        - area[i][j]: i행과 j열 구역에 속하는 적군의 개수 (1<= 각 구역에 속하는 적군의 개수 <= platoon)

    3. Condition
        - 한 특수소대는 침투한 구역 외에, 인접한 한 구역 더 침투할 수 있다. 즉, 한 특수소대는 한 개 혹은 두 개의 구역을 커버할 수 있다.
        - 특수소대끼리는 아군인지 적인지 구분을 못 하기 때문에, 각 구역은 하나의 소대로만 커버해야 한다.
        - 한 특수소대가 커버하는 구역의 적들의 합은 특수소대원 수보다 작거나 같아야 한다.

        * 환형 구조임을 고려해야 한다.
          1) 마지막 열의 위,아래 모두 첫 열과 함께 점령하지 않을 때
          2) 마지막 열의 위 부분만 첫 열과 함께 점령할 때
          3) 마지막 열의 아래 부분만 첫 열과 함께 점령할 때
          4) 마지막 열의 위,아래 모두 첫 열과 함께 점령할 떄

          위 케이스들로부터 도출된 값들 중 가장 작은 값이 우리가 구하고자 하는 solution이다.

    4.Framework for DP Problems:
        1) Define the objective function
            - f(i,k)은 i열에서 k 상태가 되기 위한 최소의 경우의 수를 말한다.
            * k 상태: 0이면 해당 열이 꽉찬 상태
                     1이면 해당 열의 상단 부분만 찬 상태
                     2이면 해당 열의 하단 부분만 찬 상태
                     3이면 해당 열의 어떤 부분도 차지 않은 상태

        2) Identify base cases
            - dp[0][0] = area[0][0] + area[1][0] <= platoon ? 1 : 2;
            - dp[0][1] = 1;
            - dp[0][2] = 1;
            - dp[0][3] = 0;

        3) Recurrence relation for the optimized objective function
            - Case 1: dp[i][0]
                first = dp[i-1][0] + a;
                second = dp[i-1][2] + (b + 1);
                third = dp[i-1][1] + (c + 1);
                fourth = dp[i-1][3] + (b + c);

                dp[i][0] = min({first, second, third, fourth});

            - Case 2: dp[i][1]
                first = dp[i-1][0] + 1;
                second = dp[i-1][2] + b;

                dp[i][1] = min(first, second);

            - Case 3: dp[i][2]
                first = dp[i-1][0] + 1;
                second = dp[i-1][1] + c;

                dp[i][2] = min(first, second);

            - Case 4: dp[i][3]
                dp[i][3] = dp[i-1][0];

        4) What`s the order of execution?
            -bottom-up approach

        5) Where to look for the answer?
            - min(dp[n-1][0], dp[n-1][1], dp[n-1][2], dp[n-1][3])
            - caution: dp[n-1][0]을 제외한 나머지 dp배열은 환형을 고려한 결과이다. 따라서 올바른 값을 도출하기 위해서는 사전에 특수한 환경을 만들어 줘야한다.
              즉, 첫 열의 해당 요소(함께 점령되는)에 무한 수를 할당해 dp를 구할 때 다른 요소들과 묶이지 않도록 조치해야 한다.
*/

int t;
int n,platoon;
int infinity = 999999;

int area[2][10000];
int dp[10000][4];

void init()
{
    scanf("%d %d", &n,&platoon);

    memset(area, 0, sizeof(area));
    memset(dp, 0, sizeof(dp));

    for(int i = 0; i < 2; i++)
    {
        for(int j = 0; j < n; j++)
            scanf("%d", &area[i][j]);
    }
}

int getDp(int CaseNum)
{
    int first;
    int second;
    int third;
    int fourth;

    // Base Cases
    dp[0][0] = area[0][0] + area[1][0] <= platoon ? 1 : 2;
    dp[0][1] = 1;
    dp[0][2] = 1;
    dp[0][3] = 0;

    for(int i = 1; i < n; i++)
    {
        int a = area[0][i] + area[1][i] <= platoon ? 1 : 2; // i열의 두 요소가 함께 점령 될 수 있는가?
        int b = area[0][i] + area[0][i-1] <= platoon ? 1 : 2; // i열과 i-1열의 상단 부분이 함께 정렬 될 수 있는가?
        int c = area[1][i] + area[1][i-1] <= platoon ? 1 : 2;  // i열과 i-1열의 하단 부분이 함계 점령 될 수 있는가?

        // Case 1: dp[i][0]
        first = dp[i-1][0] + a;
        second = dp[i-1][2] + (b + 1);
        third = dp[i-1][1] + (c + 1);
        fourth = dp[i-1][3] + (b + c);

        dp[i][0] = std::min({first, second, third, fourth});

        // Case 2: dp[i][1]
        first = dp[i-1][0] + 1;
        second = dp[i-1][2] + b;

        dp[i][1] = std::min(first, second);

        // Case 3: dp[i][2]
        first = dp[i-1][0] + 1;
        second = dp[i-1][1] + c;

        dp[i][2] = std::min(first, second);

        // Case 4: dp[i][3]
        dp[i][3] = dp[i-1][0];
    }

    if(n == 1)
        return dp[0][0];

    if(CaseNum == 2)
        return dp[n-1][2];
    else if(CaseNum == 3)
        return dp[n-1][1];
    else if(CaseNum == 4)
        return dp[n-1][3];
    else
        return dp[n-1][0];
}

void calculate_min_platoonNum(int &Case1, int &Case2, int &Case3, int &Case4)
{
    int tempUp = area[0][0];
    int tempDown = area[1][0];

    Case1 = getDp(1);

    if(area[0][0] + area[0][n-1] <= platoon)
    {
        area[0][0] = infinity;

        Case2 = getDp(2);

        area[0][0] = tempUp;
    }

    if(area[1][0] + area[1][n-1] <= platoon)
    {
        area[1][0] = infinity;

        Case3 = getDp(3);

        area[1][0] = tempDown;
    }

    if(area[0][0] + area[0][n-1] <= platoon && area[1][0] + area[1][n-1] <= platoon)
    {
        area[0][0] = infinity;
        area[1][0] = infinity;

        Case4 = getDp(4);

        area[0][0] = tempUp;
        area[1][0] = tempDown;
    }
}

int main()
{
    scanf("%d", &t);

    while(t--)
    {
        init();

        // xx: 같이 점령 하지 않음을 나타냄, oo: 같이 점령 함을 나타냄

        int Case1 = infinity; // Case1: n-1번째 열의 상단 구역 xx 0번째 열의 상단 구역 && n-1번째 열의 하단 구역 xx 0번째 열의 하단 구역
        int Case2 = infinity; // Case2: n-1번째 열의 상단 구역 oo 0번째 열의 상단 구역
        int Case3 = infinity; // Case3: n-1번째 열의 하단 구역 oo 0번째 열의 하단 구역
        int Case4 = infinity; // Case4: n-1번째 열의 상단 구역 oo 0번째 열의 상단 구역 && n-1번째 열의 하단 구역 oo 0번째 열의 하단 구역

        calculate_min_platoonNum(Case1, Case2, Case3, Case4);

        int solution = std::min({Case1, Case2, Case3, Case4});

        printf("%d\n", solution);
    }

    return 0;
}

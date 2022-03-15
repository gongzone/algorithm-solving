#include <iostream>
#include <cstring>
#include <algorithm>

/*
    1.Problem:
        -����(1006) ������ �ʶ��(P3)
        -�з�: Dynamic Programming(tiling problem)
        -��ǥ: ��� ������ Ŀ���ϱ� ���� ħ�� ���Ѿ� �� Ư�� �Ҵ��� �ּ� ����

    2. Input Instances
        - t: �׽�Ʈ Ƚ��
        - n: �� �ٿ� ���ϴ� (�����ؾ� ��) ������ ����, 2n = ��ü���� ���� (1 <= n <= 10,000)
        - platoon: Ư�� �Ҵ뿡 ���ϴ� Ư�� �Ҵ�� ���� (1 <= platoon <= 10,000)
        - area[i][j]: i��� j�� ������ ���ϴ� ������ ���� (1<= �� ������ ���ϴ� ������ ���� <= platoon)

    3. Condition
        - �� Ư���Ҵ�� ħ���� ���� �ܿ�, ������ �� ���� �� ħ���� �� �ִ�. ��, �� Ư���Ҵ�� �� �� Ȥ�� �� ���� ������ Ŀ���� �� �ִ�.
        - Ư���Ҵ볢���� �Ʊ����� ������ ������ �� �ϱ� ������, �� ������ �ϳ��� �Ҵ�θ� Ŀ���ؾ� �Ѵ�.
        - �� Ư���Ҵ밡 Ŀ���ϴ� ������ ������ ���� Ư���Ҵ�� ������ �۰ų� ���ƾ� �Ѵ�.

        * ȯ�� �������� ����ؾ� �Ѵ�.
          1) ������ ���� ��,�Ʒ� ��� ù ���� �Բ� �������� ���� ��
          2) ������ ���� �� �κи� ù ���� �Բ� ������ ��
          3) ������ ���� �Ʒ� �κи� ù ���� �Բ� ������ ��
          4) ������ ���� ��,�Ʒ� ��� ù ���� �Բ� ������ ��

          �� ���̽���κ��� ����� ���� �� ���� ���� ���� �츮�� ���ϰ��� �ϴ� solution�̴�.

    4.Framework for DP Problems:
        1) Define the objective function
            - f(i,k)�� i������ k ���°� �Ǳ� ���� �ּ��� ����� ���� ���Ѵ�.
            * k ����: 0�̸� �ش� ���� ���� ����
                     1�̸� �ش� ���� ��� �κи� �� ����
                     2�̸� �ش� ���� �ϴ� �κи� �� ����
                     3�̸� �ش� ���� � �κе� ���� ���� ����

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
            - caution: dp[n-1][0]�� ������ ������ dp�迭�� ȯ���� ����� ����̴�. ���� �ùٸ� ���� �����ϱ� ���ؼ��� ������ Ư���� ȯ���� ����� ����Ѵ�.
              ��, ù ���� �ش� ���(�Բ� ���ɵǴ�)�� ���� ���� �Ҵ��� dp�� ���� �� �ٸ� ��ҵ�� ������ �ʵ��� ��ġ�ؾ� �Ѵ�.
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
        int a = area[0][i] + area[1][i] <= platoon ? 1 : 2; // i���� �� ��Ұ� �Բ� ���� �� �� �ִ°�?
        int b = area[0][i] + area[0][i-1] <= platoon ? 1 : 2; // i���� i-1���� ��� �κ��� �Բ� ���� �� �� �ִ°�?
        int c = area[1][i] + area[1][i-1] <= platoon ? 1 : 2;  // i���� i-1���� �ϴ� �κ��� �԰� ���� �� �� �ִ°�?

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

        // xx: ���� ���� ���� ������ ��Ÿ��, oo: ���� ���� ���� ��Ÿ��

        int Case1 = infinity; // Case1: n-1��° ���� ��� ���� xx 0��° ���� ��� ���� && n-1��° ���� �ϴ� ���� xx 0��° ���� �ϴ� ����
        int Case2 = infinity; // Case2: n-1��° ���� ��� ���� oo 0��° ���� ��� ����
        int Case3 = infinity; // Case3: n-1��° ���� �ϴ� ���� oo 0��° ���� �ϴ� ����
        int Case4 = infinity; // Case4: n-1��° ���� ��� ���� oo 0��° ���� ��� ���� && n-1��° ���� �ϴ� ���� oo 0��° ���� �ϴ� ����

        calculate_min_platoonNum(Case1, Case2, Case3, Case4);

        int solution = std::min({Case1, Case2, Case3, Case4});

        printf("%d\n", solution);
    }

    return 0;
}

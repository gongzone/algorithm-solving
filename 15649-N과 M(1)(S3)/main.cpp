#include <cstdio>
#include <vector>

int n;
int m;

std::vector<int> nums;
std::vector<int> solution;

void permute(std::vector<int> &nums)
{
    if(static_cast<int>(solution.size()) == m)
    {
        for(int i = 0; i < static_cast<int>(solution.size()); i++)
            printf("%d ", solution[i]);
        printf("\n");

        return;
    }

    for(int i = 0; i < static_cast<int>(nums.size()); i++)
    {
        solution.push_back(nums[i]);

        std::vector<int> newNums(nums);
        newNums.erase(newNums.begin() + i);

        permute(newNums);

        solution.pop_back();
    }
}

int main()
{
    scanf("%d %d", &n, &m);

    for(int i = 0; i < n; i++)
        nums.push_back(i+1);

    permute(nums);

    return 0;
}

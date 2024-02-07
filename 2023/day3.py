dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

def explore_all_nums(inp, visited, n, m, i, j):
    if i not in range(n) or j not in range(m) or inp[i][j] == '.' or visited[i][j]:
        return ""
    
    visited[i][j] = True

    if not inp[i][j].isdigit():
        nums = []
        for k in range(len(dx)):
            new_i, new_j = i + dx[k], j + dy[k]
            num = explore_all_nums(inp, visited, n, m, new_i, new_j)
            if num.isdigit():
                nums.append(int(num))
        return str(sum(nums))

    curr_num = explore_all_nums(inp, visited, n, m, i, j - 1) + inp[i][j] + explore_all_nums(inp, visited, n, m, i, j + 1)
    return curr_num

def part1():
    inp = [line.strip() for line in open("day3.txt", "r").readlines()]
    n, m = len(inp), len(inp[0])

    visited = [[False] * m for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if inp[i][j] != '.' and not inp[i][j].isdigit():
                num = explore_all_nums(inp, visited, n, m, i, j)
                if num.isdigit():
                    ans += int(num)
    
    print(ans)

def explore_all_ratios(inp, visited, n, m, i, j):
    if i not in range(n) or j not in range(m) or inp[i][j] == '.' or visited[i][j]:
        return ""
    
    visited[i][j] = True

    if not inp[i][j].isdigit():
        nums = []
        for k in range(len(dx)):
            new_i, new_j = i + dx[k], j + dy[k]
            num = explore_all_ratios(inp, visited, n, m, new_i, new_j)
            if num.isdigit():
                nums.append(int(num))
        
        if inp[i][j] == '*' and len(nums) == 2:
            return str(nums[0] * nums[1])

        return ""

    curr_num = explore_all_ratios(inp, visited, n, m, i, j - 1) + inp[i][j] + explore_all_ratios(inp, visited, n, m, i, j + 1)
    return curr_num

def part2():
    inp = [line.strip() for line in open("day3.txt", "r").readlines()]
    n, m = len(inp), len(inp[0])

    visited = [[False] * m for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if inp[i][j] == '*':
                num = explore_all_ratios(inp, visited, n, m, i, j)
                if num.isdigit():
                    ans += int(num)
    
    print(ans)

if __name__ == "__main__":
    part2()

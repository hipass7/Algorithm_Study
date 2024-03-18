def cal_diff(team1, team2):
    sum1 = 0
    sum2 = 0

    for i in range(len(team1)):
        for j in range(len(team1)):
            sum1 += table[team1[i]][team1[j]]
            sum2 += table[team2[i]][team2[j]]

    return abs(sum1 - sum2)

def make_team(team1, cnt, n, start):
    global ans

    if cnt == n // 2:
        team2 = []
        for i in range(n):
            if i not in team1:
                team2.append(i)

        diff = cal_diff(team1, team2)
        ans = min(ans, diff)
        return

    for i in range(start, n):
        if i not in team1:
            team1.append(i)
            make_team(team1, cnt + 1, n, i + 1)
            team1.remove(i)

if __name__=="__main__":
    n = int(input())
    table = [list(map(int, input().split())) for _ in range(n)]

    ans = int(1e9)
    make_team([], 0, n, 0)

    print(ans)
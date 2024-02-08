def part1():
    ans = 0
    for card in open("day4.txt", "r").readlines():
        win_set, have_set = [set(s.split()) for s in card.strip().split(':')[-1].split('|')]
        match_set = win_set.intersection(have_set)
        ans += 2**(len(match_set) - 1) if len(match_set) > 0 else 0    
    print(ans)

def part2():
    ans = 0
    i = 0
    copies = {}
    for card in open("day4.txt", "r").readlines():
        i += 1

        if i not in copies:
            copies[i] = 0
        copies[i] += 1
 
        win_set, have_set = [set(s.split()) for s in card.strip().split(':')[-1].split('|')]
        match_set = win_set.intersection(have_set)
        for j in range(i + 1, i + 1 + len(match_set)):
            if j not in copies:
                copies[j] = 0
            copies[j] += copies[i]

        # print(i, copies[i], match_set, len(match_set))
        ans += copies[i]

    print(ans)

if __name__ == "__main__":
    part2()

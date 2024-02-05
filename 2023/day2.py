def part1():
    max_rgb = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    game_num = 0
    ans = 0
    for raw_game in open('day2.txt', 'r').readlines():
        game_num += 1
        is_possible = True
        
        draw_sets = raw_game[raw_game.index(":") + 2:-1].split("; ")
        for draw_set in draw_sets:
            draws = [draw.split() for draw in draw_set.split(", ")]
            rgb = {draw[1]: int(draw[0]) for draw in draws}
            for (key, value) in rgb.items():
                if max_rgb[key] < value:
                    is_possible = False
                    break
            if not is_possible:
                break
        
        if is_possible:
            ans += game_num
    
    print(ans)

def part2():
    ans = 0
    for raw_game in open('day2.txt', 'r').readlines():
        min_rgb = {
            "red": 0,
            "green": 0,
            "blue": 0
        }

        draw_sets = raw_game[raw_game.index(":") + 2:-1].split("; ")
        for draw_set in draw_sets:
            draws = [draw.split() for draw in draw_set.split(", ")]
            rgb = {draw[1]: int(draw[0]) for draw in draws}
            for (key, value) in rgb.items():
                min_rgb[key] = max(min_rgb[key], value)

        ans += min_rgb["red"] * min_rgb["green"] * min_rgb["blue"]
    
    print(ans)

if __name__ == '__main__':
    part2()

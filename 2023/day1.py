import re

def part1():
    ans = 0
    for line in open('day1.txt', 'r').readlines():
        num = 0
        for c in line:
            if c.isdigit():
                num = int(c) * 10
                break
            
        for c in line[::-1]:
            if c.isdigit():
                num += int(c)
                break
        ans += num
    
    print(ans)

def part2():
    value_map = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    
    ans = 0
    for line in open('day1.txt', 'r').readlines():
        first_digit = 0
        last_digit = 0
        first_digit_pos = len(line)
        last_digit_pos = -1
        for (char, val) in value_map.items():
            for m in re.finditer(char, line):
                pos = m.start()
                if pos < first_digit_pos:
                    first_digit_pos = pos
                    first_digit = val
                if pos > last_digit_pos:
                    last_digit_pos = pos
                    last_digit = val
        
        ans += first_digit * 10 + last_digit
    
    print(ans)

if __name__ == '__main__':
    part2()

N = int(input())
answer = set(('A', 'B', 'C', 'D', 'E','F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'))
fail = [
    set(),
    set(('I', 'K')),
    set(('B', 'D', 'J', 'K')),
    set(('B', 'D', 'J', 'K')),
    set(('D', 'I', 'J', 'K')),
    set(('B', 'D', 'I', 'J', 'K')),
    set(('B', 'D', 'I', 'J', 'K')),
    set(('B', 'D', 'I', 'J', 'K')),
    set(('B', 'D', 'I', 'J', 'K')),
    set(('B', 'D', 'I', 'J', 'K')),
    set(('D', 'E', 'I', 'J', 'K')),
]

print(len(answer)-len(fail[N]))
print(*sorted(list(answer-fail[N])))

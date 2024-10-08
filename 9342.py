T = int(input())
for tc in range(T):
    string = list(input())
    check = {'A', 'B', 'C', 'D', 'E', 'F'}
    if string[0] in check:
        if string[0] == 'A':
            if string[1] == 'A':
                string.pop(0)
        else:
            string.pop(0)
    if string[0] == 'A':
        while string and string[0] == 'A':
            string.pop(0)
        if string[0] == 'F':
            while string and string[0] == 'F':
                string.pop(0)
            if string[0] == 'C':
                while string and string[0] == 'C':
                    string.pop(0)
                if (len(string) == 1 and string[0] in check) or not string:
                    print('Infected!')
                else:
                    print('Good')
            else:
                print('Good')
        else:
            print('Good')
    else:
        print('Good')

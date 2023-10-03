import sys, heapq
# sys.stdin = open('input.txt')
N, P = map(int, input().split())
string1 = []
string2 = []
string3 = []
string4 = []
string5 = []
string6 = []
cnt = 0
for _ in range(N):
    string, fret = map(int, input().split())
    if string == 1:
        # 기타줄을 잡고있는 손가락이 없다면 그냥 잡으면 되는데
        if not string2:
            heapq.heappush(string1, -fret)
            cnt += 1
        # 기존에 잡고있던 프렛이 있고, 새로잡을 프렛보다 높다면 기존의 프렛을 떼어내고 새로 잡을 프렛을 잡아야함
        else:
            # 만약 잡고있는 스트링이 있을때 가장 높은 플렛이 새로 잡을 높은 프랫보다 높다면, 최소한 같을때 까지 잡던 프렛 떼어내기
            while string1 and fret < -string1[0]:
                heapq.heappop(string1)
                cnt += 1
            # 만약 잡고있는 스트링이 있을때 새로 잡을 프랫과 가장 높은 프렛과 같다면 아무일도 일어나지 않음
            if string1 and fret == -string1[0]:
                continue
            # 아무튼 뗄 손가락 다 떼어냈다면 이제 새 프랫 잡기
            heapq.heappush(string1, -fret)
            cnt += 1
    if string == 2:
        # 기타줄을 잡고있는 손가락이 없다면 그냥 잡으면 되는데
        if not string2:
            heapq.heappush(string2, -fret)
            cnt += 1
        # 기존에 잡고있던 프렛이 있고, 새로잡을 프렛보다 높다면 기존의 프렛을 떼어내고 새로 잡을 프렛을 잡아야함
        else:
            # 만약 잡고있는 스트링이 있을때 가장 높은 플렛이 새로 잡을 높은 프랫보다 높다면, 최소한 같을때 까지 잡던 프렛 떼어내기
            while string2 and fret < -string2[0]:
                heapq.heappop(string2)
                cnt += 1
            # 만약 잡고있는 스트링이 있을때 새로 잡을 프랫과 가장 높은 프렛과 같다면 아무일도 일어나지 않음
            if string2 and fret == -string2[0]:
                continue
            # 아무튼 뗄 손가락 다 떼어냈다면 이제 새 프랫 잡기
            heapq.heappush(string2, -fret)
            cnt += 1
    if string == 3:
        # 기타줄을 잡고있는 손가락이 없다면 그냥 잡으면 되는데
        if not string3:
            heapq.heappush(string3, -fret)
            cnt += 1
        # 기존에 잡고있던 프렛이 있고, 새로잡을 프렛보다 높다면 기존의 프렛을 떼어내고 새로 잡을 프렛을 잡아야함
        else:
            # 만약 잡고있는 스트링이 있을때 가장 높은 플렛이 새로 잡을 높은 프랫보다 높다면, 최소한 같을때 까지 잡던 프렛 떼어내기
            while string3 and fret < -string3[0]:
                heapq.heappop(string3)
                cnt += 1
            # 만약 잡고있는 스트링이 있을때 새로 잡을 프랫과 가장 높은 프렛과 같다면 아무일도 일어나지 않음
            if string3 and fret == -string3[0]:
                continue
            # 아무튼 뗄 손가락 다 떼어냈다면 이제 새 프랫 잡기
            heapq.heappush(string3, -fret)
            cnt += 1
    if string == 4:
        # 기타줄을 잡고있는 손가락이 없다면 그냥 잡으면 되는데
        if not string4:
            heapq.heappush(string4, -fret)
            cnt += 1
        # 기존에 잡고있던 프렛이 있고, 새로잡을 프렛보다 높다면 기존의 프렛을 떼어내고 새로 잡을 프렛을 잡아야함
        else:
            # 만약 잡고있는 스트링이 있을때 가장 높은 플렛이 새로 잡을 높은 프랫보다 높다면, 최소한 같을때 까지 잡던 프렛 떼어내기
            while string4 and fret < -string4[0]:
                heapq.heappop(string4)
                cnt += 1
            # 만약 잡고있는 스트링이 있을때 새로 잡을 프랫과 가장 높은 프렛과 같다면 아무일도 일어나지 않음
            if string4 and fret == -string4[0]:
                continue
            # 아무튼 뗄 손가락 다 떼어냈다면 이제 새 프랫 잡기
            heapq.heappush(string4, -fret)
            cnt += 1
    if string == 5:
        # 기타줄을 잡고있는 손가락이 없다면 그냥 잡으면 되는데
        if not string5:
            heapq.heappush(string5, -fret)
            cnt += 1
        # 기존에 잡고있던 프렛이 있고, 새로잡을 프렛보다 높다면 기존의 프렛을 떼어내고 새로 잡을 프렛을 잡아야함
        else:
            # 만약 잡고있는 스트링이 있을때 가장 높은 플렛이 새로 잡을 높은 프랫보다 높다면, 최소한 같을때 까지 잡던 프렛 떼어내기
            while string5 and fret < -string5[0]:
                heapq.heappop(string5)
                cnt += 1
            # 만약 잡고있는 스트링이 있을때 새로 잡을 프랫과 가장 높은 프렛과 같다면 아무일도 일어나지 않음
            if string5 and fret == -string5[0]:
                continue
            # 아무튼 뗄 손가락 다 떼어냈다면 이제 새 프랫 잡기
            heapq.heappush(string5, -fret)
            cnt += 1
    if string == 6:
        # 기타줄을 잡고있는 손가락이 없다면 그냥 잡으면 되는데
        if not string6:
            heapq.heappush(string6, -fret)
            cnt += 1
        # 기존에 잡고있던 프렛이 있고, 새로잡을 프렛보다 높다면 기존의 프렛을 떼어내고 새로 잡을 프렛을 잡아야함
        else:
            # 만약 잡고있는 스트링이 있을때 가장 높은 플렛이 새로 잡을 높은 프랫보다 높다면, 최소한 같을때 까지 잡던 프렛 떼어내기
            while string6 and fret < -string6[0]:
                heapq.heappop(string6)
                cnt += 1
            # 만약 잡고있는 스트링이 있을때 새로 잡을 프랫과 가장 높은 프렛과 같다면 아무일도 일어나지 않음
            if string6 and fret == -string6[0]:
                continue
            # 아무튼 뗄 손가락 다 떼어냈다면 이제 새 프랫 잡기
            heapq.heappush(string6, -fret)
            cnt += 1
print(cnt)
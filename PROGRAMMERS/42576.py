from collections import defaultdict
def solution(participant, completion):
    participant_ = defaultdict(int)
    completion_ = defaultdict(int)
    total = set()
    for ele in participant:
        participant_[ele] += 1
        total.add(ele)
    for ele in completion:
        completion_[ele] += 1
        total.add(ele)
    for ele in total:
        if participant_[ele] != completion_[ele]:
            return ele

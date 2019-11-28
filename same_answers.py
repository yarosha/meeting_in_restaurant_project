import spreadsheets

people_to_people = {}
counter = 0
same = []


def compare(answers1, answers2):
    ans = []
    for i in range(len(answers1)):
        if answers1[i] == answers2[i]:
            ans.append(i)
    return ans
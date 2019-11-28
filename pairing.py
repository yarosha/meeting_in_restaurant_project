from spreadsheets import people_answers


def partly_people_data(people_want, people):
    new_people = {}
    for i in people_want:
        new_people[i] = people[i]
    return new_people


def pair(people_concidents):
    mx = 0
    person1 = ""
    person2 = ""
    for key1 in people_concidents.keys():
        for key2 in people_concidents[key1].keys():
            if people_concidents[key1][key2] > mx:
                mx = people_concidents[key1][key2]
                person1 = key1
                person2 = key2
    return person1, person2


def compare(answers1, answers2):
    cnt = 0
    for i in range(len(answers1)):
        if answers1[i] == answers2[i]:
            cnt += 1
    return cnt


def concidents(people_want, people_answers):
    people_to_people = {}
    for person in people_want:
        people_to_people[person] = {}
        for person2 in people_want:
            if person2 != person:
                people_to_people[person][person2] = compare(people_answers[person], people_answers[person2])
    return people_to_people


def people_by_days(days):
    a = {'monday': [], 'tuesday': [], 'wednesday': [], 'thursday': [], 'friday': [], 'saturday': []}
    for keys in days:
        if days[keys] == '1':
            a['monday'].append(keys)
        if days[keys] == '2':
            a['tuesday'].append(keys)
        if days[keys] == '3':
            a['wednesday'].append(keys)
        if days[keys] == '4':
            a['thursday'].append(keys)
        if days[keys] == '5':
            a['friday'].append(keys)
        if days[keys] == '6':
            a['saturday'].append(keys)
    return a


def people_in_day(people_want, people):
    people = partly_people_data(people_want, people)
    people_concidents = concidents(people_want, people)
    ans_pairs = []
    for i in range(int(len(people_want) / 2)):
        person1, person2 = pair(people_concidents)
        for key in people_want:
            people_concidents[person1][key] = -1
            people_concidents[person2][key] = -1
            people_concidents[key][person1] = -1
            people_concidents[key][person2] = -1
        ans_pairs.append([person1, person2])
    return ans_pairs


def parsing():
    days = {}
    f = open('days.txt', 'r')
    lines = f.readlines()
    for line in lines:
        d = line.split(' ')
        d[1] = d[1].replace('\n', '')
        days[d[0]] = d[1]
    return days


def students():
    days = parsing()
    a = people_by_days(days)
    people = people_answers()
    answer_in_days = {}
    for i in a.keys():
        answer_in_days[i] = people_in_day(a[i], people)
    import datetime
    day_of_week = datetime.datetime.today().weekday()
    keys1 = answer_in_days.keys()
    keys1 = list(keys1)
    return answer_in_days[keys1[day_of_week]]

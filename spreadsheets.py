import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint


def people_answers():
    scope = ['https://spreadsheets.google.com/feeds/', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('Parsing google sheets-a6c37d67e14a.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('Answers').sheet1
    people = {}
    for i in range(2, 1000000000000000000):
        p = sheet.row_values(i)
        if len(p) == 0:
            break
        person_answers = ""
        for j in p:
            if j == "Да":
                person_answers += '1'
            if j == "Нет":
                person_answers += '0'
        people[p[2]] = person_answers
    return people


def text_of_question():
    scope = ['https://spreadsheets.google.com/feeds/', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('Parsing google sheets-a6c37d67e14a.json', scope)
    client = gspread.authorize(creds)

    sheet = client.open('Answers').sheet1
    return sheet.row_values(1)


import vk_api
import library_messages
import pairing
import schedule
import time


def meeting():
    print("meeting")
    pairs = pairing.students()
    cnt = 1
    for i in pairs:
        library_messages.sit_message(i[0], cnt, i[1])
        library_messages.sit_message(i[1], cnt, i[0])
        cnt += 1


def run_bot(time_str):
    vk = vk_api.VkApi(token='cb6145a957442835528d14699d5601685ccd389d585ab3f55786b6ec56d0600436670449ef71f0fc70f59')
    vk._auth_token()
    schedule.every().day.at(time_str).do(meeting)
    while True:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        print(messages["count"])
        if messages["count"] >= 1:
            user_id = messages["items"][0]["last_message"]["from_id"]
            text = messages["items"][0]["last_message"]["text"]
            print(text, user_id)
            if text == "Начать":
                library_messages.first_message(user_id)
            elif text == "Пройти опрос":
                library_messages.quize_message(user_id)
            elif text == 'Хочу выпить кофе':
                library_messages.days_message(user_id)
            elif text == 'Что тут вообще происходит?':
                library_messages.help_message(user_id)
            elif text =='Понедельник':
                library_messages.meeting_message(user_id, 0)
            elif text =='Вторник':
                library_messages.meeting_message(user_id, 1)
            elif text =='Среда':
                library_messages.meeting_message(user_id, 2)
            elif text =='Четверг':
                library_messages.meeting_message(user_id, 3)
            elif text =='Пятница':
                library_messages.meeting_message(user_id, 4)
            elif text =='Суббота':
                library_messages.meeting_message(user_id, 5)
            else:
                library_messages.error_message(user_id)
        schedule.run_pending()
        time.sleep(1)
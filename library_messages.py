import keyboards
import random as r
import vk_api
import same_answers
import spreadsheets

vk = vk_api.VkApi(token='cb6145a957442835528d14699d5601685ccd389d585ab3f55786b6ec56d0600436670449ef71f0fc70f59')
vk._auth_token()


def sit_message(user_id, table_number, partner_id):
    print(user_id)
    string = ''
    for index in same_answers.compare(spreadsheets.people_answers()[user_id], spreadsheets.people_answers()[partner_id]):
        print(index, "index", type(index))
        string += str(spreadsheets.text_of_question()[3 + index])
        string += '  '
    text = "Привет. Номер твоего стола " + str(table_number) + ". Твой собеседник " + "https://vk.com/id" + str(partner_id) + ". " + "У вас совпали ответы на такие вопросы: " + string
    vk.method("messages.send", {"peer_id": user_id,
                                "message": text,
                                "random_id": int(r.uniform(0, 2 ** 32)),
                                "keyboard": keyboards.main_keyboard()})


def first_message(user_id):
    text = "Привет. Чтобы пользоваться нашим ботом, нужно пройти небольшой опрос."
    vk.method("messages.send", {"peer_id": user_id,
                                "message": text,
                                "random_id": int(r.uniform(0, 2 ** 32)),
                                "keyboard": keyboards.quize_keyboard()})


def error_message(user_id):
    text = "Ты написал что-то не то. Вернись к предыдущему шагу, пожалуйста"
    vk.method("messages.send", {"peer_id": user_id,
                                "message": text,
                                "random_id": int(r.uniform(0, 2 ** 32)),
                                "keyboard": keyboards.main_keyboard()})


def help_message(user_id):
    text = """Бот кофеек был придуман для приятного времяпрепровождени.
    Он распределяет людей за обедом по столам по интересам.
    Пройди опрос(если ты его еще не проходил)
    и мы подберем тебе собеседника, если ты захочешь встетиться.
    Функцию \' Хочу выпить кофе \' нужно вызывать именно в тот день, когда ты хочешь встретиться."""
    vk.method("messages.send", {"peer_id": user_id,
                                "message": text,
                                "random_id": int(r.uniform(0, 2 ** 32)),
                                "keyboard": keyboards.help_keyboard()})


def days_message(user_id):
    text = "Выбери день недели в который тебе хотелось бы встретиться"
    vk.method("messages.send", {"peer_id": user_id,
                                "message": text,
                                "random_id": int(r.uniform(0, 2 ** 32)),
                                "keyboard": keyboards.days_of_week_keyboard()})


def quize_message(user_id):
    text = "Пройди, пожалуйста, опрос. Чтобы мы имели понятие о твоих интересах https://forms.gle/JHAZeEMjcrcNaUjY8"
    vk.method("messages.send", {"peer_id": user_id,
                                "message": text,
                                "random_id": int(r.uniform(0, 2 ** 32)),
                                "keyboard": keyboards.main_keyboard()})


def meeting_message(user_id, day_of_week):
    text = "Хорошо. Скоро мы найдём тебе пару."

    with open("days.txt", 'a') as f:
        f.write(str(user_id) + ' ' + str(day_of_week + 1) + "\n")
    vk.method("messages.send", {"peer_id": user_id,
                                "message": text,
                                "random_id": int(r.uniform(0, 2 ** 32)),
                                "keyboard": keyboards.main_keyboard()})

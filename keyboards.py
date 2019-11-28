from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api


vk = vk_api.VkApi(token='cb6145a957442835528d14699d5601685ccd389d585ab3f55786b6ec56d0600436670449ef71f0fc70f59')
vk._auth_token()


def main_keyboard():
    keyboard = VkKeyboard(one_time=True)
    keyboard.add_button('Хочу выпить кофе', color=VkKeyboardColor.PRIMARY)
    # keyboard.add_button('Хочу фильм', color=VkKeyboardColor.NEGATIVE)
    # keyboard.add_button('Хочу книгу', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Что тут вообще происходит?', color=VkKeyboardColor.NEGATIVE)
    keyboard = keyboard.get_keyboard()
    return keyboard


def quize_keyboard():
    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button('Пройти опрос', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Что тут вообще происходит?', color=VkKeyboardColor.NEGATIVE)
    keyboard = keyboard.get_keyboard()
    return keyboard


def help_keyboard():
    keyboard = VkKeyboard(one_time=True)
    keyboard.add_button('Хочу выпить кофе', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Пройти опрос', color=VkKeyboardColor.POSITIVE)
    keyboard = keyboard.get_keyboard()
    return keyboard


def days_of_week_keyboard():
    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button('Понедельник', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_button('Вторник', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Среда', color=VkKeyboardColor.POSITIVE)
    keyboard.add_button('Четверг', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button('Пятница', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_button('Суббота', color=VkKeyboardColor.POSITIVE)
    keyboard = keyboard.get_keyboard()
    return keyboard

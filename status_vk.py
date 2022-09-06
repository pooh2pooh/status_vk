import datetime
from time import sleep
import vk

def get_status(current_status, vk_api, id):
    profiles = vk_api.users.get(user_id=id, fields='online, last_seen', v=5.92)
    if (not current_status) and (profiles[0]['online']):  # если появился в сети, то выводим время
        now = datetime.datetime.now()
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Появился в сети в: ', now.strftime("%d-%m-%Y %H:%M"))
        return True
    if (current_status) and (not profiles[0]['online']):  # если был онлайн, но уже вышел, то выводим время выхода
        print('Вышел из сети: ', datetime.datetime.fromtimestamp(profiles[0]['last_seen']['time']).strftime('%d-%m-%Y %H:%M'))
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        return False
    return current_status

if __name__ == '__main__':
    id = input("ID пользователя: ")
    token = "" # токен авторизации
    vk_api = vk.API(access_token=token)
    current_status = False
    while(True):
        current_status = get_status(current_status, vk_api, id)
        sleep(60)

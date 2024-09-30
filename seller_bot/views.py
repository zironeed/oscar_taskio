from oscarbot.response import TGResponse
from oscarbot.menu import Button, Menu


def start(user):
    """
    Реакция на /start
    Файлы с локалхоста отправить нельзя
    """
    menu = Menu(
        [Button("Желаю", callback='/buy/')]
    )
    try:
        name = user.name
    except Exception:
        name = user.username

    response = TGResponse(
        message=f'Здравствуйте, {name}!\nНе желаете приобрести подарок?',
        menu=menu,
        # photo=r'gifts.png',
        file=r'https://api.slingacademy.com/v1/sample-data/files/just-text.pdf'
    )
    return response


def try_to_buy(user):
    """
    Если юзер желает купить подарок
    """
    return TGResponse(
        message='В таком случае, давайте я запишу вас на консультацию. Вместе мы сможем выбрать лучший подарок!\n'
                'Введите дату в формате dd.mm.yyyy',
    )

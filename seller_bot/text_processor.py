import re
from .models import Appointment
from oscarbot.response import TGResponse


def handler(user, text):
    """
    Обработчик текста. Ищем дату в формате dd.mm.yyyy
    """
    if re.match(r'^\d{2}.\d{2}.\d{4}$', text['text']):
        date = re.split(r'[.\-]', text['text'])
        try:
            appointment = Appointment.objects.create(user=user, date=''.join(date[::-1]))
            appointment.save()
            message = f'Заявка на консультацю принята.\nЖдем вас {date[0]}.{date[1]}!'
        except Exception:
            message = 'Вы уже записаны на консультацию в этот день'
    else:
        message = 'Я не знаю такой команды'

    return TGResponse(
        message=message,
    )

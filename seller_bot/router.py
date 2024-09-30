from .views import start, try_to_buy
from oscarbot.router import route

routes = [
    route('/start', start),
    route('/buy/', try_to_buy),
]

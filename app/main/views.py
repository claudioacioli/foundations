from . import main


@main.route('/')
def show_restaurants():
    return 'Hello World'

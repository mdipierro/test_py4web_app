

from py4web import action

@action('/')
def index():
    return "Hello world"

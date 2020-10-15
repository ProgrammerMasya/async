from .views import calculations


def setup_routes(app):
    app.router.add_route('POST', '/sum', calculations.test_sum)

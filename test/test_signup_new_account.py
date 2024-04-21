from datahelpers.stringhelper import get_random_string
from enums.letter import Letter

'''
def test_signup_new_account(app):
    username = "user_" + get_random_string(7, Letter.eng)
    email = username + "@localhost"
    password = "password"
    app.james.ensure_user_exists(username, password)
    app.signup.new_user(username, email, password)
    app.session.login(username, password)
    assert app.session.is_logged_in_as(username)
    app.session.logout()
'''


def test_signup_new_account(app):
    username = "user_" + get_random_string(7, Letter.eng)
    email = username + "@localhost"
    password = "password"
    app.james.ensure_user_exists(username, password)
    app.signup.new_user(username, email, password)
    app.soap.can_login(username, password)

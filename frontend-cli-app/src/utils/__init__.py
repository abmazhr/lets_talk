from typing import List


class MenuItems:
    from src.handlers.chatting import chatting_handler
    from src.handlers.login import login_handler
    from src.handlers.logout import logout_handler
    from src.handlers.register import register_handler

    REGISTER_NEW_USER = ('Register a new user.', register_handler)
    LOGIN_WITH_EXISTED_USER = ('Login with an existed user.', login_handler)
    LOGOUT_CURRENT_LOGGED_USER = ('Logout.', logout_handler)
    CHAT = ('Start chatting.', chatting_handler)
    EXIT = ('Exit the app.', lambda: exit(0))


def get_cli_menu(menu_items: List[str]) -> str:
    menu_str = """
###############################################################################
#                             REAL-TIME CHAT CLIENT                           #
###############################################################################
"""
    for index, item_str in enumerate(menu_items):
        menu_str += f'{index + 1}) {item_str}\n'

    return menu_str


db = {}

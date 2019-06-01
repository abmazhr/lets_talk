import os
import sys
from typing import List, Callable, Tuple

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


def main(*, menu_items_containers: List[Tuple[str, Callable]]) -> None:
    from src.utils import get_cli_menu
    from src.loop import loop

    menu_items_str = list(map(lambda tup: tup[0], menu_items_containers))
    menu_items_handlers = list(map(lambda tup: tup[1], menu_items_containers))

    print(get_cli_menu(menu_items=menu_items_str))
    loop(current_menu_handlers=menu_items_handlers)


if __name__ == '__main__':
    from src.utils import MenuItems

    current_menu_items_containers = [
        MenuItems.REGISTER_NEW_USER,
        MenuItems.LOGIN_WITH_EXISTED_USER,
        MenuItems.EXIT
    ]

    try:
        main(menu_items_containers=current_menu_items_containers)
    except KeyboardInterrupt:
        print('⇝ Exiting ...')

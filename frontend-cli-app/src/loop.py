from typing import List, Callable


def loop(*, current_menu_handlers: List[Callable]) -> None:
    from src.utils import get_cli_menu

    invalid_choice_msg = 'Error, please choose a valid choice.'
    try:
        choice = int(input("⇝ "))
        if choice > len(current_menu_handlers) or choice < 1:
            print(invalid_choice_msg)
            loop(current_menu_handlers=current_menu_handlers)
        else:
            new_menu_containers: List[Callable] = current_menu_handlers[choice - 1]()
            new_menu_items_str = list(map(lambda tup: tup[0], new_menu_containers))
            new_menu_items_handlers = list(map(lambda tup: tup[1], new_menu_containers))
            print(get_cli_menu(menu_items=new_menu_items_str))
            loop(current_menu_handlers=new_menu_items_handlers)
    except ValueError:
        print(invalid_choice_msg)
        loop(current_menu_handlers=current_menu_handlers)

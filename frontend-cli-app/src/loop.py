from typing import List, Callable


def loop(*, current_menu_handlers: List[Callable]) -> None:
    invalid_choice_msg = 'Error, please choose a valid choice.'
    try:
        choice = int(input("⇝ "))
        if choice > len(current_menu_handlers) or choice < 1:
            print(invalid_choice_msg)
            loop(current_menu_handlers=current_menu_handlers)
        else:
            current_menu_handlers[choice - 1]()
            loop(current_menu_handlers=current_menu_handlers)
    except ValueError:
        print(invalid_choice_msg)
        loop(current_menu_handlers=current_menu_handlers)

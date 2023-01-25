import view
import model

def start():
    user_choise = 0

    while user_choise != 8:
        user_choise = view.main_menu()

        match user_choise:
            case 1:
                phone_book = model.get_phone_book()
                view.show_contacts(phone_book)
            case 2:
                model.open_phone_book()
                view.load_success()
            case 3:
                model.save_phone_book()
                view.save_success()
            case 4:
                new = list(view.new_contact())
                model.update_phone_book(new)
                view.partically_save_sucess()

            case 5:
                search = view.find_contact()
                result = model.search_contact(search)
                view.show_contacts(result)
                changed = list(view.change_contact(result))
                model.changing_contact(changed)
                view.partically_save_sucess()
                pass

            case 6:
                search = view.find_contact()
                result = model.search_contact(search)
                view.show_contacts(result)
                key_to_delete = view.delete_contact()
                model.deleting_contact(key_to_delete)
                view.partically_save_sucess
                pass
            case 7:
                search = view.find_contact()
                result = model.search_contact(search)
                view.show_contacts(result)

    
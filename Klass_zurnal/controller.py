
import view
import model

def start():
    # user_input = ''
    klass = view.main_menu()
    
    model.open_journal(klass) 
    journal = model.get_journal() 
    view.print_dict(journal)
    while True:
        predmets = model.get_predmets()
        predmet = view.choose_lesson(predmets)  
        if predmet == 'exit' or predmet == 'учше':
            user_choise = view.save_and_exit()
            if user_choise == 'exit' or user_choise == 'учше':
                model.save_journal()
                break
            if user_choise == 'n' or user_choise == 'т':
                break
            
        else:
            journal = model.get_journal()     
            view.print_dict_lesson(journal,predmet) 
            
            uchenik = ''
            while True:
                pupils = model.get_pupils()
                uchenik = view.choose_student(pupils)
                if uchenik == 'exit' or uchenik == 'учше':
                    break
                    

                else:
                    ocenka = view.assessment()
                    model.provesti_urok(predmet,uchenik,ocenka)
                    journal = model.get_journal()
                    view.print_dict_lesson(journal,predmet)
                
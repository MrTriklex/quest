
class Character:
    def action(self, x, posx, posy, maps):
        ...


class CharacterStefan(Character):
    def action(self, x, posx, posy, maps):
        ...


    def talk(self):
        print("Стефан: ТЫ ЧТО ТУТ ДЕЛАЕШЬ?!!!")
        print("1. сказать: я я я")
        print("2. начать убегать")
        print("3. сказать: а ты что тут делаешь")
        print("4. сказать: всё, всё ухожу")

        while True:
            to_do = input()
            if to_do == "1":
                print("Стэфан: ну всё сейчас будет серьёзный разговор!!!")
                break
            elif to_do == "2":
                print("Стэфан: ну всё сейчас будет серьёзный разговор!!!")
                break
            elif to_do == "3":
                print("Стэфан: ну всё сейчас будет серьёзный разговор!!!")
                break
            elif to_do == "4":
                print("Стэфан: БЫСТРО В КОМНАТУ")
                # vent = EventEndEscape()
                break

        return to_do


class CharacterSVH(Character):
    ...
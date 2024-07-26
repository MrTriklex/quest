from events import EventEnd, EventEndEscape , EventEndLost, Mapmove
from chars import Character, CharacterSVH, CharacterStefan

map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 0, 1]]






posx = 5
posy = 5
place = 1
placeflag = 0
placeflag2 = 0
moveinty = 0
moveintx = 0
event = 0
eventflag = 0
print("Ночной Диолог")
name = input("введите имя диологовца: ")
age = int(input("введите возраст диологовца: "))


def move(posx, posy, place):
    do = input()
    moveintx = 0
    moveinty = 0
    if do == "w" and map[posx - 1][posy] == 0:
        map[posx][posy] = 0
        moveintx -= 1
    elif do == "w" and map[posx - 1][posy] == 2:
        if place == 1:
            place = 2
        elif place == 2:
            place = 1
        elif place == 3:
            place = 4
    elif do == "w" and map[posx - 1][posy] == 3:
        if place == 2:
            place = 3





    if do == "s" and map[posx + 1][posy] == 0:
        map[posx][posy] = 0
        moveintx += 1
    elif do == "s" and map[posx + 1][posy] == 2:
        if place == 1:
            place = 2
        elif place == 2:
            place = 1
        elif place == 3:
            place = 4
    elif do == "s" and map[posx + 1][posy] == 3:
        if place == 2:
            place = 3



    if do == "d" and map[posx][posy + 1] == 0:
        map[posx][posy] = 0
        moveinty += 1
    elif do == "d" and map[posx][posy + 1] == 2:
        if place == 1:
            place = 2
        elif place == 2:
            place = 1
        elif place == 3:
            place = 4
    elif do == "d" and map[posx ][posy + 1] == 3:
        if place == 2:
            place = 3



    if do == "a" and map[posx][posy - 1] == 0:
        map[posx][posy] = 0
        moveinty -= 1
    elif do == "a" and map[posx][posy - 1] == 2:
        if place == 1:
            place = 2
        elif place == 2:
            place = 1
        elif place == 3:
            place = 4
    elif do == "a" and map[posx][posy - 1] == 3:
        if place == 2:
            place = 3





    return moveinty, moveintx, place


while True:
    if event == 0:
        if placeflag2 == 1:
            map, posx, posy, placeflag2 = Mapmove.setmap(place)






        map[posx][posy] = 999
        if place == 1 or place == 2 or place == 3 or place == 4:
            for x in range(9):
                for y in range(9):
                    if map[x][y] == CharacterStefan:
                        if posx < x:
                            map[x - 1][y] = CharacterStefan
                            if x - 1 == posx and y == posy:
                                event = EventEndLost()
                            if eventflag == 0:
                                to_do = CharacterStefan().talk()
                                eventflag = 1
                        elif posx > x:
                            map[x + 1][y] = CharacterStefan
                            if x + 1 == posx and y == posy:
                                event = EventEndLost()
                            if eventflag == 0:
                                to_do = CharacterStefan().talk()
                                eventflag = 1
                        elif posy < y:
                            map[x][y - 1] = CharacterStefan
                            if x == posx and y -1 == posy:
                                event = EventEndLost()
                            if eventflag == 0:
                                to_do = CharacterStefan().talk()
                                eventflag = 1
                        elif posy > y:
                            map[x][y + 1] = CharacterStefan
                            if x == posx and y+1 == posy:
                                event = EventEndLost()
                            if eventflag == 0:
                                to_do = CharacterStefan().talk()
                                eventflag = 1
                        map[x][y] = 0
                        if to_do == "4":
                            event = EventEndEscape()
                    elif map[x][y] == CharacterSVH:
                        if posx > x - 1 and posx < x + 1 and posy > y - 1 and posx < y + 1:
                            event = 2





            for x in range(10):
                for y in range(10):
                    if map[x][y] == 1:
                        print("#", end=' ')
                    elif map[x][y] == 2:
                        print("[]", end='')
                    elif map[x][y] == 3:
                        print("[]", end='')
                    elif map[x][y] == CharacterStefan:
                        print("😈", end=' ')
                    elif map[x][y] == CharacterSVH:
                        print("⁂", end=' ')
                    elif map[x][y] == 999:
                        print("д", end=' ')
                    else:
                        print(" ", end=' ')
                print()

        placeflag = place
        moveinty, moveintx, place = move(posx, posy, place)
        posx += moveintx
        posy += moveinty
        moveinty = 0
        moveintx = 0
        if placeflag != place:
            placeflag2 = 1


        if age > 18:
            print("ты не попал в диолог")
            break
    elif event == 2:
        print("Стефан: ТЫ ЧТО ТУТ ДЕЛАЕШЬ?!!!")
        print("1. сказать: я я я")
        print("2. начать убегать")
        print("3. сказать: а ты что тут делаешь")
        print("4. сказать: всё, всё ухожу")

    elif isinstance(event, EventEnd):
        event.message()
        break



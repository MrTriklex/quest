from maps import *




class Mapmove:
    def setmap(place):
        if place == 1:
            map = map2
            placeflag2 = 0
            posx = 7
            posy = 8
        elif place == 2:
            map = map3
            placeflag2 = 0
            posx = 2
            posy = 3
        elif place == 3:
            map = map4
            placeflag2 = 0
            posx = 2
            posy = 3
        elif place == 4:
            map = map5
            placeflag2 = 0
            posx = 7
            posy = 7
        return map , posx, posy, placeflag2



class Event:
    def message(self):
        ...


class EventEnd(Event):
    ...









class EventEndLost(EventEnd):
    def message(self):
        print("Концовка 1: ваш диологовец пропал без вести")


class EventEndEscape(EventEnd):
    def message(self):
        print("Концовка 2: ваш диологовец убежал в комнату и спокойно провёл смену в диологе")
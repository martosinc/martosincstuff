from tkinter import *
import random
root = Tk()
root.title('Змейка')
running = True
seg_size = 20
root.geometry('500x500')

c = Canvas(root, width=500, height=500, bg='#00FF7F')
c.grid()
c.focus_set()

class Segment(object):
    def __init__(self, x, y):
        self.instance = c.create_rectangle(x,y, x+seg_size, y+seg_size, fill='#4682B4')
class Snake(object):
    def __init__(self,segments):
        self.segments = segments
        self.mapping = {"Down": (0, 1), "Right": (1, 0),
                "Up": (0, -1), "Left": (-1, 0)}
        self.vector = self.mapping['Down']

    # def move(self):
    #     for index in range(len(self.segments)-1):
    #         segment = self.segments[index].instance
    #         x1,y1,x2,y2 = c.coords(self.segments[index+1].instance)
    #         c.coords(segments,x1,y1,x2,y2)
    #     x1,y1,x2,y2 = c.coords(self.segments[-2].instance)
    #     # c.coords(self.segments[-1].instance, x1+self.vector[0]*seg_size, y1+self.vector[1]*seg_size, x2+self.vector[0]*seg_size, y2+self.vector[1]*seg_size)
    #     c.coords(self.segments[-1].instance,
    #             x1 + self.vector[0] * seg_size, y1 + self.vector[1] * seg_size,
    #             x2 + self.vector[0] * seg_size, y2 + self.vector[1] * seg_size)
    def move(self):
        # перебираем все сегменты кроме первого
        for index in range(len(self.segments) - 1):
            segment = self.segments[index].instance
            x1, y1, x2, y2 = c.coords(self.segments[index + 1].instance)
        # задаем каждому сегменту позицию сегмента стоящего после него
            c.coords(segment, x1, y1, x2, y2)

        # получаем координаты сегмента перед "головой"
        x1, y1, x2, y2 = c.coords(self.segments[-2].instance)
        # получаем координаты сегмента перед "головой"
        c.coords(self.segments[-1].instance,
                 x1 + self.vector[0] * seg_size, y1 + self.vector[1] * seg_size,
                 x2 + self.vector[0] * seg_size, y2 + self.vector[1] * seg_size)
    def change_direction(self, event):
        if event.keysym in self.mapping:
            self.vector = self.mapping[event.keysym]
    def add_segment(self):
        last_seg = c.coords(self.segments[0].instance)
        x = last_seg[2] - seg_size
        y = last_seg[3] - seg_size
        self.segments.insert(0, Segment(x,y))
def create_block():
    global block
    posx = seg_size * (random.randint(1, (500-seg_size) / seg_size))
    posy = seg_size * (random.randint(1, (500-seg_size) / seg_size))
    block = c.create_oval(posx, posy,posx + seg_size,posy + seg_size,fill="red")
def main():
    global running
    if running:
        s.move()
        head_coords = c.coords(s.segments[-1].instance)
        x1,y1,x2,y2 = head_coords
        if x1 < 0 or x2 > 480 or y1 < 0 or y2 > 480:
            running = False
        elif head_coords == c.coords(block):
            s.add_segment()
            c.delete(block)
            create_block()
        else:
            for index in range(len(s.segments)-1):
                if c.coords(s.segments[index].instance) == head_coords:
                    running = False
        root.after(200,main)

segments = [Segment(seg_size, seg_size),Segment(seg_size*2, seg_size),Segment(seg_size*3, seg_size)]

s = Snake(segments)
create_block()
main()
c.bind("<KeyPress>", s.change_direction)
root.mainloop()
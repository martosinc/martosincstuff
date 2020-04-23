from tkinter import *
import math
t=Tk()
t.geometry('950x600')
t.resizable(0,0)

c = Canvas(height=500,width=500)
c.grid(row=0,column=0,rowspan=8)

class People():
    def __init__(self):
        self.length = 100
        self.x1 = 250
        self.y1 = 150
        self.x2 = 250
        self.y2 = 250
        self.anim_count=0
        self.create()
        self.head_move()
        self.body_move()        
    def create(self):
        self.head = c.create_oval(0,0,0,0)
        self.body = c.create_line(0,0,0,0)
        self.leftlokot = c.create_line(0,0,0,0)
        self.leftarm = c.create_line(0,0,0,0)
        self.rightlokot = c.create_line(0,0,0,0)
        self.rightarm = c.create_line(0,0,0,0)
        self.leftleg = c.create_line(0,0,0,0)
        self.leftleg2 = c.create_line(0,0,0,0)
        self.rightleg = c.create_line(0,0,0,0)
        self.rightleg2 = c.create_line(0,0,0,0)
    def move(self,event):
        self.x1 = posx.get()
        self.x2 = posx.get()
        self.y1 = posy.get()
        self.y2 = posy.get()+self.length
        self.head_move()
        self.body_move()
        self.draw_left_lokot()
        self.draw_left_arm()
        self.draw_right_lokot()
        self.draw_right_arm()
        self.draw_left_leg()
        self.draw_left_leg2()
        self.draw_right_leg()
        self.draw_right_leg2()

    def head_move(self):
        c.coords(self.head,self.x1-25,self.y1-50,self.x1+25,self.y1)
    def body_move(self):
        c.coords(self.body,self.x1,self.y1,self.x2,self.y2)

    def x_coordinate(self, start_X, length, angle):
        return start_X + length * math.cos((angle-90) * math.pi / 180)

    def y_coordinate(self, start_Y, length, angle):
        return start_Y + length * math.sin((angle-90) * math.pi / 180)
    
    def set_0(self):
        s1.set(-180)
        s2.set(-180)
        s3.set(180)
        s4.set(180)
        s5.set(180)
        s6.set(-180)
        s7.set(-180)
        s8.set(-180)
        posx.set(250)
        posy.set(150)
    def draw_left_lokot(self):
        angle = s5.get()
        self.x_left_lokot = self.x_coordinate(self.x1, self.length-50, angle)
        self.y_left_lokot = self.y_coordinate(self.y1, self.length-50, angle)
        c.coords(self.leftlokot,self.x1,self.y1, self.x_left_lokot, self.y_left_lokot)

    def draw_left_arm(self):
        angle = s6.get()
        self.x_left_arm = self.x_coordinate(self.x_left_lokot, self.length-50, angle)
        self.y_left_arm = self.y_coordinate(self.y_left_lokot, self.length-50, angle)
        c.coords(self.leftarm,self.x_left_lokot, self.y_left_lokot, self.x_left_arm, self.y_left_arm)

    def draw_right_lokot(self):
        angle = s7.get()
        self.x_right_lokot = self.x_coordinate(self.x1, self.length-50, angle)
        self.y_right_lokot = self.y_coordinate(self.y1, self.length-50, angle)
        c.coords(self.rightlokot,self.x1,self.y1, self.x_right_lokot, self.y_right_lokot)

    def draw_right_arm(self):
        angle = s8.get()
        self.x_right_arm = self.x_coordinate(self.x_right_lokot, self.length-50, angle)
        self.y_right_arm = self.y_coordinate(self.y_right_lokot, self.length-50, angle)
        c.coords(self.rightarm,self.x_right_lokot, self.y_right_lokot, self.x_right_arm, self.y_right_arm)

    def draw_left_leg(self):
        angle = s1.get()
        self.x_left_leg = self.x_coordinate(self.x2, self.length-33, angle)
        self.y_left_leg = self.y_coordinate(self.y2, self.length-33, angle)
        c.coords(self.leftleg,self.x2,self.y2, self.x_left_leg, self.y_left_leg)

    def draw_left_leg2(self):
        angle = s2.get()
        self.x_left_leg2 = self.x_coordinate(self.x_left_leg, self.length-33, angle)
        self.y_left_leg2 = self.y_coordinate(self.y_left_leg, self.length-33, angle)
        c.coords(self.leftleg2,self.x_left_leg, self.y_left_leg, self.x_left_leg2, self.y_left_leg2)

    def draw_right_leg(self):
        angle = s3.get()
        self.x_right_leg = self.x_coordinate(self.x2, self.length-33, angle)
        self.y_right_leg = self.y_coordinate(self.y2, self.length-33, angle)
        c.coords(self.rightleg,self.x2,self.y2, self.x_right_leg, self.y_right_leg)

    def draw_right_leg2(self):
        angle = s4.get()
        self.x_right_leg2 = self.x_coordinate(self.x_right_leg, self.length-33, angle)
        self.y_right_leg2 = self.y_coordinate(self.y_right_leg, self.length-33, angle)
        c.coords(self.rightleg2,self.x_right_leg, self.y_right_leg, self.x_right_leg2, self.y_right_leg2)

    # def animat(self):
        self.anim_count += 1
        if self.anim_count <=20:
            s7.set(s7.get()+1)
            s8.set(s8.get()+3.75)
            s5.set(s5.get()-1.75)
            s6.set(s6.get()+1.25)
            s3.set(s3.get()+3.25)
            s4.set(s4.get()-1.25)
            s1.set(s5.get()-1.75)
            s2.set(s2.get()-4.25)
            self.move()
        elif self.anim_count <=40:
            s7.set(s7.get()-1)
            s8.set(s8.get()-3.75)
            s5.set(s5.get()+1.75)
            s6.set(s6.get()-1.25)
            s3.set(s3.get()-3.25)
            s4.set(s4.get()+1.25)
            s1.set(s5.get()+1.75)
            s2.set(s2.get()+4.25)
            self.move()
        else:
            self.anim_count = 0
            return
        c.after(50,self.animat)


man = People()
animate=Button(text='ANIMATE',command=man.anim_count)
animate.grid(row=2,column=3,columnspan=5)
s1 = Scale(t,orient=HORIZONTAL,length=200,from_=-180,to=-45,tickinterval=20,resolution=5,label='Left Up Leg',command=man.move)
s1.grid(row=0,column=1)
s1.set(-180)
s2 = Scale(t,orient=HORIZONTAL,length=200,from_=-180,to=-45,tickinterval=20,resolution=5,label='Left Down Leg',command=man.move)
s2.grid(row=1,column=1)
s2.set(-180)
s3 = Scale(t,orient=HORIZONTAL,length=200,from_=180,to=45,tickinterval=20,resolution=5,label='Right Up Leg',command=man.move)
s3.grid(row=2,column=1)
s3.set(180)
s4 = Scale(t,orient=HORIZONTAL,length=200,from_=180,to=45,tickinterval=20,resolution=5,label='Right Down Leg',command=man.move)
s4.grid(row=3,column=1)
s4.set(180)
s5 = Scale(t,orient=HORIZONTAL,length=200,from_=20,to=180,tickinterval=20,resolution=5,label='Left Up Arm',command=man.move)
s5.grid(row=4,column=1)
s5.set(180)
s6 = Scale(t,orient=HORIZONTAL,length=200,from_=-180,to=180,tickinterval=20,resolution=5,label='Left Down Arm',command=man.move)
s6.grid(row=5,column=1)
s6.set(-180)
s7 = Scale(t,orient=HORIZONTAL,length=200,from_=-180,to=-20,tickinterval=20,resolution=5,label='Right Up Arm',command=man.move)
s7.grid(row=6,column=1)
s7.set(-180)
s8 = Scale(t,orient=HORIZONTAL,length=200,from_=180,to=-180,tickinterval=60,resolution=5,label='Right Down Arm',command=man.move)
s8.grid(row=7,column=1)
s8.set(-180)
posx = Scale(t,orient=HORIZONTAL,length=200,from_=0,to=500,tickinterval=100,resolution=5,label='Pos X',command=man.move)
posx.grid(row=0,column=2)
posx.set(250)
posy = Scale(t,orient=VERTICAL,length=200,from_=0,to=500,tickinterval=100,resolution=5,label='Pos Y',command=man.move)
posy.grid(row=1,column=2,rowspan=3)
posy.set(150)
t.mainloop()
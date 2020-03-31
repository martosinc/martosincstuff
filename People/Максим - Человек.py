from tkinter import *
import math
t = Tk()
t.geometry('600x800')
t.title('Человек')
c = Canvas(t,height=600, width=380)
##################
c.pack(anchor="w")
##################
captrurebtn=Button(text="CAPTURE")
animatebtn=Button(text="ANIMATE")
def x_coordinate(start_X,length,angle):
    return start_X + length * math.cos((angle-90)*math.pi / 180)
def y_coordinate(start_Y,length,angle):
    return start_Y + length * math.sin((angle-90)*math.pi / 180)
class Person():
    def __init__(self):
        self.y1 = 0
        self.y2 = 50
        self.x1 = 0
        self.x2 = 0
        self.length = 0
        self.leftarm1deg = 0
        self.rightarm1deg = 0
        self.leftarm2deg = 0
        self.rightarm2deg = 0
        self.leftleg1deg = 0
        self.rightleg1deg = 0
        self.leftleg2deg = 0
        self.rightleg2deg = 0
        self.x_start_body = 200
        self.x_end_body = 200
        self.y_start_body = 200
        self.y_end_body = 400
        self.create()
        self.draw_all()
    def create(self):
        self.head=c.create_oval(self.x_start_body-50, self.y_start_body-100, self.x_start_body+50, self.y_start_body, width=10)
        self.body=c.create_line(self.x_start_body,self.y_start_body,self.x_end_body,self.y_end_body,width=10)
        self.left_lokot=c.create_line(0,0,0,0,width=10)
        self.left_arm=c.create_line(0,0,0,0,width=10)
        self.rightarm1=c.create_line(0,0,0,0)
        self.rightarm2=c.create_line(0,0,0,0)
        self.leftleg1=c.create_line(0,0,0,0)
        self.leftleg2=c.create_line(0,0,0,0)
        self.rightleg1=c.create_line(0,0,0,0)
        self.rightleg2=c.create_oval(0,0,0,0)
    def draw_all(self):
        self.draw_head()
        self.draw_left_lokot()
    def draw_head(self):
        c.coords(self.head, self.x_start_body-50, self.y_start_body-100, self.x_start_body+50, self.y_start_body)
    def draw_left_lokot(self):
        self.x_left_lokot = x_coordinate(self.x_start_body,self.length, 45)
        self.y_left_lokot = y_coordinate(self.y_start_body,self.length, 45)
        c.coords(self.left_lokot,self.x_start_body, self.y_start_body, self.x_left_lokot,self.y_left_lokot)
    def draw_left_arm(self):
        self.x_left_arm = x_coordinate(self.x_left_lokot,self.length, 45)
        self.y_left_arm = y_coordinate(self.y_left_lokot,self.length, 45)
        c.coords(self.left_arm, self.x_left_lokot, self.y_left_lokot, self.x_left_arm, self.y_left_arm)
man = Person()
if 1==1:
    ##################
    ##################
    sclul = Scale(t,orient=HORIZONTAL,length=200,from_=-100, to=100, tickinterval=20,resolution=5,label="Left Up Leg")
    scldl = Scale(t,orient=HORIZONTAL,length=200,from_=-100, to=100, tickinterval=20,resolution=5,label="Left Down Leg")
    scrul = Scale(t,orient=HORIZONTAL,length=200,from_=-100, to=100, tickinterval=20,resolution=5,label="Right Up Leg")
    scrdl = Scale(t,orient=HORIZONTAL,length=200,from_=-100, to=100, tickinterval=20,resolution=5,label="Right Down Leg")
    sclua = Scale(t,orient=HORIZONTAL,length=200,from_=-100, to=100, tickinterval=20,resolution=5,label="Left Up Arm")
    sclda = Scale(t,orient=HORIZONTAL,length=200,from_=-100, to=100, tickinterval=20,resolution=5,label="Left Down Arm")
    scrua = Scale(t,orient=HORIZONTAL,length=200,from_=-100, to=100, tickinterval=20,resolution=5,label="Right Up Arm")
    scrda = Scale(t,orient=HORIZONTAL,length=200,from_=-100, to=100, tickinterval=20,resolution=5,label="Right Down Arm")
    scpx = Scale(t,orient=HORIZONTAL,length=200,from_=-100, to=100, tickinterval=20,resolution=5,label="Position X")
    scpy = Scale(t,orient=HORIZONTAL,length=200,from_=-100, to=100, tickinterval=20,resolution=5,label="Position Y")
    c.grid(row=0,column=0,columnspan=1, rowspan=10,pady=0.1)
    captrurebtn.grid(row=0,column=3,rowspan=1,columnspan=4,pady=0.1)
    animatebtn.grid(row=1,column=3,rowspan=1,columnspan=4,pady=0.1)   
    sclul.grid(row=2,column=3,rowspan=1,columnspan=4,pady=0.1)
    scldl.grid(row=3,column=3,rowspan=1,columnspan=4,pady=0.1)
    scrul.grid(row=4,column=3,rowspan=1,columnspan=4,pady=0.1)
    scrdl.grid(row=5,column=3,rowspan=1,columnspan=4,pady=0.1)
    sclua.grid(row=6,column=3,rowspan=1,columnspan=4,pady=0.1)
    sclda.grid(row=7,column=3,rowspan=1,columnspan=4,pady=0.1)
    scrua.grid(row=8,column=3,rowspan=1,columnspan=4,pady=0.1)
    scrda.grid(row=9,column=3,rowspan=1,columnspan=4,pady=0.1)
    scpx.grid(row=10,column=3,rowspan=1,columnspan=4,pady=0.1)
    scpy.grid(row=11,column=3,rowspan=1,columnspan=4,pady=0.1)
t.mainloop()
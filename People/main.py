from tkinter import *
t = Tk()
t.geometry('600x800')
t.title('Человек')
c = Canvas(t,height=600, width=380)
captrurebtn=Button(text="CAPTURE")
animatebtn=Button(text="ANIMATE")
class Person():
    def __init__(self):
        self.y1 = 0
        self.y2 = 50
        self.y1 = 0
        self.x2 = 0
        self.length = 50
        self.leftarm1deg = 0
        self.rightarm1deg = 0
        self.leftarm2deg = 0
        self.rightarm2deg = 0
        self.leftleg1deg = 0
        self.rightleg1deg = 0
        self.leftleg2deg = 0
        self.rightleg2deg = 0
        self.create()
        self.move()
    def create(self):
        canvas.create_oval(0,0,0,0)
        body=canvas.create_line(0,0,0,0)
        leftarm1=canvas.create_line(0,0,0,0)
        leftarm2=canvas.create_line(0,0,0,0)
        rightarm1=canvas.create_line(0,0,0,0)
        rightarm2=canvas.create_line(0,0,0,0)
        leftleg1=canvas.create_line(0,0,0,0)
        leftleg2canvas.create_line(0,0,0,0)
        rightleg1=canvas.create_line(0,0,0,0)
        rightleg2=canvas.create_line(0,0,0,0)
    def headmoving(self):
        c.coords(head,x1,y2,x1,y2)
    def bodymoving(self):
        c.coords(body,x1,y1,x2,y2)
    def x_coordinate(start_X,length,angle):
        return start_X + length * math.cos((angle-90)*math.pi / 180)
    def y_coordinate(start_Y,length,angle):
        return start_Y + length * math.sin((angle-90)*math.pi / 180)

    def draw_left_lokot(self):
        anglefunc = sclua.get()
        self.x_left_lokot = x_coordinate(self.x1,self.length, self.anglefunc)
        self.y_left_lokot = y_coordinate(self.y1,self.length, self.anglefunc)
        c.coords(self.leftarm1,self.x1, self.y1, self.x_left_lokot,self.y_left_lokot)
    def left_arm(self):
        self.leftarmx1 = self.x_left_lokot
        self.leftarmy1 = self.y_left_lokot
        anglefunc = sclda.get()
        self.leftarmx2 = x_coordinate(self.leftarmx1,25,self.anglefunc)
        self.leftarmy2 = y_coordinate(self.leftarmx1,25,self.anglefunc)
        c.coords(leftarm2,leftarmx1,leftarmy1,leftarmx2,leftarmy2)

    def draw_right_lokot(self):
        anglefunc = scrua.get()
        self.x_right_lokot = x_coordinate(self.x1,self.length, self.anglefunc)
        self.y_right_lokot = y_coordinate(self.y1,self.length, self.anglefunc)
        c.coords(self.rightarm1,self.x1, self.y1, self.x_right_lokot,self.y_right_lokot)
    def right_arm(self):
        self.rightarmx1 = self.x_right_lokot
        self.rightarmy1 = self.y_right_lokot
        anglefunc = scrda.get()
        self.rightarmx2 = x_coordinate(self.rightarmx1,25,self.anglefunc)
        self.rightarmy2 = y_coordinate(self.rightarmx1,25,self.anglefunc)
        c.coords(rightarm2,rightarmx1,rightarmy1,rightarmx2,rightarmy2)

    def draw_left_bedro(self):
        anglefunc = sclul.get()
        self.x_left_bedro = x_coordinate(self.x2,self.length, self.anglefunc)
        self.y_left_bedro = y_coordinate(self.y2,self.length, self.anglefunc)
        c.coords(self.leftleg1,self.x2, self.y2, self.x_left_bedro,self.y_left_bedro)
    def left_leg(self):
        anglefunc = scldl.get()
        self.leftlegx1 = self.x_left_bedro
        self.leftlegy1 = self.y_left_bedro
        self.leftlegx2 = x_coordinate(self.leftlegx1,25,self.anglefunc)
        self.leftlegy2 = y_coordinate(self.leftlrgx1,25,self.anglefunc)
        c.coords(leftleg2,leftlegx1,leftlegy1,leftlegx2,leftlegy2)

    def draw_left_bedro(self):
        anglefunc = sclul.get()
        self.x_left_bedro = x_coordinate(self.x2,self.length, self.anglefunc)
        self.y_left_bedro = y_coordinate(self.y2,self.length, self.anglefunc)
        c.coords(self.leftleg1,self.x2, self.y2, self.x_left_bedro,self.y_left_bedro)
    def left_leg(self):
        anglefunc = scldl.get()
        self.leftlegx1 = self.x_left_bedro
        self.leftlegy1 = self.y_left_bedro
        self.leftlegx2 = x_coordinate(self.leftlegx1,25,self.anglefunc)
        self.leftlegy2 = y_coordinate(self.leftlegx1,25,self.anglefunc)
        c.coords(leftleg2,leftlegx1,leftlegy1,leftlegx2,leftlegy2)

    def draw_right_bedro(self):
        anglefunc = scrul.get()
        self.x_right_bedro = x_coordinate(self.x2,self.length, self.anglefunc)
        self.y_right_bedro = y_coordinate(self.y2,self.length, self.anglefunc)
        c.coords(self.rightleg1,self.x2, self.y2, self.x_right_bedro,self.y_right_bedro)
    def right_leg(self):
        anglefunc = scrdl.get()
        self.rightlegx1 = self.x_right_bedro
        self.rightlegy1 = self.y_right_bedro
        self.rightlegx2 = x_coordinate(self.rightlegx1,25,self.anglefunc)
        self.rightlegy2 = y_coordinate(self.rightlegx1,25,self.anglefunc)
        c.coords(rightleg2,rightlegx1,rightlegy1,rightlegx2,rightlegy2)

    def move():
        self.draw_left_lokot()
        self.left_arm()
        self.draw_right_lokot()
        self.right_arm()
        self.draw_left_bedro()
        self.left_leg()
        self.draw_right_bedro()
        self.right_leg()

if 1==1:
    sclul = Scale(t,orient=HORIZONTAL,length=200,from_=-100, to=100, tickinterval=20,resolution=5,label="Left Up Leg")
    scldl = Scale(t,orient=HORIZONTAL,length=200,from_=-100, to=100, tickinterval=20,resolution=5,label="Left Down Leg")
    scrul = Scale(t,orient=HORIZONTAL,length=200,from_=-100, to=100, tickinterval=20,resolution=5,label="Right Up Leg")
    scrdl = Scale(t,orient=HORIZONTAL,length=200,from_=-100, to=100, tickinterval=20,resolution=5,label="Right Down Leg")
    sclua = Scale(t,orient=HORIZONTAL,length=200,from_=-100, to=100, tickinterval=20,resolution=5,label="Left Up Arm")
    sclda = Scale(t,orient=HORIZONTAL,length=200,from_=-100, to=100, tickinterval=20,resolution=5,label="Left Down Arm")
    scrua = Scale(t,orient=HORIZONTAL,length=200,from_=-100, to=100, tickinterval=20,resolution=5,label="Right Up Arm")
    scrda = Scale(t,orient=HORIZONTAL,length=200,from_=-100, to=100, tickinterval=20,resolution=5,label="Right Down Arm")
    scpx = Scale(t,orient=HORIZONTAL,length=200,from_=-100, to=100, tickinterval=20,resolution=5,label="Position X")
    scpy = Scale(t,orient=VERTICAL,length=200,from_=-100, to=100, tickinterval=20,resolution=5,label="Position Y")
    c.grid(row=0,column=0,columnspan=1, rowspan=10,pady=0.1)
    captrurebtn.grid(row=0,column=3,rowspan=1,columnspan=4,pady=0.1)
    animatebtn.grid(row=1,column=3,rowspan=1,columnspan=4,pady=0.1)   
    sclul.grid(row=2,column=3,rowspan=1,columnspan=4,pady=0.1)
    scldl.grid(row=3,column=3,rowspan=1,columnspan=4,pady=0.1)
    scrul.grid(row=4,column=3,rowspan=1,columnspan=4,pady=0.1)
    scrdl.grid(row=5,column=3,rowspan=1,columnspan=4,pady=0.1)
    sclua.grid(row=6,column=3,rowspan=1,columnspan=4,pady=0.1)
    scrua.grid(row=7,column=3,rowspan=1,columnspan=4,pady=0.1)
    scrda.grid(row=8,column=3,rowspan=1,columnspan=4,pady=0.1)
    scpx.grid(row=9,column=3,rowspan=1,columnspan=4,pady=0.1)
    scpy.grid(row=10,column=3,rowspan=1,columnspan=4,pady=0.1)
t.mainloop()
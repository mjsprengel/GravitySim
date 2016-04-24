### Matt Sprengel
### 4/23/16       
# For faster or slower computers, try altering 'dt' variable in
# the gameon() function (line 302) to better suit your computer's performance
# fast computers ---> smaller dt (1/2000.0, 1/5000.0, etc etc)
# slow computers ---> bigger dt (1/500.0, 1/250.0, etc etc)

from tkinter import *
import math

gamestate = 0 #global toggle for start/stop

def start(): #this function is bound to the "start" botton
    global gamestate
    gamestate = 1
    animation.title("Calculating...")
    canvas.delete(canvas.find_withtag("uno"))
    canvas.delete(canvas.find_withtag("dos"))
    canvas.delete(canvas.find_withtag("tres"))
    gameon() #gameon()starts the physics engine

def stop(): #this function is bound to the "stop" button
    global gamestate
    gamestate = 0
    animation.title("Left click and drag to set position, right click and drag"
                    " to set velocity. To alter mass, enter number in text box")
    car() #car() turns off the gravity and lets user reset positions

def reset(): #resets to initial conditions
    global r1,v1,a1,r2,v2,a2,r3,v3,a3,gamestate,m1,m2,m3,size1,size2,size3
    gamestate = 0
    animation.title("Left click and drag to set position, right click and drag"
                    " to set velocity. To alter mass, enter number in text box")
    r1 = [600,300]
    v1 = [0,4] 
    a1 = [0,0]
    r2 = [500,300]
    v2 = [0,0] 
    a2 = [0,0]       #semi-stable equilibrium
    r3 = [400,300]
    v3 = [0,-4]    
    a3 = [0,0] 
    size1 = 7.5*m1**(1.0/3.0)
    size2 = 7.5*m2**(1.0/3.0)
    size3 = 7.5*m3**(1.0/3.0)
    car()
def setmass1():
    global m1, size1
    m1 = float(mass1.get())
    size1 = 7.5*m1**(1.0/3.0)
    mass1.delete(0,'end')
def setmass2():
    global m2, size2
    m2 = float(mass2.get())
    size2 = 7.5*m2**(1.0/3.0)
    mass2.delete(0,'end')
def setmass3():
    global m3, size3
    m3 = float(mass3.get())
    size3 = 7.5*m3**(1.0/3.0)
    mass3.delete(0,'end')
def getmass1(event):
    global m1, size1
    m1 = float(mass1.get())
    size1 = 7.5*m1**(1.0/3.0)
    mass1.delete(0,'end')
def getmass2(event):
    global m2, size2
    m2 = float(mass2.get())
    size2 = 7.5*m2**(1.0/3.0)
    mass2.delete(0,'end')   
def getmass3(event):
    global m3, size3  
    m3 = float(mass3.get())
    size3 = 7.5*m3**(1.0/3.0)
    mass3.delete(0,'end')
    
animation = Tk() #creating the GUI canvas and buttons,widgets
animation.title("Left click and drag to set position, right click and drag"
                " to set velocity. To alter mass, enter number in text box")
frame = Frame(width = 1000, height = 50, bg = "black")
frame.pack(fill=BOTH)
start = Button(frame, text = "Start", command = start, bg ="green")
start.pack(side = LEFT,padx=5)
stop = Button(frame, text = "Stop", command = stop, bg = "green")
stop.pack(side = LEFT,padx=5)
reset = Button(frame, text = "Reset", command = reset, bg = "green")
reset.pack(side = LEFT,padx=5)
mb1 = Button(frame, text = "Set Mass", command = setmass1, bg="Blue",
             fg = "white")
mb1.pack(side = RIGHT,padx=10,pady=3)
mass1 = Entry(frame, width = 5, bg = "black", fg = "white",
              insertbackground="white",insertwidth=1)
mass1.pack(side = RIGHT,padx=5)
mb2 = Button(frame, text = "Set Mass", command = setmass2, bg="Yellow")
mb2.pack(side = RIGHT,padx=10)
mass2 = Entry(frame, width = 5, bg = "black", fg = "white",
              insertbackground="white",insertwidth=1)
mass2.pack(side = RIGHT,padx=5)
mb3 = Button(frame, text = "Set Mass", command = setmass3, bg="Red",
             fg = "white")
mb3.pack(side = RIGHT,padx=10)
mass3 = Entry(frame, width = 5, bg = "black", fg = "white",
              insertbackground="white",insertwidth=1)
mass3.pack(side = RIGHT,padx=5)
mass1.bind('<Return>', getmass1)
mass2.bind('<Return>', getmass2)
mass3.bind('<Return>', getmass3)

canvas = Canvas(animation, width=1000, height=600, bg="black")
canvas.pack()

##GLOBALS##
G = 1000.0 #gravity strength (arbitrarily chosen to suit timestep/screensize)

m1 = 1.0 #mass
r1 = [600,300] #position 
v1 = [0,4] #velocity 
a1 = [0,0] #acceleration
size1 = 7.5*m1**(1.0/3.0) #diameter of balls

m2 = 2.0
r2 = [500,300]
v2 = [0,0] 
a2 = [0,0] 
size2 = 7.5*m2**(1.0/3.0) 

m3 = 1.0
r3 = [400,300]
v3 = [0,-4]    
a3 = [0,0]
size3 = 7.5*m3**(1.0/3.0)

#center of mass of the system
rcm = [(m1*r1[0] + m2*r2[0] + m3*r3[0])/(m1+m2+m3),((m1*r1[1] + m2*r2[1] +
                                                     m3*r3[1])/(m1+m2+m3))]

def drag(event): #changes the location of the body to current mouse coordinates
    xm, ym = event.x, event.y
    rm1 = math.sqrt(((xm-r1[0])**2)+((ym-r1[1])**2))
    rm2 = math.sqrt(((xm-r2[0])**2)+((ym-r2[1])**2))
    rm3 = math.sqrt(((xm-r3[0])**2)+((ym-r3[1])**2))
    clickableRadius1, clickableRadius2, clickableRadius3 = (2*size1,2*size2,
                                                            2*size3)
    if rm1 < clickableRadius1:
        a1[0],a1[1] = 0,0
        v1[0],v1[1] = 0,0
        r1[0],r1[1] = xm,ym
        canvas.delete(canvas.find_withtag("uno"))
    if rm2 < clickableRadius2:
        a2[0],a2[1] = 0,0
        v2[0],v2[1] = 0,0
        r2[0],r2[1] = xm,ym
        canvas.delete(canvas.find_withtag("dos"))
    if rm3 < clickableRadius3:
        a3[0],a3[1] = 0,0
        v3[0],v3[1] = 0,0
        r3[0],r3[1] = xm,ym
        canvas.delete(canvas.find_withtag("tres"))
        
pressed1 = 0 #toggles for wasRightClicked handler
pressed2 = 0
pressed3 = 0
def wasRightClicked(event): #checks to see if ball was rightclicked
    global pressed1,pressed2,pressed3
    xm, ym = event.x, event.y
    rm1 = math.sqrt(((xm-r1[0])**2)+((ym-r1[1])**2)) 
    clickableRadius1 = size1/2
    if rm1 < clickableRadius1:
        pressed1 = 1 #toggles "pressed" to on, allowing for velset function
    rm2 = math.sqrt(((xm-r2[0])**2)+((ym-r2[1])**2))
    clickableRadius2 = size2/2
    if rm2 < clickableRadius2:
        pressed2 = 1
    rm3 = math.sqrt(((xm-r3[0])**2)+((ym-r3[1])**2))
    clickableRadius3 = size3/2
    if rm3 < clickableRadius3:
        pressed3 = 1
        
newvel1 = [0,0] #toggles for drag set velocity handler
newvel2 = [0,0]
newvel3 = [0,0]
def MakeVelLine(event): #this func is called upon right-click-motion. Draws.
    global pressed1,newvel1,pressed2,newvel2,pressed3,newvel3
    vxm, vym = event.x, event.y
    velscale = 10
    if pressed1 == 1:
        canvas.delete(canvas.find_withtag("uno"))
        canvas.create_line(r1[0], r1[1], vxm, vym, fill = "green", width = 1,
                           tags="uno")
        newvel1[0],newvel1[1] = (vxm-r1[0])/velscale , (vym-r1[1])/velscale
    if pressed2 == 1:
        canvas.delete(canvas.find_withtag("dos"))
        canvas.create_line(r2[0], r2[1], vxm, vym, fill = "green", width = 1,
                           tags="dos")
        newvel2[0],newvel2[1] = (vxm-r2[0])/velscale , (vym-r2[1])/velscale
    if pressed3 == 1:
        canvas.delete(canvas.find_withtag("tres"))
        canvas.create_line(r3[0], r3[1], vxm, vym, fill = "green", width = 1,
                           tags="tres")
        newvel3[0],newvel3[1] = (vxm-r3[0])/velscale , (vym-r3[1])/velscale
        
def velLineSet(event): #this function is called upon mouse release. Sets vel.
    global newvel1, newvel2,newvel3, pressed1, pressed2,pressed3
    if pressed1 == 1:
        v1[0],v1[1] = newvel1[0],newvel1[1]
        newvel1[0],newvel1[1] = 0,0
        if gamestate == 1:
            canvas.delete(canvas.find_withtag("uno"))
        pressed1 = 0
    if pressed2 == 1:
        v2[0],v2[1] = newvel2[0],newvel2[1]
        newvel2[0],newvel2[1] = 0,0
        if gamestate == 1:
            canvas.delete(canvas.find_withtag("dos"))
        pressed2 = 0
    if pressed3 == 1:
        v3[0],v3[1] = newvel3[0],newvel3[1]
        newvel3[0],newvel3[1] = 0,0
        if gamestate == 1:
            canvas.delete(canvas.find_withtag("tres"))
        pressed3 = 0

def showinfo(): #This function runs once every time step. Shows vel, position.
    if pressed2 == 1:
        str1 = "Yellow:   v = [%.2f, %.2f]\nRed:        v = [%.2f, %.2f]\nB"\
               "lue:       v = [%.2f, %.2f]"%(newvel2[0],newvel2[1],v3[0],
                                              v3[1],v1[0],v1[1])
        canvas.delete(canvas.find_withtag("velinfo"))
        canvas.create_text(75,30,text = str1, fill = "green", justify = LEFT,
                           tags = "velinfo")
    if pressed1 == 1:
        str1 = "Yellow:   v = [%.2f, %.2f]\nRed:        v = [%.2f, %.2f]\nB"\
               "lue:       v = [%.2f, %.2f]"%(v2[0],v2[1],v3[0],v3[1],
                                              newvel1[0],newvel1[1])
        canvas.delete(canvas.find_withtag("velinfo"))
        canvas.create_text(75,30,text = str1, fill = "green", justify = LEFT,
                           tags = "velinfo")
    if pressed3 == 1:
        str1 = "Yellow:   v = [%.2f, %.2f]\nRed:        v = [%.2f, %.2f]\nB"\
               "lue:       v = [%.2f, %.2f]"%(v2[0],v2[1],newvel3[0],
                                              newvel3[1],v1[0],v1[1])
        canvas.delete(canvas.find_withtag("velinfo"))
        canvas.create_text(75,30,text = str1, fill = "green", justify = LEFT,
                           tags = "velinfo")
    if pressed2 == 0 and pressed1 == 0 and pressed3 == 0:
        str2 = "Yellow:   v = [%.2f, %.2f]\nRed:        v = [%.2f, %.2f]\nB"\
               "lue:       v = [%.2f, %.2f]"%(v2[0],v2[1],v3[0],v3[1],v1[0],
                                              v1[1])
        canvas.delete(canvas.find_withtag("velinfo"))
        canvas.create_text(75,30,text = str2, fill = "green", justify = LEFT,
                           tags = "velinfo")
    str3 = "Yellow:   r = [%d, %d]\nRed:        r = [%d, %d]\nB"\
           "lue:       r = [%d, %d]" % (r2[0],r2[1],r3[0],r3[1],r1[0],r1[1])
    canvas.delete(canvas.find_withtag("posinfo"))
    canvas.create_text(70,570,text = str3, fill = "green", justify = LEFT,
                       tags = "posinfo")
    str4 = "Yellow:   Mass = %.1f\nRed:        Mass = %.1f\nB"\
           "lue:       Mass = %.1f" % (m2,m3,m1)
    canvas.delete(canvas.find_withtag("massinfo"))
    canvas.create_text(935,30, text=str4, fill = "green", justify = LEFT,
                       tags = "massinfo")
    str5 = "Euler-Cromer Method"
    canvas.delete(canvas.find_withtag("RAWR"))
    canvas.create_text(935,590, text = str5, fill = "green", tags = "RAWR")
 
canvas.bind('<B1-Motion>',drag) #Binds left click to drag()
canvas.bind('<Button-3>',wasRightClicked)
canvas.bind('<B3-Motion>',MakeVelLine)
canvas.bind('<ButtonRelease-3>',velLineSet)

def updatescreen(): #deletes old, draws new circles at current position
    canvas.delete(canvas.find_withtag("blue"))
    canvas.delete(canvas.find_withtag("yellow"))
    canvas.delete(canvas.find_withtag("red"))
    canvas.delete(canvas.find_withtag("cm"))
    canvas.create_oval(r1[0]-(size1/2),r1[1]-(size1/2),r1[0]+(size1/2),r1[1]+
                       (size1/2), outline = "blue", fill = "blue", tags="blue")
    canvas.create_oval(r2[0]-(size2/2),r2[1]-(size2/2),r2[0]+(size2/2),r2[1]+
                       (size2/2), outline = "yellow", fill = "yellow",
                       tags="yellow")
    canvas.create_oval(r3[0]-(size3/2),r3[1]-(size3/2),r3[0]+(size3/2),r3[1]+
                       (size3/2), outline = "red", fill = "red", tags="red")
    canvas.create_oval(rcm[0]-(1),rcm[1]-(1),rcm[0]+(1),rcm[1]+(1),
                       outline = "white", fill = "white", tags="cm")

updatescreen()
animation.update()

def car():
    global r1,r2,r3,size1,size2,size3,gamestate,rcm
    while gamestate == 0: #will move objects to current location
        rcm = [(m1*r1[0] + m2*r2[0] + m3*r3[0])/(m1+m2+m3),
               ((m1*r1[1] +m2*r2[1] + m3*r3[1])/(m1+m2+m3))]
        updatescreen()
        showinfo()
        animation.update()
        
def gameon(): #this function contains the physics engine. 
    global G, m1,r1,v1,a1,size1,m2,r2,v2,a2,size2,m3,r3,v3,a3,size3
    global gamestate, rcm
    dt = 1/1000.0 #timestep
    i = 0
    while gamestate == 1:
        i += 1
        ###Eueler-Cromer integration method applied to a summation of forces###
        rMag_12 = math.sqrt((r1[0]-r2[0])**2 + (r1[1]-r2[1])**2) 
        rMag_13 = math.sqrt((r1[0]-r3[0])**2 + (r1[1]-r3[1])**2)
        rMag_23 = math.sqrt((r2[0]-r3[0])**2 + (r2[1]-r3[1])**2)

        #unit vectors used to resolve acceleration into x,y components
        rHat_21 = [(r2[0]-r1[0])/rMag_12, (r2[1]-r1[1])/rMag_12] 
        rHat_12 = [(r1[0]-r2[0])/rMag_12, (r1[1]-r2[1])/rMag_12] 

        rHat_23 = [(r2[0]-r3[0])/rMag_23, (r2[1]-r3[1])/rMag_23] 
        rHat_32 = [(r3[0]-r2[0])/rMag_23, (r3[1]-r2[1])/rMag_23] 

        rHat_13 = [(r1[0]-r3[0])/rMag_13, (r1[1]-r3[1])/rMag_13] 
        rHat_31 = [(r3[0]-r1[0])/rMag_13, (r3[1]-r1[1])/rMag_13] 
        
        a21Mag = -(m1)*G/(rMag_12**2) #magnitude of the acceleration
        a12Mag = -(m2)*G/(rMag_12**2) 
        a23Mag = -(m3)*G/(rMag_23**2)  
        a32Mag = -(m2)*G/(rMag_23**2) 
        a13Mag = -(m3)*G/(rMag_13**2)
        a31Mag = -(m1)*G/(rMag_13**2)

        #each body has x,y component of acceleration due to the other 2 bodies:
        a2 = [(rHat_21[0]*a21Mag)+(rHat_23[0]*a23Mag),
              (rHat_21[1]*a21Mag)+(rHat_23[1]*a23Mag)] 
        a1 = [(rHat_12[0]*a12Mag)+(rHat_13[0]*a13Mag),
              (rHat_12[1]*a12Mag)+(rHat_13[1]*a13Mag)]
        a3 = [(rHat_31[0]*a31Mag)+(rHat_32[0]*a32Mag),
              (rHat_31[1]*a31Mag)+(rHat_32[1]*a32Mag)]
        
        #how much the velocity changes by (dv) via dv/dt = a ... (dv = a*dt)
        dv2 = [a2[0]*dt, a2[1]*dt]
        dv1 = [a1[0]*dt, a1[1]*dt]
        dv3 = [a3[0]*dt, a3[1]*dt]

        #updating the velocity of each body by adding dv
        v2 = [v2[0] + dv2[0], v2[1] + dv2[1]]
        v1 = [v1[0] + dv1[0], v1[1] + dv1[1]]
        v3 = [v3[0] + dv3[0], v3[1] + dv3[1]]

        #how much the position changes by (dr) via dr/dt = v ... (dr = v*dt)
        dr2= [v2[0]*dt, v2[1]*dt]
        dr1= [v1[0]*dt, v1[1]*dt]
        dr3= [v3[0]*dt, v3[1]*dt]

        #updating the position of each body by adding dr
        r2 = [r2[0]+dr2[0],r2[1]+dr2[1]]
        r1 = [r1[0]+dr1[0],r1[1]+dr1[1]]
        r3 = [r3[0]+dr3[0],r3[1]+dr3[1]]
        rcm = [(m1*r1[0] + m2*r2[0] + m3*r3[0])/(m1+m2+m3),
               ((m1*r1[1] + m2*r2[1] + m3*r3[1])/(m1+m2+m3))]
        if i%228 == 0: #don't need to update screen EVERY computation
            i = 0
            updatescreen()
            showinfo()
            animation.update()

car() #Starts screen update loop

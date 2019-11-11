from psychopy import event, core, visual
import random

#generate "selections" from each bag (without replacement)
def selOrder(nRed,nBlue,nSel):
    lsSel = []
    for i in range(nSel):
        rand = random.randint(1,nRed+nBlue)
        if rand in range(1,nRed):
            lsSel.append('R')
            nRed -= 1
        else:
            lsSel.append('B')
            nBlue -= 1
    return(lsSel)

#70 red, 30 blue
sel1 = selOrder(70,30,20)
#30 red, 70 blue
sel2 = selOrder(30,70,20)



#generate experiment window (expWin)
expWin = visual.Window(size=(800,800),winType = 'pyglet', units='pix')


#function for drawing rectangles in a stack
def drawRects(xRec, yRec, nRec, color, width, height, nWide):
    rect = visual.Rect(win=expWin, units = 'pix')
    j = 1
    for i in range(nRec):
        rect.width = width
        rect.height = height
        rect.fillColor = color
        rect.pos = (xRec,yRec)

        if j%nWide == 0 and i !=0:
            yRec += height
            xRec -= width*(nWide-1)
        else:
            xRec += width
            
        j += 1
        rect.draw()

def drawCircs(xCir, yCir, nCir, color, radius, nWide):
    circle = visual.Circle(win=expWin, units = 'pix')
    j = 1
    for i in range(nCir):
        circle.radius = radius
        circle.fillColor = color
        circle.pos = (xCir,yCir)

        if j%nWide == 0 and i !=0:
            yCir += 2*radius
            xCir -= 2*radius*(nWide-1)
        else:
            xCir += 2*radius
            
        j += 1
        circle.draw()


#Draw the components of the main experiment windoow
class ExpMain():
    nRec1 = 50
    nRedC1 = 70; nBlueC1 = 30
    nRedC2 = 30; nBlueC2 = 70
    xRec1 = -200; yRec1 = -150
    xRec2 = 100; yRec2 = -150
    xCirR1 = -205; yCirR1 = -300
    xCirB1 = -135; yCirB1 = -300
    xCirR2 = 95; yCirR2 = -300
    xCirB2 = 125; yCirB2 = -300
    chipsDrawn = 0
    def drawExpMain():
        drawRects(ExpMain.xRec1,ExpMain.yRec1,ExpMain.nRec1,(1,-1,1),20,10,5)
        drawRects(ExpMain.xRec2,ExpMain.yRec2,100-ExpMain.nRec1,(1,-1,1),20,10,5)
        drawCircs(ExpMain.xCirR1,ExpMain.yCirR2,ExpMain.nRedC1,(1,-1,-1),5,7)
        drawCircs(ExpMain.xCirB1,ExpMain.yCirB1,ExpMain.nBlueC1,(-1,-1,1),5,3)
        drawCircs(ExpMain.xCirR2,ExpMain.yCirR2,ExpMain.nRedC2,(1,-1,-1),5,3)
        drawCircs(ExpMain.xCirB2,ExpMain.yCirB2,ExpMain.nBlueC2,(-1,-1,1),5,7)
        
        #draw the chips drawn (chosen) so far
        if ExpMain.chipsDrawn != 0:
            j = 1
            xChip1 = -200;yChip1 = 150
            for i in range(ExpMain.chipsDrawn):
                pokerChip = visual.Circle(win = expWin,units='pix')
                pokerChip.radius = 15
                pokerChip.pos = (xChip1,yChip1)
                if sel1[i-1] == 'R':
                    pokerChip.fillColor = (1,-1,-1)
                if sel1[i-1] == 'B':
                    pokerChip.fillColor = (-1,-1,1)
                if j%10 == 0 and i !=0:
                    yChip1 += 2*pokerChip.radius +10
                    xChip1 -= (2*pokerChip.radius + 10)*(9)
                else:
                    xChip1 += 2*pokerChip.radius + 10
            
                j += 1
                pokerChip.draw()

        expWin.flip()

#draws first experiment flip (default view)
ExpMain.drawExpMain()

#user input
subjectProbs = []
while ExpMain.chipsDrawn <= 20:
    keyPress = event.waitKeys(keyList=('a','z','s','x','space'))
    
    if keyPress[0] == 'space':
        subjectProbs.append(ExpMain.nRec1)
        ExpMain.chipsDrawn += 1       
    if keyPress[0] == 'a':
        ExpMain.nRec1 += 1
    if keyPress[0] == 'z':
        ExpMain.nRec1 -= 1
    if keyPress[0] == 's':
        ExpMain.nRec1 += 5
    if keyPress[0] == 'x':
        ExpMain.nRec1 -= 5
    if ExpMain.nRec1 >= 100:
        ExpMain.nRec1 = 100
    if ExpMain.nRec1 <= 0:
        ExpMain.nRec1 = 0
    if ExpMain.chipsDrawn <= 20:
        ExpMain.drawExpMain()

print(subjectProbs)
event.waitKeys(keyList = ('q', 'Esc'))

expWin.close()
core.quit()
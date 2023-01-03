import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.lines import Line2D      
from matplotlib.patches import Circle, Rectangle
import matplotlib.animation as animation
from car_run import Running_Car

def drawing(dataset):
    running_car=Running_Car()
    running_car.run(dataset)
    fig=plt.figure(figsize=(6.5,6))
    ax=fig.add_subplot(111)
    with open("軌道座標點.txt","r") as f:
        lines=f.read().splitlines()
    wallx=[]
    wally=[]
    finishx=[]
    finishy=[]
    for i in range(len(lines)):
        lines[i]=lines[i].split(',')
        if i>=3:
            wallx.append(int(lines[i][0]))
            wally.append(int(lines[i][1]))
        else:
            finishx.append(int(lines[i][0]))
            finishy.append(int(lines[i][1]))
    xtrace=[]
    ytrace=[]
    distance=running_car.distances
    for plot in running_car.plots:
        xtrace.append(plot[0])
        ytrace.append(plot[1])
    phis=running_car.phis
    wallLine = Line2D(wallx, wally)
    startLine=Line2D((wallx[0],wallx[-2]),(finishx[0],finishy[0]))
    endLine=Rectangle((finishx[1],finishy[2]),finishx[2]-finishx[1],finishy[1]-finishy[2])
    car=Circle((finishx[0],finishy[0]),3,facecolor="None",edgecolor="black")
    direction_text=ax.annotate("direction: "+str(90),(7,4))
    circle_pos=ax.annotate(str((finishx[0],finishy[0])),(finishx[0],finishy[0]))
    front_dis=ax.annotate("front distance: "+str(round(distance[0][0],3)),(20,6))
    right_dis=ax.annotate("right distance: "+str(round(distance[0][1],3)),(20,4))
    left_dis=ax.annotate("left distance: "+str(round(distance[0][2],3)),(20,2))
    ax.add_patch(car)
    ax.add_artist(endLine)
    plt.plot(*startLine.get_data())
    plt.plot(*wallLine.get_data())
    line, = ax.plot([], [])

    def Animate(i):
        line.set_data(xtrace[:i],ytrace[:i])
        car.center=(xtrace[i],ytrace[i])
        circle_pos.set_text(str((round(xtrace[i],3),round(ytrace[i],3))))
        circle_pos.set_position((xtrace[i-1],ytrace[i-1]))
        direction_text.set_text("direction:"+str(round(phis[i],3)))
        front_dis.set_text("front distance: "+str(round(distance[i][0],3)))
        right_dis.set_text("right distance: "+str(round(distance[i][1],3)))
        left_dis.set_text("left distance: "+str(round(distance[i][2],3)))
        return line

    ani = animation.FuncAnimation(fig, Animate,len(xtrace),repeat=False)
    if dataset==0:
        ani.save('train4d.gif')
    else:
        ani.save('train6d.gif')
    # clip = mp.VideoFileClip("train4d.gif")
    # clip.write_videofile("train4d.mp4")
    plt.show()
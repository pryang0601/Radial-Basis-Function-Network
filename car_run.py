import numpy as np
from RBFN6d import RBFN6d
from RBFN4d import RBFN4d
import copy
from env import Car,Wall
class Running_Car():
    def __init__(self):
        self.plots=[]
        self.phis=[]
        self.distances=[]
        self.fdis=0
        self.ldis=0
        self.rdis=0
    def run(self,dataset):
        if dataset==0:
            r=RBFN4d()
        else:
            r=RBFN6d()
        
        with open("軌道座標點.txt","r") as f:
            lines=f.read().splitlines()
        walls=[]
        for i in range(len(lines)):
            lines[i]=lines[i].split(',')
        car=Car((int(lines[0][0]),int(lines[0][1])),int(lines[0][2]),3)
        finish_area_x=[int(lines[1][0]),int(lines[2][0])]
        finish_area_y=[int(lines[2][1]),int(lines[1][1])]
        for i in range(3,len(lines)):
            lines[i][0]=int(lines[i][0])
            lines[i][1]=int(lines[i][1])
        for i in range(3,len(lines)-1):
            walls.append(Wall(lines[i],lines[i+1]))
        run=True
        tracks=[]
        while run:
            record=[]
            if finish_area_x[0]<car.pos[0]<finish_area_x[1] and finish_area_y[0]<car.pos[1]<finish_area_y[1]:
                run=False
            if car.check_wall()==True:
                run=False
            if run==False:
                break
            distance=car.sensor_dist(walls)
            self.distances.append(distance)
            self.phis.append(car.phi)
            if dataset==0:
                theta=r.output(distance)
            else:
                theta=r.output([car.pos[0],car.pos[1],distance[0],distance[1],distance[2]])
            if dataset==1:
                record.append(car.pos[0])
                record.append(car.pos[1])
            for dis in distance:
                record.append(dis)
            record.append(theta)
            tracks.append(record)
            self.plots.append([car.pos[0],car.pos[1],car.phi,distance[2],distance[0],distance[1]])      #位置、方向、左、前、右距離
            car.move(theta)
        if dataset==0:
            with open("track4D.txt","w") as f:
                for track in tracks:
                    t=""
                    for record in track:
                        t+=(str(record)+' ')
                    f.write(str(t)+'\n')
        else:
            with open("track6D.txt","w") as f:
                for track in tracks:
                    t=""
                    for record in track:
                        t+=(str(record)+' ')
                    f.write(str(t)+'\n')

                
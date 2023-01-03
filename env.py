import numpy as np
import math
class Car:
    def __init__(self,pos,phi,radius=3):
        self.pos = np.asarray(pos).astype(float)
        self.phi = float(phi)
        self.radius = float(radius)
    def move(self, theta):
        c = math.radians(self.phi)
        t = math.radians(theta)
        self.pos[0] += math.cos(c+t) + math.sin(t)*math.sin(c)     # X-axis
        self.pos[1] += math.sin(c+t) - math.sin(t)*math.cos(c)     # Y-axis
        self.phi -= math.degrees(math.asin(2*math.sin(t)/self.radius))    # phi傾斜角度
    def sensor_dist(self, walls):
        slope_l = math.radians((self.phi + 45)% 360) 
        slope_r = math.radians((self.phi - 45)% 360) 
        slope_f = math.radians((self.phi)% 360)
        sensors = [slope_f, slope_r, slope_l]
        sensor_intersect = []
        for sensor in sensors:
            inter_dists = []
            for wall in walls:
                intersect = wall.radar_intersect(self.pos, sensor)
                if intersect is not None:
                    dist = np.linalg.norm(self.pos - intersect)
                    inter_dists.append(dist)
                    # inter_dists.append((intersect.tolist(), dist))
            mindis = min(inter_dists) if inter_dists else None
            sensor_intersect.append(mindis)
        return sensor_intersect
    def check_wall(self):
        if self.pos[0]-3<-6 or self.pos[0]+3>30:
            return True
        elif -6<self.pos[0]<18 and self.pos[1]+3>22:
            return True
        elif 22<self.pos[1]<50 and self.pos[0]-3<18:
            return True
        elif 6<self.pos[0]<30 and self.pos[1]-3<10:
            return True
        elif -3<self.pos[1]<10 and self.pos[0]+3>6:
            return True
        else:
            return False

class Wall:
    def __init__(self,start,end) :
        self.start=np.asarray(start).astype(float)
        self.end=np.asarray(end).astype(float)
        self.vector=np.asarray(self.start-self.end)
    def radar_intersect(self,pos,dir):
        pos = np.asarray(pos).astype(float)
        vector_radar = np.array([math.cos(dir), math.sin(dir)])
        a1=[vector_radar[0],self.vector[0]]
        a2=[vector_radar[1],self.vector[1]]
        a=np.array([a1,a2])
        b=self.start-pos
        if np.linalg.det(a) != 0:
            ps=np.linalg.solve(a,b)
            if(ps[0] > 0 and 0 < ps[1] < 1):
                inter = np.array(self.start) - ps[1]*self.vector
                return inter
        else:
            return None
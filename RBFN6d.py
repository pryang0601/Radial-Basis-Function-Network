import numpy as np
from kmeans6d import *
import copy
import math
class RBFN6d:
    def __init__(self):
        k=Kmeans6d()
        self.data=k.X
        self.truth=k.truth
        centers,clusters,kmeans_result=k.start_cluster()
        self.num_neuron=kmeans_result.K+1
        self.centers=centers
        self.clusters=clusters
        self.norms=np.zeros(kmeans_result.K)
        self.weights=np.zeros(kmeans_result.K)
        self.bias=-1
        self.epoch=1000
        self.rate=0.01
        self.neuron_init()
    def neuron_init(self):
        idx=-1
        for cluster,center in zip(self.clusters,self.centers):
            idx+=1
            radius=0
            w=0
            for c in cluster:
                point=self.data[c]
                w+=self.truth[c]
                radius+=np.linalg.norm(point-center)
            radius/=len(cluster)    
            w/=len(cluster)
            self.norms[idx]=radius
            self.weights[idx]=w
        self.training()
    def activate(self,x,c,n):
        # dis=np.linalg.norm(x-c)
        no=-1*((x-c).dot(x-c))
        deno=2*(n**2)
        return math.exp(no/deno)
    def output(self,x):
        out=0
        for weight,center,norm in zip(self.weights,self.centers,self.norms):
            b=self.activate(np.array(x),center,norm)
            out+=(round((b*weight),5))
        out+=self.bias
        if out>40:
            out=40
        elif out<-40:
            out=-40
        return out
    def training(self):
        for e in range(self.epoch):
            for i in range(self.data.shape[0]):
                idx=-1
                out=self.output(self.data[i])
                diff=self.truth[i]-out
                for center,norm,weight in zip(self.centers,self.norms,self.weights):
                    idx+=1
                    oldcenter=copy.copy(center)
                    b=self.activate(self.data[i],center,norm)
                    for j in range(len(center)):
                        center[j]=center[j]+self.rate*diff*weight*b*(1/math.pow(norm,2))*(self.data[i][j]-center[j])
                    norm=norm+self.rate*diff*weight*b*(1/math.pow(norm,3))*((np.linalg.norm(self.data[i]-oldcenter))**2)
                    weight=weight+self.rate*diff*b
                    self.centers[idx]=center
                    self.norms[idx]=norm
                    self.weights[idx]=weight
                self.bias=self.bias+self.rate*diff
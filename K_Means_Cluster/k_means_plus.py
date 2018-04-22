#coding=utf-8
from pylab import *
from math import pi, sin, cos
from collections import namedtuple
from random import random, choice
from copy import copy
from scipy.cluster.vq import *
 
try:
    import psyco
    psyco.full()
except ImportError:
    pass
 
 
FLOAT_MAX = 1e100
 
 
class Point:
    __slots__ = ["x", "y", "z","group"]
    def __init__(self, x=0.0, y=0.0,z=0.0,group=0):
        self.x, self.y,self.z,self.group = x, y,z,group
 
 
def generate_points(npoints):
    points = [Point() for _ in xrange(len(npoints))]
 
    # note: this is not a uniform 2-d distribution
    index = 0
    for p in points:
	p.x = npoints[index][0]
	p.y = npoints[index][1]
	p.z = npoints[index][2]
	index = index + 1
    return points
 
def nearest_cluster_center(point, cluster_centers):
    """Distance and index of the closest cluster center"""
    def sqr_distance_2D(a, b):
        return abs(a.x - b.x) *abs(a.x - b.x) +  abs(a.y - b.y) *abs(a.x - b.x) + abs(a.z-b.z)*abs(a.x - b.x)
    min_index = point.group
    min_dist = FLOAT_MAX
 
    for i, cc in enumerate(cluster_centers):
        d = sqr_distance_2D(cc, point)
        if min_dist > d:
            min_dist = d
            min_index = i
 
    return (min_index, min_dist)
 
 
def kpp(points, cluster_centers):
    cluster_centers[0] = copy(choice(points))
    d = [0.0 for _ in xrange(len(points))]
 
    for i in xrange(1, len(cluster_centers)):
        sum = 0
        for j, p in enumerate(points):
            d[j] = nearest_cluster_center(p, cluster_centers[:i])[1]
            sum += d[j]
 
        sum *= random()
 
        for j, di in enumerate(d):
            sum -= di
            if sum > 0:
                continue
            cluster_centers[i] = copy(points[j])
            break
 
    for p in points:
        p.group = nearest_cluster_center(p, cluster_centers)[0]
 
 
def lloyd(points, nclusters):
    features = array(points,'f')
    points = generate_points(points)
    cluster_centers = [Point() for _ in xrange(nclusters)]
    # call k++ init
    kpp(points, cluster_centers)
 
    lenpts10 = len(points) >> 10
 
    changed = 0
    while True:
        # group element for centroids are used as counters
        for cc in cluster_centers:
            cc.x = 0
            cc.y = 0
	    cc.z = 0
            cc.group = 0
 
        for p in points:
            cluster_centers[p.group].group += 1
            cluster_centers[p.group].x += p.x
            cluster_centers[p.group].y += p.y
	    cluster_centers[p.group].z += p.z
 
        for cc in cluster_centers:
            cc.x /= cc.group
            cc.y /= cc.group
	    cc.z /= cc.group
 
        # find closest centroid of each PointPtr
        changed = 0
        for p in points:
            min_i = nearest_cluster_center(p, cluster_centers)[0]
            if min_i != p.group:
                changed += 1
                p.group = min_i
 
        # stop when 99.9% of points are good
        if changed <= lenpts10:
            break
 
    for i, cc in enumerate(cluster_centers):
        cc.group = i
    centers = []
    for cluster in cluster_centers:
	centers.append([cluster.x, cluster.y, cluster.z])
    centers = array(centers,'f')
    return centers,features

 

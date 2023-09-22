class edge():
    def __init__(self,time,test=None):
        self.time=time
        self.test=test     
class node():
    def __init__(self,value,name):
        self.value=value
        self.name=name
        self.child=[]
class degree(node): 
    def getName(self):
        return self.name

class job(node):
    def __init__(self,sal):
        self.sal=sal
    def getName(self):
        return self.name
class graph():
    def __init__(self,degree):
        self.Mainnode=degree("tenth",10)
    def traversalByTime(time):
        pass
    def traversalByJob(job):
        pass
    def traversalBySalary(salary):
        pass

d1=degree("Intermediate M",12.0)
d2=degree("Intermediate ",12.1)
d3=degree("Intermediate")
        

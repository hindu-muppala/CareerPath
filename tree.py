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
    def __init__(self,value,name,sal):
        super.__init__(value,name)
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

d1=degree(12.0,"Intermediate MPC")
d2=degree(12.1,"Intermediate BiPC")
d3=degree(12.2,"CEC")
d4=degree(13.0,"Polytechnical Mechanical")
d5=degree(13.1,"Polytechnic CSE")
d6=degree(13.2,"Polytechnic Civil")
d7=degree(13.3,"Polytechnic IT")
d8=degree(13.4,"Polytechnic Aeronautical")
d9=degree(16.0,"BTech CSE")
d10=degree(16.1,"BTech IT")
d11=degree(21,"LLB")
d12=degree(22,"Bachelors")
j0=job(23,"IFS",())
j1=job(24,"IAS",())
        

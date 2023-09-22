class edge():
    def __init__(self,time,next,Entrancetest=None):
        self.time=time
        self.test=Entrancetest 
        self.next=next   
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
        super().__init__(value,name)
        self.sal=sal
    def getName(self):
        return self.name 
class graph():
    def __init__(self):
        self.Mainnode=degree("tenth",10.0)
    def traversalByTime(time):
        pass
    def traversalByJob(job):
        pass
    def traversalBySalary(salary):
        pass
def travesalByTime(t,n,path):
    if len(n.child)==0:
        print(path)
    for i in n.child:
        if i.time < t:
            travesalByTime(t,i.next,path+n.value)

d1=degree(12.0,"Intermediate MPC")
d2=degree(12.1,"Intermediate BiPC")
d3=degree(12.2,"Intermediate CEC")
d4=degree(13.0,"Polytechnical Mechanical")
d5=degree(13.1,"Polytechnic CSE")
d6=degree(13.2,"Polytechnic Civil")
d7=degree(13.3,"Polytechnic IT")
d8=degree(13.4,"Polytechnic Aeronautical")
d9=degree(16.0,"BTech CSE")
d10=degree(16.1,"BTech IT")
d11=degree(21,"LLB")
d12=degree(22,"Bachelors")
j0=job(101,"IFS",(9.6,30))
j1=job(102,"IAS",(6.7,15.8))
j2=job(103,"Data Analyst",(4,9))
j3=job(104,"Lawyer",(3,10))
j4=job(105,"Scientist",(6,17))      
j5=job(106,"IPS",(6.7,27))
j6=job(107,"Indian Army",(2.5,30))
j7=job(108,"Indian Air",(1.5,13))
j8=job(109,"Indian Navy",(6,30))

CareerPath=graph()
CareerPath.Mainnode.child=[edge(2,d1),edge(2,d2),edge(2,d3),edge(3,d4),edge(3,d5),edge(3,d6),
                           edge(3,d7),edge(3,d8)]
d1.child=[edge(6,d9),edge(6,d10),edge(6,d11)]
d2.child=[edge(6,d12)]
d4.child=[edge(6,d12)]
d5.child=[edge(6,d9),edge(6,d10),edge(6,d11)]
d6.child=[edge(6,d12)]
d7.child=[edge(6,d9),edge(6,d10),edge(6,d11)]
d9.child=[edge(6,j2),edge(6,j0),edge(6,j1),edge(6,j5),edge(6,j4)]
d10.child=[edge(6,j2),edge(6,j0),edge(6,j1),edge(6,j5),edge(6,j4)]
d12.child=[edge(6,j2),edge(6,j0),edge(6,j1),edge(6,j5),edge(6,j4),edge(9,d11)]
d11.child=[edge(9,j3)]
travesalByTime(6,CareerPath.Mainnode,"")
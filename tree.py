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
        self.Mainnode=degree(10.0,"tenth")

def travesalByTime(t, n, path,pathList):
    new_path = path+ '-->' + str(n.name)
    if len(n.child) == 0:
       # print(new_path)
        pathList.append(new_path)
        return pathList
    for i in n.child:
        if i.time <= t:
            pathList=travesalByTime(t, i.next, new_path,pathList)
    return pathList
def traversalByJob(job, n, path,pathList):
    new_path = path+ '-->' +str(n.name)
    if str(n.name) == job:
     #   print(new_path)
        pathList.append(new_path)
        return pathList
    for i in n.child:
        pathList=traversalByJob(job, i.next, new_path,pathList)
    return pathList
def traversalBySalary(jlist,salary):
    Output_list=[]
    for i in jlist:
        if salary > i.sal[0] and salary < i.sal[1]:
            Output_list.extend(traversalByJob(i.name,CareerPath.Mainnode,'',[]))
    return Output_list
d1=degree(12.0,"Intermediate MPC")
d5=degree(13.1,"Polytechnic CSE")
d10=degree(16.1,"BTech IT")
d11=degree(21,"LLB")
d12=degree(22,"Bachelors")
j0=job(101,"IFS",(9.6,30))
j1=job(102,"IAS",(6.7,15.8))
j2=job(103,"Data Analyst",(4,9))
j3=job(104,"Lawyer",(3,10))     
j5=job(106,"IPS",(6.7,27))
j6=job(107,"Indian Army",(2.5,30))
j7=job(108,"Indian Air",(1.5,13))
j8=job(109,"Indian Navy",(6,30))
jlist=[j0,j1,j2,j3,j5,j6,j7,j8]
CareerPath=graph()
CareerPath.Mainnode.child=[edge(2,d1),edge(3,d5)]
d1.child=[edge(6,d10),edge(6,d11)]
d5.child=[edge(6,d10),edge(6,d11)]
d10.child=[edge(6,j2),edge(6,j0),edge(6,j1),edge(6,j5)]
d12.child=[edge(6,j2),edge(6,j0),edge(6,j1),edge(6,j5),edge(9,d11)]
d11.child=[edge(9,j3)]
print(travesalByTime(6,CareerPath.Mainnode,"",[]))
print(traversalByJob("Data Analyst", CareerPath.Mainnode, "",[]))
print(traversalBySalary(jlist,12))
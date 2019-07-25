class Student: #must be title case
    name = ""
    age =()
    gender = ""
    math = 0
    eng = 0
    swa = 0
    sci = 0
    soc = 0
    total=0
    avg=0

    #create a constructor to instatiate the class

    def __init__(self, n, a, g, math, eng, swa, sci, soc):
        Student.name=n
        Student.age=a
        Student.gender=g
        Student.math=math
        Student.eng=eng
        Student.swa=swa
        Student.sci=sci
        Student.soc=soc
        Student.total(self)
        Student.avg(self)


    def total(self):
        self.total= self.math+self.eng+self.swa+self.sci+self.soc


    def avg(self):
        self.avg=self.total/5




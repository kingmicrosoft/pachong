__author__ = 'wisdom'

total=20

def translate():
    s='xxxx'
    print list(s)
    print str(list(s))
    print tuple(s)
    data=    list(s)
    print("".join(data))
    print "".join(tuple(s))
    print str(tuple(s))
    # print hex(s)


def getData(num=10, *args):
    "test for getdata"
    total=num
    print 'output',num
    # print num
    for var in args:
        print  var
    str1="cain1234"+str(3)
    print "%d is %d kg" % (num,3)
    print "shdus %s cain %s" % ("csd","dd")
    print str1


class User :
    __cainAttri=''
    'user table'
    def __init__(self,name,id):
        self.name=name
        self.id =id
        self.__cainAttri=name
    def getName(self):
        return self.name
    def getId(self):
        return self.id


    def outputData(self):
        print self.__cainAttri+'  private '
        print " name is %s" % self.name+" and id is %d" % self.id


class Cain (User):

    def __init__(self):
        pass
    def getCainName(self):
        return 'cain'


if __name__ == '__main__':
    # translate()
    # getData(12,13,"cain","cain12")
    # print total
    # var1,var2=20,30
    #
    # sum=lambda var1, var2 :var1+var2
    # print sum(1,20)


    user = User("brucee",1010)

    print    user.getName()
    user.outputData()

    print user.__dict__
    print user.__module__
    cain =Cain()
    print cain.getCainName()
    # cain.getCainName(user)

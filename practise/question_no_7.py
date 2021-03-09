#you have four miles for uni bus ko speed is 25mph and takes 10 stops 2minutes each.. then by jogging speed is 7mph for
#1st and last mile and 15mph for middle 2 miles... find out which one is faster



bussp=int(input("enter the speed of the bus"))
tm=4
timebus=(4/bussp)
timeloss=(2*10)/60
totaltime=timebus+timeloss
print("total time taken by bus",totaltime)
stu1=int(input("enter speed for 1st mile"))
stu2=int(input("enter speed for second and third mile" ))
stu3=int(input("enter the speed for fourth mile"))
dis1=(1/stu1)
dis2=(2/stu2)
dis3=(1/stu3)
totalstuti=dis1+dis2+dis3
if totaltime>totalstuti:
    print("will reach faster by jogging")
else:
    print("will reach faster by bus")

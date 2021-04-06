#WAP to print marksheet

math=int(input("enter marks obtained in maths "))
science=int(input("makrs obtained in science"))
english=int(input("marks obtained in english"))
nepali=int(input("enter marks obtained in nepali"))
total_marks=math+science+english+nepali
full_marks=400
per=(total_marks/full_marks)*100
print("total marks",total_marks)
print("percentage:",per,"%")

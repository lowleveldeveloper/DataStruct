l=['문학','영어','수학','확통','생명','화학','중국어','미술','체육','고윤','진로']
w=[]


print(l)
n=int(input("공지할 과목 수:"))

f=open('공지용.txt',"w")
f.write("☆수행평가 공지☆ \n")
f.write("\n")

for x in range(0,n):
    q=str(input("공지할 과목 선택:"))
    c=str(input("과목의 내용:"))
    t=str(input("과목의 데드라인:"))
    f.write("<")
    f.write(q)
    f.write(">")
    f.write(": ")
    f.write(c)
    f.write("\n")
    f.write("  //기한: ")
    f.write(t)
    f.write("\n")
    f.write("\n")
f.close()


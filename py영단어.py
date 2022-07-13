import random as r

f=["scholarship","grant","qualification","uneasiness","barely","confine","give a grin","proceed","distracted","relevant","redundant","hesitate","content","pitcher","batter","intimidate","intuitively","come in contact with","ensure","reunion","patron"]
s=["by the same token","fungus","hardy","crusty","moderate","chemical","excessive","isle","chimney","landmass","coral","enrollment","ethnic","account for","just around the corner","drop off","reception","no charge","portable","compression","conform to"]

f2=['장학금','주다','자격조건','불안감','거의 아니게','가두다','씩 웃어주다','나아가다','정신 산만한','관련된','반복 되어 불필요한','주저하다','요지','투수','타자','위협하다','직관적으로','와 접촉하다','보장하다','친목모임','고객']
s2=['마찬가지로','균류','강인한','껍질이 딱딱한','중간의','화학물질','과잉의','섬','굴뚝','육지','산호의','등록','민족의','차지하다','임박한','갖다놓다','수신','무료','휴대용의','압박','을 따르다']

while True:
    a=r.randrange(0,20)
    print(f[a])
    n=int(input())
    print(f2[a])
    print("===================")
    if n == 0:
        while True:
            a=r.randrange(0,20)
            print(s[a])
            m=input()
            print(s2[a])
            print("===================")
    else:
        continue


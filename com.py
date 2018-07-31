
import numpy as np
import matplotlib.pyplot as plt
import math
import pprint
def dis(a,b):
    c = 0.0
    for i in range(len(a)):
        c+=math.pow(a[i] - b[i],2)
    return math.sqrt(c)
def ang(j1,j2,j3):
    a=[0,0,0]
    b=[0,0,0]
    for i in range(3):
        a[i]=j1[i]-j2[i]
        b[i]=j3[i]-j2[i]
    c=a[0]*b[0]+a[1]*b[1]+a[2]*b[2]
    l=math.sqrt((a[0]**2+a[1]**2+a[2]**2)*(b[0]**2+b[1]**2+b[2]**2))
    return math.acos(c/l)*(180/math.pi)
#點座標轉角度
#1070730版本--19節
def datatoang(data):
    a=[#ang(data["FootLeft"],data["AnkleLeft"],data["KneeLeft"]),#1
        ang(data["FootRight"],data["AnkleRight"],data["KneeRight"]),
        ang(data["FootLeft"],data["KneeLeft"],data["HipLeft"]),
        ang(data["FootRight"],data["KneeRight"],data["HipRight"]),
        ang(data["KneeLeft"],data["HipLeft"],data["SpineBase"]),#5
        ang(data["KneeRight"],data["HipRight"],data["SpineBase"]),
        #ang(data["AnkleLeft"],data["SpineBase"],data["AnkleRight"]),
        ang(data["KneeLeft"],data["SpineBase"],data["KneeRight"]),
        ang(data["ElbowLeft"],data["SpineBase"],data["ElbowRight"]),
        ang(data["FootLeft"],data["SpineBase"],data["WristLeft"]),#10
        ang(data["FootRight"],data["SpineBase"],data["WristRight"]),
        ang(data["SpineBase"],data["SpineShoulder"],data["Head"]),
        ang(data["ElbowLeft"],data["SpineShoulder"],data["ElbowRight"]),
        ang(data["WristLeft"],data["SpineShoulder"],data["WristRight"]),
        ang(data["SpineBase"],data["ShoulderLeft"],data["ElbowLeft"]),#15
        ang(data["SpineBase"],data["ShoulderRight"],data["ElbowRight"]),
        ang(data["SpineShoulder"],data["ShoulderLeft"],data["ElbowLeft"]),
        ang(data["SpineShoulder"],data["ShoulderRight"],data["ElbowRight"]),
        ang(data["ShoulderLeft"],data["ElbowLeft"],data["WristLeft"]),
        ang(data["ShoulderRight"],data["ElbowRight"],data["WristRight"]),#20
        ang(data["ShoulderLeft"],data["Head"],data["ShoulderRight"])]
    b=[ang(data["FootLeft"],data["AnkleLeft"],data["KneeLeft"]),#1
        ang(data["FootRight"],data["AnkleRight"],data["KneeRight"]),
        ang(data["FootLeft"],data["KneeLeft"],data["HipLeft"]),
        ang(data["FootRight"],data["KneeRight"],data["HipRight"]),
        ang(data["KneeLeft"],data["HipLeft"],data["SpineBase"]),#5
        ang(data["KneeRight"],data["HipRight"],data["SpineBase"]),
        ang(data["AnkleLeft"],data["SpineBase"],data["AnkleRight"]),
        ang(data["KneeLeft"],data["SpineBase"],data["KneeRight"]),
        ang(data["ElbowLeft"],data["SpineBase"],data["ElbowRight"]),
        ang(data["FootLeft"],data["SpineBase"],data["WristLeft"]),#10
        ang(data["FootRight"],data["SpineBase"],data["WristRight"]),
        ang(data["SpineBase"],data["SpineShoulder"],data["Head"]),
        ang(data["ElbowLeft"],data["SpineShoulder"],data["ElbowRight"]),
        ang(data["WristLeft"],data["SpineShoulder"],data["WristRight"]),
        ang(data["SpineBase"],data["ShoulderLeft"],data["ElbowLeft"]),#15
        ang(data["SpineBase"],data["ShoulderRight"],data["ElbowRight"]),
        ang(data["SpineShoulder"],data["ShoulderLeft"],data["ElbowLeft"]),
        ang(data["SpineShoulder"],data["ShoulderRight"],data["ElbowRight"]),
        ang(data["ShoulderLeft"],data["ElbowLeft"],data["WristLeft"]),
        ang(data["ShoulderRight"],data["ElbowRight"],data["WristRight"]),#20
        ang(data["ShoulderLeft"],data["Head"],data["ShoulderRight"])]
    return b

#將原始點座標txt讀入，轉成角度資料存檔
#who=實驗者代號(WCZAX)
#expnum=第幾回實驗
#nowmax=現在最大輸出編號
def tansdata(who,expnum,nowmax,where):
    f = open("原始資料區\\" + who+str(expnum) + ".txt", "r")
    data = f.readlines()
    f.close()
    adata =[{"time":0,
        "SpineBase":[0,0,0],
        "SpineMid":[0,0,0],
        "Neck":[0,0,0],
        "Head":[0,0,0],
        "ShoulderLeft":[0,0,0],
        "ElbowLeft":[0,0,0],
        "WristLeft":[0,0,0],
        "HandLeft":[0,0,0],
        "ShoulderRight":[0,0,0],
        "ElbowRight":[0,0,0],
        "WristRight":[0,0,0],
        "HandRight":[0,0,0],
        "HipLeft":[0,0,0],
        "KneeLeft":[0,0,0],
        "AnkleLeft":[0,0,0],
        "FootLeft":[0,0,0],
        "HipRight":[0,0,0],
        "KneeRight":[0,0,0],
        "AnkleRight":[0,0,0],
        "FootRight":[0,0,0],
        "SpineShoulder":[0,0,0],
        "HandTipLeft":[0,0,0],
        "ThumbLeft":[0,0,0],
        "HandTipRight":[0,0,0],
        "ThumbRight":[0,0,0]} for i in range(int(len(data)/25))]
    for i in range(len(data)):
        data[i] = data[i].split(",")
        data[i][2] = int(data[i][0]) * 60000 + int(data[i][1]) * 1000 + int(data[i][2])
        data[i][4] = float(data[i][4])
        data[i][5] = float(data[i][5])
        data[i][6] = float(data[i][6])
        ii=int(i/25)
        adata[ii][data[i][3]]=[data[i][4],data[i][5],data[i][6]]
        adata[ii]["time"]=data[i][2]
    p1=[]
    p2=[]
    p3=[]
    for a in adata:
        p2+=[dis(a["AnkleRight"],a["AnkleLeft"])]
        p1+=[a["time"]]
    pole=[]
    maxmin=0#=0大開始，=1小開始
    allpole=0
    for i in range(1,len(adata)-1):
        if p2[i]>p2[i+1] and p2[i]>p2[i-1]:
            #print(allpole,p1[i],"雙腳著地")
            pole+=[[p1[i],p2[i]]]
            allpole=allpole+1
            if allpole==0:
                maxmin=0
        if p2[i]<p2[i+1] and p2[i]<p2[i-1]:
            #print(allpole,p1[i],"單腳站立")
            pole+=[[p1[i],p2[i]]]
            allpole=allpole+1
            if allpole==0:
                maxmin=1
    #取兩腳部幅>0.25公尺之極點
    useable=[]
    for i in range(1,allpole):
        if abs(pole[i][1]-pole[i-1][1])>0.25 :
            useable+=[i]
    #取其次個極點亦為通過上述之條件
    useable2=[]
    for i in range(0,len(useable)-1):
        if useable[i]+1==useable[i+1]:
            useable2+=[useable[i]]
            useable2+=[useable[i+1]]
    ii=0
    useset=[]
    for a in range(len(adata)):
        while  ii<len(useable2) and adata[a]["time"]==pole[useable2[ii]][0] :
            #useset+=[datatoang(adata[a-1]),datatoang(adata[a]),datatoang(adata[a+1])]
            useset+=[datatoang(adata[a])]
            #print("add",useable2[ii],pole[useable2[ii]][0])
            ii=ii+1
    nametonum=["","W","C","Z","A","X"]
    cla=str(nametonum.index(who))
    num=nowmax
    d=[]
    for i in range(0,len(useset),2):
        if maxmin==1:
            dl=useset[i]#+useset[i+1]+useset[i+2]
            dh=useset[i+1]#+useset[i+4]+useset[i+5]
            d=dl+dh

        elif maxmin==0:
            dh=useset[i]#+useset[i+1]+useset[i+2]
            dl=useset[i+1]#+useset[i+4]+useset[i+5]
            d=dl+dh
        f=open(where+ cla+"-"+str(int(num)+(i//2))+ ".txt", "w")
        for a in d:
            f.write(str(a)+"\n")
        f.close()
    return len(useset)/2

def readdata(datanum,people,where):
    adata=[[0 for i in range(datanum[j])] for j in range(people)]
    for i in range(people):
        for j in range(datanum[i]):
            f=open(where+ str(i+1)+"-"+str(j+1) + ".txt","r")
            adata[i][j]=f.readlines()
            f.close()
    for i in range(len(adata)):
        for j in range(len(adata[i])):
            for k in range(len(adata[i][j])):
                adata[i][j][k]=float(adata[i][j][k])
    return adata
def GLdata(adata,ang):
    bdata=[[] for j in range(len(adata))]
    for i in range(len(adata)):
        mean=[0 for j in range(len(adata[i][0]))]
        for j in range(len(adata[i])):
            for k in range(len(adata[i][j])):
                mean[k]+=adata[i][j][k]/len(adata[i])
        #print(mean)
        
        for j in range(len(adata[i])):
            for k in range(len(adata[i][j])): 
                if abs(adata[i][j][k]-mean[k])<ang:
                    if k==len(adata[i][j])-1:
                        bdata[i]+=[adata[i][j]]
                        #print(i,"的第",j,"筆加入，第",k,"，平均為",mean[k],"其值為",adata[i][j][k])
                else:
                    #print(i,"的第",j,"筆的第",k,"個維度差異過大，平均為",mean[k],"其值為",adata[i][j][k])
                    break
    return bdata
#打亂資料
def randdata(adata):
    import random
    newdata=[[] for i in range(len(adata))]
    for p in range(len(adata)):
        n=len(adata[p])
        tdata=[-1 for i in range(n)]
        j=0
        for i in range(n):
            while 1:
                a=random.randint(0,n-1)
                if tdata[a]==-1:
                    tdata[a]=j
                    j=j+1
                    break

        for i in range(n):
            newdata[p]+=[adata[p][tdata[i]]]
    return newdata

def cutdata(adata,TrainDataFrom=0,TrainDataEnd=-1,TestDataFrom=-1,TestDataEnd=-1):
    if TrainDataEnd==-1:
        dlen=[]
        for i in range(len(adata)):
            dlen+=[len(adata[i])]
            
        TrainDataEnd=min(dlen)//2
    if TestDataFrom==-1:
        TestDataFrom=TrainDataEnd
    bdata=[0 for i in range(len(adata))]
    for i in range(len(adata)):
            bdata[i]=adata[i][TrainDataFrom:TrainDataEnd]
    if TestDataEnd==-1:
        cdata=[0 for i in range(len(adata))]
        for i in range(len(adata)):
            cdata[i]=adata[i][TestDataFrom:len(adata[i])]        
    else:
        cdata=[0 for i in range(len(adata))]
        for i in range(len(adata)):
            cdata[i]=adata[i][TestDataFrom:TestDataEnd]
    return bdata,cdata
#列印結果
def printres(res,table=1,rec=1,pre=1,acc=1):
    import pandas
    import copy
    pres=copy.deepcopy(res)
    if table==1:
        display(pandas.DataFrame(pres))
    recall=[]
    precision=[]
    for i in range(len(res)):
        r=0
        p=0
        for j in range(len(res[i])):
            r+=res[i][j]
            p+=res[j][i]
        recall+=[res[i][i]/r]
        if p==0:
            p=1
        precision+=[res[i][i]/p]
    if rec==1:
        print("召回率")
        print(recall)
    if pre==1:
        print("精確率")
        print(precision)
    ZQL=0
    tot=0
    isright=0
    for i in range(len(res)):
        for j in range(len(res[i])):
            tot+=res[i][j]
            if i==j:
                isright+=res[i][j]
        ZQL=isright/tot
    if acc==1:
        print("準確率",ZQL)
    f1=[]
    for i in range(len(recall)):
        if recall[i]==0 or precision[i]==0:
            f1+=[0]
        else:
            f1+=[2/((1/recall[i])+(1/precision[i]))]
    print("f1平均為:",float(sum(f1))/len(f1))
    return {"ZHL":recall,"JQL":precision,"ZQL":ZQL,"f1TH":f1,"f1THPJ":float(sum(f1))/len(f1)}
def HT(x,y,xlabel,ylabel,title=""):
    import matplotlib.pyplot as plt
    if title=="":
        title=xlabel+"對"+ylabel+"的影響"
    plt.plot(x,y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.savefig(title, dpi=600)
    plt.show()
def divdata(adata):
    data = []
    label = []
    for i in range(len(adata)):
        for j in range(len(adata[i])):
            data += [adata[i][j]]
            label += [i]
    return data, label
class KNN:
    def __init__(self,data):
        self.data=data
    def test(self,testdata,k=1):
        ddata=[]
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                ddata+=[[i,dis(self.data[i][j],testdata)]]
        ddata=sorted(ddata, key = lambda x : x[1]) 
        ans=[0 for i in range(len(self.data))]
        totd=0
        for i in range(k):
            ans[(ddata[i][0])]+=1/ddata[i][1]
        return ans.index(max(ans))
    def bigtest(self,testdata,k=1):
        res=[[0 for j in range(len(testdata))] for i in range(len(testdata))]
        for i in range(len(testdata)):
            for j in range(len(testdata[i])):
                ans=self.test(testdata[i][j],k)
                res[i][ans]+=1
        return res

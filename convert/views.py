from django.shortcuts import render
import os
import glob



def convert(request):
    if request.POST:
        print(request.POST)
        print(request.FILES)
        files2 = glob.glob('static/file/*')    #для удаление всехфайлов из static/file/
        for f in files2:
            os.remove(f)                        #собственно удалениее файлов
        file=request.FILES["file"]
        print(file)
        sname=str(file)
        name=''
        nb=0
        bn=sname[nb]
        print(bn)

        while bn != ".":
            name=name+bn
            nb=nb+1
            bn=sname[nb]
        namebtn="Скачать " + name+"(n,x,y,z,kod)"+".txt"
        name="static/file/"+name+"(n,x,y,z,kod)"+".txt"
        print(name)
        lines = file.readlines()


        print(len(lines))
        i=0
        a=[1,2,3,4]
        nxyzkd=open(name,"w")
        for line in file:
            i=i+1
            if i not in a:
                #print(line[2:4])
                s=str(line)
              #  print(s[22])

                if s[4:6] == 'TP':
                    i0=22
                    sx=s[i0]
                    x=''
                    while sx != " ":
                        i0=i0+1
                        x=x+sx
                        sx=s[i0]
                    i1=21
                    sn=s[i1]
                    n=''
                    while sn != " ":
                        i1=i1-1
                        n=sn+n
                        sn=s[i1]
                    while sx == " ":
                        i0=i0+1
                        sx=s[i0]
                        sy=sx
                    y=""
                    while sy != " ":
                        i0=i0+1
                        y=y+sy
                        sy=s[i0]
                    while sy == " ":
                        i0=i0+1
                        sy=s[i0]
                        sz=sy
                    z=""
                    while sz != " ":
                        i0=i0+1
                        z=z+sz
                        sz=s[i0]
                    while sz == " ":
                        i0=i0+1
                        sz=s[i0]
                        skod=sz
                    kd=""

                    while skod != " ":
                        i0=i0+1
                        kd= kd + skod
                        skod=s[i0]

                    print(n,',' , x ,',',y,',',z,',', kd)
                    stroka=n+',' + x +','+ y +',' +  z + ',' + kd +'\n'
                    nxyzkd.write(stroka)

        nxyzkd.close()
        nxyzkd=open(name,"r")
        f=nxyzkd.read()

        print(f)

        nxyzkd.close()



    return render(request,'convert/convert.html',locals())

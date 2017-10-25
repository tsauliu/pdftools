# -*-coding:gbk -*-
from PyPDF2 import PdfFileWriter, PdfFileReader
import os, copy

dir='C:\Users\Liu\Dropbox\#cicc_alpha/6-Dazhuang/'  #文件所在路径

filename = os.listdir(dir)

N=5 #把pdf 文件分割成几列

def becomemutliplepage(filename,Npage):
    fileread = PdfFileReader(open(dir + filename, 'rb'), strict=False)
    output = PdfFileWriter()
    p = fileread.getPage(0)
    for i in range(Npage):
        output.addPage(p)

    newpath = dir + '/temp/'
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    outputStream = file(newpath + filename[0:-4] + '-temp.pdf', "wb")
    output.write(outputStream)
    outputStream.close()

def two_col_to_one(filename):
    fileread = PdfFileReader(open(dir+filename, 'rb'), strict=False)
    output = PdfFileWriter()

    p = fileread.getPage(0)
    lf = p.mediaBox.lowerLeft
    ur = p.mediaBox.upperRight
    print lf,ur
    # print type(ur[0])
    pagew=ur[0]/N
    # print type(pagew)
    thepagew=float(ur[0])
    thepagel=float(ur[1])
    pagel=float(1.41)*float(pagew)
    row_count_all=int(float(ur[1])/pagel)

    becomemutliplepage(filename, N*(row_count_all+1))

    q = PdfFileReader(open(dir+filename, 'rb'), strict=False).getPage(0)

    pagenumtocrop=0

    for row_count in range(1,row_count_all+2):
        for colcount in range(1,N+1):
            print [row_count,colcount]


            pur=(float(pagew*colcount) , thepagel-float(pagel*(row_count-1)))
            print 'page ur',pur
            plf=(float(pagew*(colcount-1)) , thepagel-pagel*(row_count))
            print 'page lf',plf
            p2 = PdfFileReader(open(dir + '/temp/' + filename[0:-4] + '-temp.pdf', 'rb'), strict=False).getPage(pagenumtocrop)
            p2.mediaBox.upperRight = pur
            p2.mediaBox.lowerLeft = plf
            output.addPage(p2)
            pagenumtocrop+=1
        #     print '-'*30
        # print '*'*30
    # for colcount in range(1, N + 1):
    #     print [row_count_all+1,colcount]


    newpath = dir+'/output/'
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    outputStream = file(newpath+filename[0:-4] + '-'+str(N)+'-col.pdf', "wb")
    output.write(outputStream)
    outputStream.close()


for i in filename:
    filename = i
    print filename.decode('gbk')
    if 'pdf' in filename[-4:]:
        # becomemutliplepage(filename, 3)
        two_col_to_one(filename)
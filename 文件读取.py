import os
#文件读取写入
def work(path):
    #要保存的文件路径
    restPath = r"C:\Users\Administrator\Desktop\test"
    with open(path,"r") as f:
        while True:
            lineInfo = f.readline()
            if len(lineInfo) < 5:
                break
            #截取邮箱
            email = lineInfo.split("----")[0]
            #截取邮箱类型
            fileType = email.split("@")[1].split(".")[0]
            #路径拼接   绝对路径+邮箱类型
            dir = os.path.join(restPath,fileType)
            #判断目录是否存在如果不存在
            if not os.path.exists(dir):
                #创建目录
                os.mkdir(dir)
            #创建文件
            filePath = os.path.join(dir,fileType+".txt")
            #打开文件
            with open(filePath,"a") as fw:
                #写内容
                fw.write(email+"\n")
#遍历目录
def getAllDirRecu(path, sp = "  " ):
    #获取当前文件下的所有文件
    fileList = os.listdir(path)
    #处理文件名
    sp += "    "
    for fileName in fileList:
        #判断当前目录是否是路径还是文件
        filePath = os.path.join(path,fileName)
        #如果是文件打印目录名称
        if os.path.isdir(filePath):
            print(sp + "目录：", fileName)
            #递归调用
            getAllDirRecu(filePath, sp)
        else:
            work(filePath)
getAllDirRecu(r"C:\Users\Administrator\Desktop\test")

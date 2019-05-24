import os
def work(path):
    restPath = r"C:\Users\Administrator\Desktop\test"
    with open(path,"r") as f:
        while True:
            lineInfo = f.readline()
            if len(lineInfo) < 5:
                break
            email = lineInfo.split("----")[0]
            fileType = email.split("@")[1].split(".")[0]
            dir = os.path.join(restPath,fileType)
            if not os.path.exists(dir):
                os.mkdir(dir)
            filePath = os.path.join(dir,fileType+".txt")
            with open(filePath,"a") as fw:
                fw.write(email+"\n")
def getAllDirRecu(path, sp = "  " ):
    fileList = os.listdir(path)
    sp += "    "
    for fileName in fileList:
        filePath = os.path.join(path,fileName)
        if os.path.isdir(filePath):
            print(sp + "目录：", fileName)
            getAllDirRecu(filePath, sp)
        else:
            work(filePath)
getAllDirRecu(r"C:\Users\Administrator\Desktop\test")

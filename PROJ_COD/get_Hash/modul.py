import hashlib, glob, os

def fileScan(filename):
    try:
        db = open("db.txt", 'r')
        checkFile = open(filename, 'r')
    except:
        print("DB File Read Fail")

    myMd5 = hashlib.md5()
    print(filename)

    with open("C:\\TMP2\\AdobePhotoshopCS5@19_50184.exe", 'rb') as checkFile:
        for chunk in iter(lambda: checkFile.read(8192), ''):
            myMd5.update(chunk)
            line = db.readline()
            if line == '':
               break
            line = line.rstrip('\n')
            if myMd5.hexdigest().upper() == line:
                print(line)
                checkFile.close()
                db.close()
                return filename
        checkFile.close()
        db.close()

if __name__ == "__main__":
    flist = glob.glob('C:\\TMP2\\*.exe')

    for i in flist:
        if fileScan(i) is not None:
            print("find :",i,os.path.getsize(i))
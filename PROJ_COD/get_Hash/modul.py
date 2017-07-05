import hashlib, glob, os

def fileScan(filename):
    try:
        db = open("C:/Users/kitri/Desktop/new/db.txt", 'r')
        checkFile = open(filename, 'r')
    except:
        print("DB File Read Fail")

    myMd5 = hashlib.md5()

    with open(filename, 'rb') as checkFile:
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
    flist = glob.glob('C:/Users/kitri/Desktop/new/*.txt')

    for i in flist:
        if fileScan(i) is not None:
            print("find :",i,os.path.getsize(i))
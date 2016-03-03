import os, ftplib

print "Connecting to FTP Site..."
ftp = ftplib.FTP("ftp.phila-records.com", "anonymous", "your@email.com")

myDirs = ftp.dir()
print myDirs

directory = "/Year-to-Date Transaction Files/"
print "Changing directory to " + directory
ftp.cwd(directory)
transDirs = ftp.nlst()
print transDirs

filematch = "*.txt"
archiveTo = "Path/to/directory"

for currentDir in transDirs:
    ftp.cwd(directory + currentDir)
    for filename in ftp.nlst(filematch):
        print filename
        fhandle = open(os.path.join(archiveTo, filename), "wb")
        ftp.retrbinary("RETR " + filename, fhandle.write)
       fhandle.close()

ftp.quit()


print "Done!"
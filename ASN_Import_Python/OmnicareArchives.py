import sys
import os
import shutil

# Module moves Omnicare "PUT" files ready for archive into an archive folder based on month and year. If specific folder does not exist, will create it.
def ftnPutArchive():
    strFileName = str(0)

    strDirectory = "\\\\charon.pdi.local\\d$\\SFTP\\Omnicare\\PUT\\ARCHIVE"
    os.chdir(strDirectory)

    strFiles = os.listdir(strDirectory)

    for strFileName in strFiles:
        print(strFileName)
        if strFileName.endswith(".ootw"):
            strOotwFile = str(strFileName)
            strFileDate = str(strOotwFile[:6])
            strFileYear = str(strFileDate[:4] + "-" + strFileDate[4:6])
            if os.path.exists(strFileYear):
                strNewDirPath = os.path.join(strDirectory, strFileYear)
                if strFileName.startswith(strFileDate) and strFileName.endswith(".ootw"):
                    strFilePath = os.path.join(strDirectory, strFileName)
                    shutil.move(strFilePath, strNewDirPath)
            else:
                os.makedirs(strFileYear)
                strNewDirPath = os.path.join(strDirectory, strFileYear)
                if strFileName.startswith(strFileDate) and strFileName.endswith(".ootw"):
                    strFilePath = os.path.join(strDirectory, strFileName)
                    shutil.move(strFilePath, strNewDirPath)

# Module moves Omnicare archived files into an archive folder based on month and year. If specific folder does not exist, will create it.
def ftnOmnicareArchive():
    strFileNameOA = str(0)

    strDirectoryOA = "\\\\charon.pdi.local\\d$\\SFTP\\Omnicare\\Archive"
    os.chdir(strDirectoryOA)

    strFilesOA = os.listdir(strDirectoryOA)

    for strFileNameOA in strFilesOA:
        print(strFileNameOA)
        if strFileNameOA.endswith(".ASN"):
            strAsnFile = str(strFileNameOA)
            strFileDate = str(strAsnFile[:6])
            strFileYear = str(strFileDate[:4] + "-" + strFileDate[4:6])
            if os.path.exists(strFileYear):
                strNewDirPath = os.path.join(strDirectoryOA, strFileYear)
                if strFileNameOA.startswith(strFileDate) and strFileNameOA.endswith(".ASN"):
                    strFilePath = os.path.join(strDirectoryOA, strFileNameOA)
                    shutil.move(strFilePath, strNewDirPath)
            else:
                os.makedirs(strFileYear)
                strNewDirPath = os.path.join(strDirectoryOA, strFileYear)
                if strFileNameOA.startswith(strFileDate) and strFileNameOA.endswith(".ASN"):
                    strFilePath = os.path.join(strDirectoryOA, strFileNameOA)
                    shutil.move(strFilePath, strNewDirPath)

# Module moves Omnicare "Backup-Stat" files ready for archive into an archive folder based on month and year. If specific folder does not exist, will create it.
def ftnFtpBstatArchive():
    strFileNameBStat = str(0)

    strDirectoryBStat = "\\\\charon.pdi.local\\d$\\SFTP\\Omnicare\\BACKUP-STAT\\Archive"
    os.chdir(strDirectoryBStat)

    strFilesBStat = os.listdir(strDirectoryBStat)

    for strFileNameBStat in strFilesBStat:
        print(strFileNameBStat)
        if strFileNameBStat.endswith("PDICC.ASN"):
            strAsnFile = str(strFileNameBStat)
            strFileDate = str(strAsnFile[:6])
            strFileYear = str(strFileDate[:4] + "-" + strFileDate[4:6])
            if os.path.exists(strFileYear):
                strNewDirPath = os.path.join(strDirectoryBStat, strFileYear)
                if strFileNameBStat.startswith(strFileDate) and strFileNameBStat.endswith("PDICC.ASN"):
                    strFilePath = os.path.join(strDirectoryBStat, strFileNameBStat)
                    shutil.move(strFilePath, strNewDirPath)
            else:
                os.makedirs(strFileYear)
                strNewDirPath = os.path.join(strDirectoryBStat, strFileYear)
                if strFileNameBStat.startswith(strFileDate) and strFileNameBStat.endswith("PDICC.ASN"):
                    strFilePath = os.path.join(strDirectoryBStat, strFileNameBStat)
                    shutil.move(strFilePath, strNewDirPath)

# Module moves IDS "hhs" files ready for archive into an archive folder based on month and year. If specific folder does not exist, will create it.
def ftnCvgutils01FtpArchive():
    strFileNameUtils = str(0)

    strDirectoryUtils = "\\\\cvgutils01.pdi.local\\F$\\FTP\\ids\\hhs\\Archive"
    os.chdir(strDirectoryUtils)

    strFilesUtils = os.listdir(strDirectoryUtils)

    for strFileNameUtils in strFilesUtils:
        print(strFileNameUtils)
        if strFileNameUtils.endswith(".txt"):
            strAsnFile = str(strFileNameUtils)
            strFileDate = str(strAsnFile[:16])
            strFileYear = str(strFileDate[12:16] + "-" + strFileDate[8:10])
            if os.path.exists(strFileYear):
                strNewDirPath = os.path.join(strDirectoryUtils, strFileYear)
                if strFileNameUtils.startswith(strFileDate) and strFileNameUtils.endswith(".txt"):
                    strFilePath = os.path.join(strDirectoryUtils, strFileNameUtils)
                    shutil.move(strFilePath, strNewDirPath)
            else:
                os.makedirs(strFileYear)
                strNewDirPath = os.path.join(strDirectoryUtils, strFileYear)
                if strFileNameUtils.startswith(strFileDate) and strFileNameUtils.endswith(".txt"):
                    strFilePath = os.path.join(strDirectoryUtils, strFileNameUtils)
                    shutil.move(strFilePath, strNewDirPath)

# Module moves IDS files ready for archive into an archive folder based on month and year. If specific folder does not exist, will create it.
def ftnCvgutils01FtpArchive1():
    strFileNameUtils = str(0)

    strDirectoryUtils = "\\\\cvgutils01.pdi.local\\F$\\FTP\\ids\\DataDump\\Archive"
    os.chdir(strDirectoryUtils)

    strFilesUtils = os.listdir(strDirectoryUtils)

    for strFileNameUtils in strFilesUtils:
        if strFileNameUtils.endswith(".csv"):
            strFNameU = strFileNameUtils.strip("IDS_priority_detailed_")
            strStripFile = str(strFNameU)
            strFileDate = str(strStripFile[:6])
            strFileYear = str(strFileDate[:4] + "-" + strFileDate[4:6])
            if os.path.exists(strFileYear):
                strNewDirPath = os.path.join(strDirectoryUtils, strFileYear)
                if strFileNameUtils.endswith(".csv"):
                    strFilePath = os.path.join(strDirectoryUtils, strFileNameUtils)
                    shutil.move(strFilePath, strNewDirPath)
            else:
                os.makedirs(strFileYear)
                strNewDirPath = os.path.join(strDirectoryUtils, strFileYear)
                if strFileNameUtils.endswith(".csv"):
                    strFilePath = os.path.join(strDirectoryUtils, strFileNameUtils)
                    shutil.move(strFilePath, strNewDirPath)

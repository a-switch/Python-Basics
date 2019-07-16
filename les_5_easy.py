import os
import sys
import shutil

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

# def makeDirectories():
#     for i in range (1,10):
#         dirName = 'dir_'+str(i)
#         if not os.path.exists(dirName):
#             os.makedirs('dir_'+str(i))

def makeDirectories(dirName):
    if not os.path.exists(dirName):
        os.makedirs(dirName)

# def delDirectories():
#     for i in range (1,10):
#         dirName = 'dir_'+str(i)
#         if os.path.exists(dirName):
#             os.rmdir('dir_'+str(i))

def delDirectories(dirName):
    if os.path.exists(dirName):
        os.rmdir(dirName)

def showDirectories():
    listDir = next(os.walk('.'))[1]
    for i in listDir:
        print(i)

def showDirectories_2():
    listDir = os.listdir()
    for i in listDir:
        if os.path.isdir(i):
            print(i)

def makeCopy():
    fullPath = sys.argv[0]
    curFile = os.path.basename(fullPath)
    newFile = shutil.copy2(os.path.abspath(pathFile), os.path.dirname(os.path.abspath(__file__))+'\\'+'new_' + curFile)
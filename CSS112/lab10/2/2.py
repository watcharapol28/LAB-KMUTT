import sys
import os

os.chdir(r"D:/Programming/Git/CSS112/Python/lab10/2")

try:
    super_dd = open("super_dd.txt", 'a',)
except:
    super_dd = open("super_dd.txt", 'w',)

for i in range(1,4):
    for j in range(1,4):
        nub = 0                 #check how many dd files

        path = r"D:/Programming/Git/CSS112/Python/lab10/2/aa/" + "bb{}/cc{}/".format(i ,j) 

        os.chdir(path)

        for file in os.listdir():

            if file.endswith(".txt"): 
                nub += 1

                file_path = f"{path}\{file}"
                with open(file_path, 'r') as f:
                    
                    super_dd.write("aa/bb{}/cc{}/dd{} : ".format(i,j,nub) + f.read() + "\n")


super_dd.close()





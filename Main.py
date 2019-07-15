from package.write_data_txt import *
import os 
index=0
path_label=[]
path_txt=[]
for name_file in os.listdir("/home/dung/Desktop/label/data"):
    if(name_file.split(".")[1]=="trans"):
        path_txt.append(os.path.join("/home/dung/Desktop/label/data",name_file))
    else:
        path_label.append(os.path.join("/home/dung/Desktop/label/data",name_file))
    index +=1

for number in range(len(path_label)):
    try:
        write_data_txt(path_label[number],path_txt[number])
    except IndexError:
        print("loi")
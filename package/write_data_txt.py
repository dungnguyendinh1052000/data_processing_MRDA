def write_data_txt(path_label,path_txt):
    data_label=open(path_label,"r")
    data_text=open(path_txt,"r")
    label=[]
    for line in data_label.read().split("\n"):
        try:
            label.append(line.split(",")[::-1][5])
        except IndexError:
            print("")
    data_label.close()
    path_file_save="/home/dung/Desktop/label/txt/"+path_label.split("/")[-1].split(".")[0]+".txt"
    fileData=open(path_file_save,"w")
    index=0
    for text in data_text.read().split("\n"):
        try:
            write_text="__"+label[index]+"__"+text.split(",")[1]+"__"+text.split(",")[0].split("_")[0].split("-")[1]+"\n"
            fileData.write(write_text)
            index +=1
        except IndexError:
            print("text")
    fileData.close()
    data_text.close()



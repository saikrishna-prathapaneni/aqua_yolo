import os
import ast


path="C:\\object_yolov3\\data\\valid\\_annotations.txt"
pathtosave="C:/object_yolov3/data/valid/"


def creat_annotations(a,pathtosave):

   with open(pathtosave+a[0][:-3]+'txt','w') as k:

       for i in range(len(a)-1):
        #print(a[i+1].split(','))
        al=a[i+1].split(',')
        al=list(map(int,al))
        al.insert(0,al[-1])
        al=al[:-1]
        al=list(convert_data(al))
        for all in al:
            k.write(str(all)+' ')
        k.write('\n')
def convert_data(llis):
    lab=llis[0]
    x=llis[1]
    y=llis[2]
    w=llis[3]
    h=llis[4]
    x_center = x + y / 2
    y_center = y + h / 2
    x_center=x_center/1024.0
    y_center=y_center/1024.0
    w /= 1024.0
    h /= 1024.0
    return (lab,x_center, y_center, w, h)

with open(path) as f:
    content = f.readlines()
    for line in content:
        new_string = line.split()
        creat_annotations(new_string,pathtosave)
        


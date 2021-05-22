import os
import ast


path="C:\\object_yolov3\\data\\valid\\_annotations.txt"
pathtosave="C:/object_yolov3/data/"


def creat_annotations(a,pathtosave):
     
 with open(pathtosave+'train.txt','w') as k:
            k.write(a[0])
            k.write('\n')        
  
    #print(a[i+1].split(',')
                     # k.write(str(a[i][0]))
                      #k.write('\n')


with open(path) as f:
    content = f.readlines()
    with open(pathtosave+'test.txt','w') as k:
      for line in content:
            new_string = line.split()
        
            k.write('data/fishdata/'+new_string[0])
            k.write('\n')
        #print(new_string[0])
       # creat_annotations(new_string,pathtosave)
        


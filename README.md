1.  Before training the network, create the input, logs, results and img folders, and put the weight file in the model_ Data folder
2. Before training, put the label file in the annotation under voc207 folder under vocdevkit folder。  
3. Before training, put the picture files in jpegimages under voc207 folder under vocdevkit folder。  
4. Before training, use the voc2yolo4.py file to generate the corresponding TXT。  
5. Before training, use the voc2yolo4.py file to generate the corresponding TXT, and then run VOC in the root directory_ Annotation.py, you need to change your classes to your own before running** Be careful not to use Chinese labels, and there should be no spaces in the folder**   
```python
classes = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]
```
6. The corresponding 2007 is generated_ Train.txt, each line corresponds to its * * picture position * * and its * * real box position**。  
7.**Before training, you must be in the model_ Create a new TXT document under data, enter the classes to be divided in the document, and set the classes in train.py_ Path points to the file * *. An example is shown below：   
```python
classes_path = 'model_data/new_classes.txt'    
```
model_data/new_classes.txt：   
```python
cat
dog
...
```
8. Run train.py to start training。
9. Put the picture to be predicted in img folder (the picture size should be consistent)
10. Run change_ im_ Name
11. Run the predict file or predict2 file to predict the seed setting rate of rice, and select predict or predict2 according to the size of the picture
12. Training set, test set and weight file
**link：https://pan.baidu.com/s/1boB-hAusrJ_geebViThrgw 
**Extraction code：dutm
13. ## Reference
14. https://github.com/bubbliiiing/yolov4-pytorch

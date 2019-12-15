# FTree
Frame Tree to make image processing easier. 


### Proposed interaction

```python
import cv2
import face_detection
import FTree.Frame

img = cv2.imread("abc")

master_frame = Frame(img)
bboxes = face_detection.find_people(master_frame.arr)

human_sub_frames = map(lambda bbox: master_frame.crop(bbox), bboxes)

all_faces = []
for human_frame in human_sub_frames""
    all_faces += [*map(lambda x:  human_frame.crop(x) ,face_recognition.find_faces(human_frame))
    
for face in all_faces:
    get_parent



```


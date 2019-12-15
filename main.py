import numpy as np
import imutils
from typing import Tuple, List
class Frame:
    def __init__(self,
                 arr:np.array,
                 dx = 0,
                 dy = 0,
                 sx = 1,
                 sy = 1,
                 level = 0):

        self.frame_array = arr
        h,w,z = arr.shape

        self.width = w
        self.height = h

        ## Offset from parent (if a parent exists)
        self.dx = dx
        self.dy = dy

        ## Multipliers in scale from the parent object
        self.sx = sx
        self.sy = sy

        self.parent = None
        self.root   = self

        self.level = level

    def crop(self, x:int,y:int,w:int,h:int) -> "Frame":
        new_arr = self.frame_array[y:y+h, x:x+w,:]
        sub_frame =  Frame(new_arr,
                        dx = x,
                        dy = y,
                        level= self.level + 1)

        sub_frame.parent = self
        sub_frame.root = self.root

        return sub_frame

    def down_scale_height(self, scale:float = 1.0) -> "Frame":

        if scale > 1:
            raise Exception("Scale should be <= 1")

        array_height,array_width, _ = self.frame_array.shape
        new_arr = imutils.resize(self.frame_array, height= int(scale **array_height))

        new_height, new_width, _ = new_arr.shape
        sub_frame =  Frame(new_arr,
                        sx = new_width/array_width,
                        sy = new_height/array_height,
                        level= self.level + 1)

        sub_frame.parent = self
        sub_frame.root   = self.root


    def bbox_relative_to_root(self) -> Tuple[int,int,int,int]:
        y,x   = (0,0)
        h,w,_ = self.frame_array.shape

        subject = self

        while subject.level > 0:
            dx = subject.dx
            dy = subject.dy

            x += dx
            y += dy

            sx = subject.sx
            sy = subject.sy

            x = int(x * (1/sx))
            y = int(y * (1/sy))

            subject = subject.parent
        return





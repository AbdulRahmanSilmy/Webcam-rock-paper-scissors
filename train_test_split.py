#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class train_test_split():
    
    def __init__(self,ratio,XML_present=True):
        self.ratio=ratio #decimal percentage of train samples
        self.XML_present=XML_present #set the condition for xml files
        
    def split(self,labels,sourcepaths,destpaths):
        self.labels=labels
        self.sourcepaths=sourcepaths
        self.destpaths=destpaths
        #sourcedir array containing the source directeries 
        #destdir is the destination directory
        
        assert type(labels)==list,'labels must be a list'
        assert type(destpaths)==list,'destpaths must be a list'
        
        self.destination_creator()
      
        for label in self.labels:
            self.filename_divisor(label)
        print('done...')
   
        
    def filename_divisor(self,label):
        import os,shutil
        import numpy
        from os import walk
        import math
        import random
        mypath= os.path.join(self.sourcepaths,label)
        filenames = next(walk(mypath), (None, None, []))[2]
        if self.XML_present:
            filenames=numpy.array(filenames).reshape(5,2)
        else:
            filenames=numpy.reshape(filenames,(len(filenames),1))
        len_list=len(filenames)
        num_train=math.floor(self.ratio*len_list)
        random_list=random.sample(range(len_list), len_list)
        train_list,test_list=random_list[:num_train],random_list[num_train:]
        train_names=filenames[train_list]
        test_names=filenames[test_list]
        
        for item in train_names:
            
            dest_path0=os.path.join(self.destpaths[0],item[0])
            if not os.path.exists(dest_path0):
                temp_path0=os.path.join(mypath,item[0])
                shutil.copyfile(temp_path0, dest_path0)
            
            if self.XML_present:
                dest_path1=os.path.join(self.destpaths[0],item[1])
                if not os.path.exists(dest_path1):
                    temp_path1=os.path.join(mypath,item[1])
                    shutil.copyfile(temp_path1, dest_path1)
            
        for item in test_names:
            
            dest_path0=os.path.join(self.destpaths[1],item[0])
            if not os.path.exists(dest_path0):
                temp_path0=os.path.join(mypath,item[0])
                shutil.copyfile(temp_path0, dest_path0)
            
            if self.XML_present:
                dest_path1=os.path.join(self.destpaths[1],item[1])
                if not os.path.exists(dest_path1):
                    temp_path1=os.path.join(mypath,item[1])
                    shutil.copyfile(temp_path1, dest_path1)
                
        print(f'transferred {label} files to destination paths..')
            
    def destination_creator(self):
        import os
        import shutil
        import glob

        for destpath in self.destpaths:
            if os.path.exists(destpath):
                files = glob.glob(destpath+'/*')
                for f in files:
                    os.remove(f)
                print('removing existing destpath files...')
            else:
                os.mkdir(destpath)
        print('created destination folders...')
                
       


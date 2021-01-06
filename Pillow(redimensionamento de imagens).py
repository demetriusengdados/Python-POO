#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os 
from PIL import Image


# In[5]:


def main(main_images_folder):
    if not os.path.isdir(main_images_folder):
        raise NotADirectoryError(f'{main_images_folder} não existe')
        
    for root, dirs, files in os.walk(main_images_folder):
        for file in files:
            file_full_path = os.path.join(root, file)
            file_name, extension = os.path.splitext(file)
            new_file = file_name + '_CONVERTED' + extension
            print(new_file)
        
if __name__ == '__main__':
    main_images_folder = '/home/demetrius/Imagens/Videos'
    main(main_images_folder)


# In[ ]:





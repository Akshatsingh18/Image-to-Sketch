#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[2]:


#read the image location and image file name

img_location = "zatch.jpg"


# ## READ THE IMAGE FROM THE LOCATION

# In[3]:


img = cv2.imread(img_location)

#DISLPLAY ORIGNAL IMAGE

cv2.imshow('original image' , img)
cv2.waitKey(0)


# ## CONVERT ORIGINAL IMAGE TO GRAY IMAGE

# In[4]:


gray_image = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)


# ## CONVERT GRAY TO BLUR IMAGE

# In[5]:


blurred_image = cv2.GaussianBlur(gray_image, (21,21) , 0)


# ## CONVERT BLUR IMAGE TO PENCIL SKETCH

# In[6]:


pencil_sketch = cv2.divide(gray_image , blurred_image , scale = 256.0)

#DISPLAY PENCIL SKETCH OF THE ORIGIAL IMAGE

cv2.imshow('PENCIL SKETCH' , pencil_sketch)
cv2.waitKey(0)


# In[ ]:





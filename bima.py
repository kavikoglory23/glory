#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
st.header("'sample web app'")
st.write("'my app'")
celcius=st.slider('val')
st.write(celcius,"fahrenheit",(celcius*9/5)+32)


# In[ ]:





# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IHIQOohXR_5xkUAct9ITYiF6KrrFQMu6
"""

import numpy as np
import pandas as pd 
import streamlit as st

def main():
  st.title("SUM OF TWO NUMBERS")
  html_temp ="""
  <div style="background-color:black;padding:10px">
  <h2 style="color:black;text-align:centre;"> Addition of two numbers</h2>
  </div>
  """
  st.markdown(html_temp,unsafe_allow_html=True)
  num1=st.number_input("Number 1")
  num2=st.number_input("Number 2")
  result=num1+num2
  st.success('The output is {}'.format(result))
if __name__=='__main__':
  main()
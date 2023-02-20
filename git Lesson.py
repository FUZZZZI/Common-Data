# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 01:03:58 2023

@author: lalwa
"""

#conda install -c anaconda git  #installed in conda
!git init
!git version
!git config -h
!git clone https://github.com/FUZZZZI/Flas_app1.git

ls
cd Flas_app1/  #set cd
ls

!git init
!git add .          #add entire code to local github
!git commit -m "this is flas1 code" #give email and userid to push added code to new github repository
!git config --global user.email "lalwanisaurbh9@gmail.com"
!git config --global user.name "FUZZZZI"
!git branch -M main
!git remote add origin https://github.com/FUZZZZI/Flask2.git
# error: error: remote origin already exists.
!git remote remove origin
!git remote add origin https://github.com/FUZZZZI/Flask2.git
!git push -u origin main
#Authetication
#Result: All files/folders copied from Flas_app1 (already cloned to wd) to Flask2 repository
---
title: FastAI Flower Classif
emoji: ⚡
colorFrom: blue
colorTo: yellow
sdk: gradio
sdk_version: 3.39.0
app_file: app.py
pinned: false
license: apache-2.0
---


# *fastAI* to make a Flower Classifier


Do you like gardening? Would you like to know more about flowers?

If so, then this project is for you. In this project, I have built a flower classifier that can identify over 100 different species of flowers. The classifier is trained on a dataset of over 10,000 flower images, and it can classify flowers with an accuracy of over 95%.

## Project Objective


The purpose of this project is to create a machine learning model that can (_almost_) any common flower. This model could be used to help people identify flowers in the wild, which can be useful for a variety of purposes, such as wildlife conservation, gardening, and education.

__Methods used:__
 - Deep Learning
 - Python
 - Hugging face Spaces
 - Git
 - fastAI 
 - Jupyter Lab
 




# Getting started

<script
	type="module"
	src="https://gradio.s3-us-west-2.amazonaws.com/3.39.0/gradio.js"
></script>

<gradio-app src="https://mateocontreras-fastai-flower-classif.hf.space"></gradio-app>

# Data
The data used to train this model was the Oxford 102 Flower Dataset: https://www.robots.ox.ac.uk/~vgg/data/flowers/102/. This dataset contains 102 flower categories, with a total of 8189 images. 

The data was split into a training set of 6149 images, a validation set of 1020 images, and a test set of 1020 images. The training set was used to train the model, the validation set was used to evaluate the model's performance, and the test set was used to test the model's performance on unseen data.

The data was preprocessed to resize the images to 224x224 pixels and normalize the pixel values.


## Badges


[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)



# Draw, Detect, Navigate

## Team 4 AAI-590: Capstone Project

**-- Project Status: Active**

## Project Intro/Objective

This project creates and uses synthetically generated data comprised of drawings from the Quick, Draw! dataset identify not only the class of the doodle, but also the bounding box. A subset of 12 classes from the original data is used. An original convolutional neural network was used, as well as fine-tuned editions of Pytorch's Faster R-CNN and Ultralytics YOLOv8 models were explored and evaluated, with YOLOv8 selected due to its real time usage capabilities and support in the Sentis package of the Unity game engine. The exported model is included in a desktop application built with Unity using webcam data to detect and classify pictograms, place augmented reality 3d models of pictograms through the use of Aruco anchors through OpenCV, space is decomposed into a connected grid of nodes, and A* pathfinding is used to navigate the optimal path from the most recent detected helicopter to the most recent detected hospital.

### Goals:

- Determine feasibility drawing bounding box detection and classification with models suitable for real-time use and AR applications
- Adapt data as needed for detection of multiple drawings per image with bounding boxes
- Verify results on real world data with imperfect camera angles, lighting, line thickness, etcetera
- Determine optimal approaches
- Combine best-performing model with augmented reality technologies to combine 2D and 3D data, placing 3D models over drawings
- Use A* to determine optimal paths from start (helicopter) to destination (hospital) routing aroudn obstacles, all placed by drawings to demonstrate an example of more complex interactions facilitated by the the combination of imagle classification, image spatial relationships, and augmented reality


### Partner(s)/Contributor(s)
   - **Elan Wilkinson**
   - **Dominic Fanucchi**
   - **Gabriel Emanuel Colón**
   - **Parker Christenson**

![Live Use](materials/drawDetectNav.gif)

 **Programming Languages:** 
- Python
- C#

 **Models and Libraries:** 
  - Model Types Used: CNN, FASTER R-CNN, YOLO
  - Libraries: Numpy, Pandas, PyTorch, MatPlotLib, Ultralytics, AST, Albumentations, Torchvision, SKLearn

## Installation
To use this project, first clone the repo on your device using the command below:
```bash
git init
git clone https://github.com/dominicfanucchi/aai-590_group4.git
```

## About the Dataset
Early models trained directly on raw and augmented images from the *Quick, Draw!* dataset from Google Creative Lab.

## Approach
The specific algorithms and networks used were as follows: 


These algorithms and networks were implemented through Python, Jupyter Notebooks.

### Imports and Libraries
The project relies on the following libraries and packages:
* `os` - Provides a way of using operating system-dependent functionality.
* `warnings` - Provides a way to issue warnings and control their behavior.
* `numpy` - Fundamental package for numerical computations in Python.
* `pandas` - Data manipulation and analysis library.
* `matplotlib.pyplot` - Plotting library for creating static, interactive, and animated visualizations.
* `seaborn` - Statistical data visualization library based on Matplotlib.
* `%matplotlib inline` - Jupyter magic command for displaying plots inline within Jupyter notebooks.

## Results

The results of the project were evaluated based on the following metrics:
* **Accuracy** - The proportion of true results (both true positives and true negatives) among the total number of cases examined.
* **Precision** - The ratio of correctly predicted positive observations to the total predicted positives.
* **Recall** - The ratio of correctly predicted positive observations to all actual positives.
* **Ability to detect multiple objects** - The model's capability to identify and classify multiple objects within a single image.
* **Speed** - The time taken for the model to process an image and make predictions, which is crucial for real-time applications.
* **mAP@0.5** - Mean Average Precision at IoU threshold of 0.5, a common evaluation metric for object detection tasks.
* **mAP@0.5:0.95** - Mean Average Precision at IoU thresholds ranging from 0.5 to 0.95, providing a more comprehensive evaluation of the model's performance across different levels of overlap between predicted and ground truth bounding boxes.
* **Training Time** - The time taken to train the model on the dataset, which can impact the feasibility of deploying the model in real-world applications.


The results of the two models YOLO detection and classification models that were developed using the *Quick, Draw!* dataset foundations, and Augmented data by combining multiple images into one, are as follows: 


### `YOLOv8N` - Yolov8 Nano

**Training Info**
- **Epochs**: 25  
- **Training Time**: ~0.75 hours  
- **Model Weights**:  
  - [`best.pt`](runs/detect/train4/weights/best.pt) – 6.3MB  
  - [`last.pt`](runs/detect/train4/weights/last.pt) – 6.3MB  
-  **Framework**: [Ultralytics YOLOv8 (v8.3.107)](https://github.com/ultralytics/ultralytics)  
- **Environment**: Python 3.9.21, PyTorch 2.6.0+cu118, CUDA: NVIDIA RTX 2060 (6GB)



#### Validation Metrics

| Class         | Precision | Recall | mAP@0.5 | mAP@0.5:0.95 |
|---------------|-----------|--------|--------|--------------|
| **All**       | 0.938     | 0.944  | 0.978  | 0.968        |
| campfire      | 0.960     | 0.974  | 0.987  | 0.977        |
| cloud         | 0.960     | 0.965  | 0.990  | 0.989        |
| firetruck     | 0.843     | 0.870  | 0.931  | 0.925        |
| helicopter    | 0.939     | 0.974  | 0.990  | 0.977        |
| hospital      | 0.956     | 0.945  | 0.983  | 0.975        |
| mountain      | 0.977     | 0.976  | 0.992  | 0.983        |
| skull         | 0.982     | 0.967  | 0.993  | 0.991        |
| skyscraper    | 0.963     | 0.947  | 0.980  | 0.951        |
| tractor       | 0.927     | 0.906  | 0.975  | 0.971        |
| traffic light | 0.949     | 0.972  | 0.992  | 0.967        |
| tree          | 0.953     | 0.973  | 0.992  | 0.982        |
| van           | 0.848     | 0.855  | 0.932  | 0.929        |



#### Speed (per image)

| Step         | Time (ms) |
|--------------|-----------|
| Preprocess   | 0.6       |
| Inference    | 2.4       |
| Postprocess  | 0.6       |
| Loss         | ≈0        |


### `YOLOv8S` - Yolov8 Small

**Training Info**
- **Epochs**: 25  
- **Training Time**: ~1.39 hours  
- **Model Weights**:  
  - [`best.pt`](runs/detect/train6/weights/best.pt) – 22.5MB  
  - [`last.pt`](runs/detect/train6/weights/last.pt) – 22.5MB  
-  **Framework**: [Ultralytics YOLOv8 (v8.3.107)](https://github.com/ultralytics/ultralytics)  
- **Environment**: Python 3.9.21, PyTorch 2.6.0+cu118, CUDA: NVIDIA RTX 2060 (6GB)



#### Validation Metrics

| Class         | Precision | Recall | mAP@0.5 | mAP@0.5:0.95 |
|---------------|-----------|--------|--------|--------------|
| **All**       | 0.956     | 0.961  | 0.986  | 0.978        |
| campfire      | 0.946     | 0.988  | 0.994  | 0.985        |
| cloud         | 0.971     | 0.987  | 0.994  | 0.993        |
| firetruck     | 0.872     | 0.887  | 0.955  | 0.947        |
| helicopter    | 0.981     | 0.974  | 0.994  | 0.980        |
| hospital      | 0.980     | 0.960  | 0.993  | 0.988        |
| mountain      | 0.978     | 0.987  | 0.994  | 0.987        |
| skull         | 0.987     | 0.992  | 0.995  | 0.993        |
| skyscraper    | 0.969     | 0.966  | 0.991  | 0.972        |
| tractor       | 0.949     | 0.929  | 0.982  | 0.977        |
| traffic light | 0.978     | 0.983  | 0.994  | 0.977        |
| tree          | 0.979     | 0.990  | 0.994  | 0.984        |
| van           | 0.885     | 0.887  | 0.950  | 0.947        |



#### Speed (per image)

| Step         | Time (ms) |
|--------------|-----------|
| Preprocess   | 0.6       |
| Inference    | 5.9       |
| Postprocess  | 0.4       |
| Loss         | ≈0        |




## References



## Acknowledgments
Our thanks and appreciation go to our professor **Roozbeh Sadeghian**  and to **Google Creative Lab** for the use of the *Quick, Draw!* dataset.

## License
This dataset is licensed under a [CC0 1.0 DEED license](https://creativecommons.org/publicdomain/zero/1.0/legalcode.en) - see the [Creative Commons](https://creativecommons.org/publicdomain/zero/1.0/legalcode.en) website for details.

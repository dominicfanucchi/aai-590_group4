# Draw, Detect, Navigate
# MSAAI Capstone Project
This project is a part of the AAI-590 course in the Applied Artificial Intelligence Program at the University of San Diego (USD).

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


- ### Partner(s)/Contributor(s)
   * Elan Wilkinson
   * Dominic Fanucchi
   * Gabriel Emanuel Colón
   * Parker Christenson

![Live Use](materials/drawDetectNav.gif)

## Installation
To use this project, first clone the repo on your device using the command below:
```bash
git init
git clone https://github.com/dominicfanucchi/aai-590_group4.git
```

## Project Objective

## About the Dataset

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

## References

## Acknowledgments
We would like to express our sincere gratitude to... 

## License
This dataset is licensed under a [CC0 1.0 DEED license](https://creativecommons.org/publicdomain/zero/1.0/legalcode.en) - see the [Creative Commons](https://creativecommons.org/publicdomain/zero/1.0/legalcode.en) website for details.

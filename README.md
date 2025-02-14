# **Structure_from_Motion**
Created by Ayeda Sayeed (sayeayed@gmail.com)
***
Attempted implementation and custom library for SfM

## **Summary**
This repository containts a first attempt at completing a SfM module, using images from http://phototour.cs.washington.edu/datasets/, of the Notre Dame cathedral. It also contains the beginnings of a custom Python package (library) to implement SfM from a similar dataset.
As time goes on, this repository will be updated to improve the SfM implementation and complete the package. 

## Disclaimer
I have no prior experience with SfM, so hold on because it's going to be a bumpy ride!

## **Dependencies**
To run the files in this repository, the following libraries/packages must be installed:
- `numpy`
- `os`
- `cv2`
- `matplotlib`*
- `mpl_toolkits`*

Notes: 
- 'In order to run the test code, `SfM_test.py` you must copy the "images" folder from the original dataset at http://phototour.cs.washington.edu/datasets/ into NotreDame/NotreDame/ in the working directory
- 'Lines 5 and 6 of `SfM_test.py` can be commented out to avoid missing dependencies of non-standard libraries denoted by the asterisk, which are only used for plotting purposes

## **File descriptions**
Files "for submission" are:
- `SfMlib/mySfM.py`
- `SfM_test.py` (not to be confused with `SfM_Test.ipynb` which is a Jupyter notebook that was used for compiling and testing)

### `mySfM.py`
This Python script is a module in the package (or library) that can be imported into any other script to implement SfM. As of now, it is unpopulated, with only placeholder definitions for classes and methods that would be used in SfM algorithms. If other modules should be needed, they will be added to the package `SfMlib`. 

### `SfM_test.py`
This script is not the required test program, but rather my proving grounds for attempting the SfM algorithms before building the package. The bulk of it attempts to parse the data from the dataset; loading images, and reading relevant data from the output file that was previously generated by Bundler. Since I am unfamiliar with SfM theory, I was unable to properly understand the instructions regarding the library inputs: "images, point correspondences, and the camera matrix". From my meager understanding, it seemed that if I had the point correspondences, I would not need the images as well, but if I had only the images I could implement the full SfM procedure to generate the point correspondences. In this confusion, I had decided to extract the point correspondences from the Bundler output file, which, theoretically, is half of the work of an SfM algorithm. 

Since I was unable to complete the project, this file contains some comments regarding the procedures I would follow regarding next steps.

Most of the code in this file would be redistributed to the `mySfM.py` package, when the final implementation has been determined. For now, it remains as a single script, sans proper objects, to allow for further modifications. 

## Next Steps
With more time, I would complete the SfM implementation and library. There are two paths ahead of me:
1. To complete the project using my current assumptions around the library inputs
2. To complete the project with full SfM capability
Path 1 involves immediate next steps, whereas path 2 would follow after path 1 and requires a great deal more time

### Immediate next steps
- correct data parsing
- extract and assign matched point correspondences
- calculate true camera projection matrices in order to
- triangulate 3D points from the matched point correspondences
- generate simple 3D scatter plot of reconstructed points (currently, the coordinate space seems wrong)
- generate a PLY or PCD file of the reconstructed points

### Future steps
- implement feature detection for any dataset of images
- implement feature matching between two images
- implement point correspondence (select matched points)
- estimate camera pose of second view relative to first view
- update view set
- compute camera pose in global coordinate system
- triangulate 3D points
- bundle adjustment to refine camera poses and 3D points
- reiterate, using dense reconstruction

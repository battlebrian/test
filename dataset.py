import numpy as np
import os
import cv2
def loadImages(dataPath):
    """
    load all Images in the folder and transfer a list of tuples. The first 
    element is the numpy array of shape (m, n) representing the image. 
    The second element is its classification (1 or 0)
      Parameters:
        dataPath: The folder path.
      Returns:
        dataset: The list of tuples.
    """
    # Begin your code (Part 1)
    # raise NotImplementedError("To be implemented")
    dataset = []
    faceDataPath = dataPath + '/face'
    for filename in os.listdir(faceDataPath):
        img = cv2.imread(os.path.join(faceDataPath,filename), cv2.IMREAD_GRAYSCALE)
        if img is not None:
            dataset.append((img, 1))
    nonFaceDataPath = dataPath + '/non-face'
    for filename in os.listdir(nonFaceDataPath):
        img = cv2.imread(os.path.join(nonFaceDataPath,filename), cv2.IMREAD_GRAYSCALE)
        if img is not None:
            dataset.append((img, 0))
    # End your code (Part 1)
    return dataset
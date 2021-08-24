# Breast Cancer Causality_Challenge

The causal graph is a central object in a framework developed by Judea Pearl and his research group, but it is often unknown, subject to personal knowledge and bias, or loosely connected to the available data. The main objective of the task is to highlight the importance of the matter in a concrete way. In this spirit, the tasks of this challenge include:

1.	Perform a causal inference task using Pearl’s framework;
2.	Infer the causal graph from observational data and then validate the graph;
3.	Merge machine learning with causal inference

* The features of the data are computed from a digitized image of a fine needle aspirate (FNA) of a breast mass. They describe characteristics of the cell nuclei present in the image.

<h2>Data Attributes</h2>

* ID number
* Diagnosis (M = malignant, B = benign)

**Ten real-valued features are computed for each cell nucleus:**

* radius (mean of distances from center to points on the perimeter)
* texture (standard deviation of gray-scale values)
* perimeter
* area
* smoothness (local variation in radius lengths)
* compactness (perimeter^2 / area - 1.0)
* concavity (severity of concave portions of the contour)
* concave points (number of concave portions of the contour)
* symmetry
* fractal dimension ("coastline approximation" - 1)

The mean, standard error and "worst" or largest (mean of the three largest values) of these features were computed for each image

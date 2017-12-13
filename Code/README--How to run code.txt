1. FP-Growth
	The FP Growth can be run through a weka explorer, using the provided med.arff file. 
	The confidence used for the FP Growth algorithm is 0.1.

2. KMeans 
	Open the provided iPython Notebook called 'diabetes'.
	The filepath should already lead to the diabetes dataset kept within the 'Dataset' folder.
	Click on 'Kernel' and choose the option to 'Restart & Run All'.

3. Logistic Regression
	The file called 'PCA on diabetes dataset' consists of the updated logistic regression model, which was
	retrained on the data after PCA was added and found to improve the model's accuracy. 
	Click on 'Kernel' and choose the option to 'Restart & Run All'. 

	The file called 'PCA on diabetes dataset updated' is the results after apply PCA to the dataset. 
	Click on 'Kernel' and choose the option to 'Restart & Run All'. 

	The file called 'Readmission Prediction Model' is the results of the logistic model before it was retrained
	on the data produced by PCA.
	Click on 'Kernel' and choose the option to 'Restart & Run All' in order to reproduce results.
	
4. Preprocessing
	The file 'csv2arff.py' was used to convert the given dataset to ARFF format for weka purposes.
	Run from command line and the program takes as argument the file path of the dataset, and produces the ARFF file within the same folder.

	The file 'csv2arff_shrink-icd9.py' also takes the datasets file path as an argument in order to run it. It groups the 
	diagnoses by which body system they affect and produces the ARFF file of the result.

	The file 'flatten' does a manual one-hot encoding on all of our categorical data, producing a file 'flattened.csv'after 
	being run from command line with no arguments.

5. RandomForest and SVD
	The file named 'Applying SVD' shows the results of the application of SVD on the diabetic dataset.
	The filepath should already lead to the diabetes dataset within the 'Dataset' folder. 
	Click on 'Kernel' and choose the option to 'Restart & Run All' in order to reproduce results.
	
	The file named 'Random Forest' shows the results of applying a Randmon Forest Classifier model on the dataset.
	The filepath should already lead to the diabetes dataset within the 'Dataset' folder. 
	Click on 'Kernel' and choose the option to 'Restart & Run All' in order to reproduce results.
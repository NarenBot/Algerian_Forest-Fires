<div id="top"></div>

## Algerian_Forest-Fires:
### Deployed App--
[![Algerian_Wild-Fires](https://user-images.githubusercontent.com/58779483/183146427-bdc8e223-d5b9-4123-8375-902f1c197106.jpg)](http://algerian-wildfires.herokuapp.com/)

[LINK TO HEROKU APP](http://algerian-wildfires.herokuapp.com/)

## About The Project:
The dataset includes 244 instances that regroup a data of two regions of Algeria, namely the Bejaia region located in the northeast of Algeria and the Sidi Bel-abbes region located in the northwest of Algeria.

<p align="right">(<a href="#top">back to top</a>)</p> 

### Steps Taken:
* Installed Python, VS Code and Git.
* Created an account on Atlas MongoDB.
* Download the source dataset from [UCI Repository](https://archive.ics.uci.edu/ml/datasets/Algerian+Forest+Fires+Dataset++#).
* For Classification algorithm decided to predict the features `Classes` from the dataset which is Binary classification `(fire, not fire)`.
* For Regression Problem algorithm decided to predict the feature `FWI` (Fire weather Index) which is 90% correlated to Classes Feature.
* Deployed on Heroku app.

### Data Cleaning:
* Data was cleaned which has an header issue, missing values, misplaced values and outliers.

### EDA and Feature Engineering:
* In this step, we will apply Exploratory Data Analysis (EDA) to extract insights from the data set to know which features have contributed more in predicting Forest fire by performing Data Analysis using Pandas and Data visualization using Matplotlib & Seaborn.
* Done Feature scaling by Standard Scaler in which data lies between -1 and +1.

### Model Building 
* For Regression Problem algorithm decided to predict the feature `FWI` (Fire weather Index) which is 90%+ correlated to Classes Feature.
* Models used : **Linear regression, Lasso Regression, Ridge Regression, Random forest, Decision tree, K-Nearest Neighbour regressor, Support Vector Regressor.**
* For Classification algorithm decided to predict the features `Classes` from the dataset which is Binary classification `(fire, not fire)`.
* Models used : **Logistic Regression, Decision Tree, Random Forest, XGboost, K-Nearest Neighbour, Support Vector Classifier.**

<p align="right">(<a href="#top">back to top</a>)</p> 

### Model Selection
* HyperParameter Tuning with Gridsearch CV is done for both Regression and Classification.
* For Classification: Metrics are accuracy score, confusion matrix and classification report.
* For Regression: Metrics are r2 score, adjusted r2 and mean absolute error.

### Single and Batch Prediction:
* For single prediction, user can enter the values on UI.
* For batch prediction, it will select random number of records from mongodb.

### Flask, Docker and  Heroku Deployment:
* Build a Flask App with Docker file.
* Deployed on Heroku with CI/CD pipeline through Github actions.

<p align="right">(<a href="#top">back to top</a>)</p> 

### **Technologies used**
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)


### **Tools used**
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)

## Contact
[![Narendran Mudadi|LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)][reach_linkedin]
[![Narendran Mudadi|G-Mail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)][reach_gmail]

<p align="right">(<a href="#top">back to top</a>)</p> 


<!-- Reach Contact -->
[reach_linkedin]: https://www.linkedin.com/in/narendran-mudadi/
[reach_gmail]: mailto:narendas10@gmail.com?subject=Github



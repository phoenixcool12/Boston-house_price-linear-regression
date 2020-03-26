# Boston-house_price-linear-regression
This is a linear regression model that trains the model to predict possible house prices based on the features of each dataset.
The dataset used here is boston dataset which is loaded in scikit library.
Explaination of the code:
First we import the required libraries which will be used to train the dataset next we load our dataset from scikit library.
Next we store all the feature in df_x variable and the price in the variable df_y.
Using the train_test_split we divide our training and testing data for the model I have used 0.33 of the data for testing rest is used to train the model.
Fit the training data and then store the predictions on test data in another variable.
To find the accuracy we can import mean squared error in scikit learn, I have obtained an error of 20.72 in this model.

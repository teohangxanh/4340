import numpy as np
import pandas as pd

df = pd.read_csv("data.csv")
x = df.drop(df.columns[[0, 1, 3, 4, 5, 8, 9, 18, 19, 20, 21, 22, 23, 24, 25, 26]], axis=1)

# Drop all rows having at least one missing value
x.dropna(how='any', inplace=True)

# Turn values, wages, and release clauses of tring to float16
signs = '|'.join(['€', 'M', 'K'])
x['Value'] = x['Value'].str.replace(signs, '')
x['Wage'] = x['Wage'].str.replace(signs, '')
x['Release Clause'] = x['Release Clause'].str.replace(signs, '')
x = x.rename(columns={'Wage': 'Wage_in_K', 'Value': 'Value_in_M', 'Release Clause': 'Release_clause_in_M'})
x['Work Rate'] = x['Work Rate'].replace(['Low/ Low', 'Low/ Medium', 'Low/ High','Medium/ Low', 'Medium/ Medium', 'Medium/ High',
                              'High/ Low', 'High/ Medium', 'High/ High'], 
                              ['2', '3', '4', '3', '4', '5', '4', '5', '6'])
x = x.astype({'Age': 'int8', 'Overall': 'int8', 'Special': 'int16', 'Work Rate': 'int8', 'Wage_in_K': 'float16', 'Value_in_M': 'float16', 'Release_clause_in_M': 'float16'})

# Turn Preferred Foot into 0 and 1
x = pd.get_dummies(x, columns=['Preferred Foot'], drop_first=True)
# Turn Preferred Foot_Right into int
x['Preferred Foot_Right'] = x['Preferred Foot_Right'].astype('int8')

# Handle "+" from column LS:RB
for val in x.loc[:, 'LS':'RB']:
    # Split into two columns without plus and turn them into float16 type
    x[val + '_' + str(0)] = x[val].str.split('+', expand=True)[0].astype('float16')
    x[val + '_' + str(1)] = x[val].str.split('+', expand=True)[1].astype('float16')
    # Add the value of the newly splited columns to a new one
    x[val] = x[val + '_' + str(0)] + x[val + '_' + str(1)]
    
# Drop the newly splited columns
col_del_from = x.columns.get_loc('LS_0')
col_del_to = x.columns.get_loc('RB_1')
x.drop(x.columns[col_del_from: col_del_to + 1], axis=1, inplace=True)

# Add series y, which is the target for the predicting model
y = x.loc[:, 'Value_in_M']
# Drop column 
x.drop(columns = 'Value_in_M', axis=1)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

# Splitting the data into training and testing set and making predictions
from sklearn.linear_model import LinearRegression 
lm = LinearRegression() 
lm.fit(x_train, y_train) 
y_pred = lm.predict(x_test)

# Find mean squared errors of the predicting and real values
from sklearn.metrics import mean_squared_error
print(mean_squared_error(y_test, y_pred, squared = True))

# Find out how each variable impacts on the value of soccer players
import statsmodels.api as sm
x = np.append(arr = np.ones((len(x), 1)).astype(int), values = x, axis = 1)

# This function is to eleminate columns in x having p-values > significance level
def backwardElimination(x, sl):
    numVars = len(x[0])
    for i in range(0, numVars):
        regressor_OLS = sm.OLS(y, x).fit()
        maxVar = max(regressor_OLS.pvalues)
        if maxVar > sl:
            for j in range(0, numVars - i):
                if regressor_OLS.pvalues[j] == maxVar:
                    x = np.delete(x, j, 1)
    regressor_OLS.summary()
    return x

sl = 0.05
x_opt = x[:, :]
x_Modeled = backwardElimination(x_opt, sl)










# PRODIGY_DS_02


This project involved performing data cleaning and exploratory data analysis (EDA) on the Titanic dataset. The primary goal was to explore relationships between variables, identify patterns and trends, and derive meaningful insights from the data.

#**Key Steps**

##**Data Loading:** Imported the dataset into a Pandas DataFrame.

##**Data Assessment:** Checked the dataset's shape, first few rows, and summary statistics.

##**Missing Data Handling:**
Dropped the Cabin column due to extensive missing values.
Filled missing values in the Age column with the mean age.
Filled missing values in the Embarked column with the most frequent value ('S').

##**Data Type Conversion:** Converted appropriate columns to categorical data types.

##**Visualization and Analysis:**
Visualized survival rates across different passenger classes and embarkation points.
Analyzed age and fare distributions.
Created various plots to uncover patterns and trends.

##**Tools and Libraries**
Pandas: For data manipulation and analysis.
Seaborn and Matplotlib: For data visualization.

#**Key Insights**

##**Gender and Survival:** Survival rates were higher among female passengers compared to male passengers.

##**Passenger Class:** 3rd class was the deadliest, while first-class passengers had higher survival counts. The majority of passengers belonged to the 3rd class

##**Family Size:** People with smaller families had more chances of survival compared to large families.

##**Fare Distribution:**
The fare distribution was right-skewed, with most passengers paying lower fares.

##**Embarkation Points:**
Most passengers embarked from Southampton ('S'), followed by Cherbourg ('C'), and Queenstown ('Q').
Passengers from Cherbourg had a higher survival rate.

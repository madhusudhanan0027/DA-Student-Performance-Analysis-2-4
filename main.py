import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("student_data.csv")

print("Dataset Preview:")
print(data.head())

# Rename columns (important for Kaggle dataset)
data.rename(columns={
    'G1': 'Internal_Marks',
    'G2': 'Assignment_Score',
    'G3': 'Final_Grade'
}, inplace=True)

# Descriptive Statistics
print("\nStatistics:")
print(data.describe())

# Correlation
print("\nCorrelation:")
print(data.corr(numeric_only=True))

# Visualization

# Scatter Plot
sns.scatterplot(x='Internal_Marks', y='Final_Grade', data=data)
plt.title("Internal Marks vs Final Grade")
plt.show()

# Histogram
data.hist(figsize=(10,6))
plt.show()

# Boxplot
sns.boxplot(data=data[['Internal_Marks','Assignment_Score','Final_Grade']])
plt.show()

# Machine Learning
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X = data[['Internal_Marks', 'Assignment_Score']]
y = data['Final_Grade']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
prediction = model.predict([[15, 14]])

print("\nPredicted Final Grade:", prediction[0])
# Student Performance Analysis & Prediction 🎓

This project analyzes a student performance dataset to identify key factors influencing academic success. It includes exploratory data analysis (EDA), data visualization, and a Logistic Regression model to predict whether a student will pass or fail based on their habits and scores.

## 📌 Project Overview
The goal of this project is to understand the relationship between study habits (study hours, attendance) and academic outcomes. By utilizing Python's data science stack, we visualize trends and build a machine learning model to provide predictive insights.

## 📊 Key Features
* **Exploratory Data Analysis (EDA):** Detailed statistical summary of student demographics and scores.
* **Data Visualization:** * Correlation Heatmaps to find hidden patterns.
    * Distribution Histograms of subject scores.
    * Box plots comparing performance across Genders and Attendance levels.
    * Scatter plots showing the impact of Study Hours on final grades.
* **Machine Learning:** A Logistic Regression model that predicts the `Pass_Fail` status with high accuracy.

## 🛠️ Technologies Used
* **Python 3.x**
* **Pandas & NumPy:** Data manipulation and cleaning.
* **Matplotlib & Seaborn:** Advanced data visualization.
* **Scikit-Learn:** Machine learning (Preprocessing, Model Training, and Evaluation).

## 📈 Visualizations
Below are the key insights generated from the analysis:

### 1. Correlation Matrix
Identifies how variables like attendance and previous scores relate to the final percentage.

### 2. Performance by Category
Includes comparisons of average scores by gender and the distribution of passing vs. failing students.

### 3. Study Hours vs. Result
Visualizes the threshold where study hours significantly impact the probability of passing.

## 🚀 How to Run the Project
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
    ```
2.  **Install dependencies:**
    ```bash
    pip install pandas numpy matplotlib seaborn scikit-learn
    ```
3.  **Run the script:**
    Ensure the `Student_Performance_Dataset.csv` is in the same directory as the script, then run:
    ```bash
    python your_script_name.py
    ```

## 📝 Model Results
The Logistic Regression model evaluates students based on:
* Study Hours Per Day
* Attendance Percentage
* Subject Scores (Math, Science, English)
* Previous Year Scores

**Current Accuracy:** `[Insert your accuracy score here, e.g., 0.92]`

## 📂 File Structure
* `analysis_script.py`: The main Python code for analysis and modeling.
* `Student_Performance_Dataset.csv`: The dataset used for the project.
* `images/`: Folder containing saved plot outputs (PNGs).

---
Developed with ❤️ for Data Science.

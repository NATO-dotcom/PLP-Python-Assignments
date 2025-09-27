# Frameworks_Assignment – CORD-19 Data Explorer

This project explores the **CORD-19 research dataset** and provides a simple **Streamlit web application** to visualize insights.  
The assignment covers the complete beginner-friendly data science workflow: loading, cleaning, analyzing, visualizing, and presenting findings.

---

## 🚀 Learning Objectives

By completing this project, I practiced:

- Loading and exploring a real-world dataset
- Cleaning messy metadata (handling missing values, fixing date columns)
- Creating meaningful visualizations (bar charts, line plots, word cloud)
- Building a Streamlit app for interactive exploration
- Presenting insights effectively

---

## 📂 Project Structure

Frameworks_Assignment/
│── analysis.ipynb # Jupyter Notebook with exploration and analysis
│── app.py # Streamlit app for interactive visualization
│── requirements.txt # Dependencies
│── README.md # Documentation
│── metadata.csv # Dataset (from Kaggle) or sample subset


---

## 🛠️ Tools & Libraries

- Python 3.7+
- pandas → data manipulation  
- matplotlib & seaborn → visualizations  
- wordcloud → word frequency visualization  
- Streamlit → web application  

---

## 📊 Analysis Overview

### 🔹 Part 1: Data Loading and Exploration
- Loaded **metadata.csv** into pandas  
- Checked shape, column types, and missing values  
- Identified key columns: `title`, `abstract`, `publish_time`, `authors`, `journal`, `source_x`

### 🔹 Part 2: Data Cleaning
- Removed rows with missing `title` or `publish_time`  
- Converted `publish_time` to datetime  
- Extracted **year** for time-based analysis  
- Added `abstract_word_count` feature  

### 🔹 Part 3: Data Analysis
- Counted papers by year  
- Found **top journals** publishing COVID-19 research  
- Generated **word cloud** of frequent title words  
- Checked distribution of publications by **source**  

### 🔹 Part 4: Visualizations
- 📈 Publications per year (line chart / bar chart)  
- 📊 Top 10 journals (bar chart)  
- ☁️ Word cloud of titles  
- 📦 Papers by source (bar chart)  

### 🔹 Part 5: Streamlit App
Features in `app.py`:
- Slider to filter by publication year range  
- Interactive bar charts (top journals, publications per year)  
- Display of sample dataset rows  
- Keyword search (optional extra)  

Run the app:
```bash
streamlit run app.py

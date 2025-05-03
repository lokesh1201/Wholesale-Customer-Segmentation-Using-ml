# 🧠 Wholesale Customer Segmentation using Machine Learning

## 📌 Overview

This project leverages unsupervised machine learning techniques to segment wholesale customers based on their annual purchasing behavior. By analyzing patterns across different spending categories and customer metadata (like region and sales channel), businesses can gain actionable insights to:

- Tailor marketing campaigns
- Optimize inventory planning
- Enhance customer service strategies

The dataset includes spending amounts across the following categories:
- Fresh
- Milk
- Grocery
- Frozen
- Detergents & Paper  
...along with the **customer’s channel** (Hotel/Restaurant/Café or Retail) and **region** (Lisbon, Oporto, or Other).

---

## 🎯 Objectives

- Cluster customers into meaningful groups using ML algorithms
- Visualize customer segments for better interpretation
- Derive business insights from spending patterns

---

## 🚀 Features

- 🔍 Exploratory Data Analysis (EDA) with visual insights  
- ⚙️ Feature scaling and dimensionality reduction (PCA)  
- 🤖 Clustering using:
  - K-Means
  - Hierarchical Clustering
  - DBSCAN
- 📊 Visualized cluster behavior
- 📁 Modular structure for scalability

---

## 🛠️ Tech Stack

- **Language**: Python  
- **Libraries**:  
  - Data Analysis: `pandas`, `numpy`  
  - Visualization: `matplotlib`, `seaborn`  
  - Machine Learning: `scikit-learn`, `scipy`

---

## 📂 Project Structure

```bash
wholesale-customer-segmentation-using-ml/
│
├── data/                 # Dataset CSV files
├── notebooks/            # Jupyter notebooks for experiments & EDA
├── src/                  # Modular Python scripts
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation

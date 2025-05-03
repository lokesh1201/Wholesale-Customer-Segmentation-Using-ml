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

## ⚙️ Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/lokesh1201/Wholesale-Customer-Segmentation-Using-ml.git
   cd wholesale-customer-segmentation-using-ml
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the analysis:**
   Open the `.ipynb` files in the `notebooks/` folder using Jupyter Notebook or VS Code.

---

## 🧪 Clustering Techniques Used

* **K-Means Clustering:** Fast and efficient for large datasets
* **Hierarchical Clustering:** Provides a dendrogram-based structure
* **DBSCAN:** Captures noise and arbitrary shaped clusters

Each model was tested after scaling and PCA transformation to improve performance and reduce dimensionality.

---

## 📈 Outcomes

By segmenting customers based on behavioral patterns, the project helps wholesalers:

* Design personalized product bundles
* Focus sales efforts on high-potential customer segments
* Strategically expand into specific regions or channels

---

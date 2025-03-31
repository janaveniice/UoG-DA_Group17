# **UoG-DA_Group17**
This project uses the Line of Sight (LOS) & Non Line of Sight (NLOS) UWB dataset to create prediction and estimation models while demonstrating the three stages of Data Analytics - data preparation, data mining, and data visualization with result analysis. 

## Dataset
This project uses the [UWB LOS/NLOS dataset](https://github.com/ewine-project/UWB-LOS-NLOS-Data-Set) consisting of 21,000 LOS and 21,000 NLOS samples collected from 7 indoor environments (office1, office2, etc.). It consists of 15 features and 1 class.

## **LOS/NLOS Classifier Model**
Details of this model

## **Distance Estimation Model**
This model predicts distance measurements using various machine learning algorithms. The model employs **Lasso Regression**, **RBF Support Vector Regression (SVR)**, **Random Forest**, and **Gradient Boosting** to estimate distances based on input features. Each model is trained, tuned, and evaluated for its performance, with the best-performing models selected as the final model. The approach combines different models to enhance accuracy and reliability in distance estimation tasks.

## Project Structure
```
UoG-DA-Group17
├── dataset/                     # Dataset files
├── distance-estimator-model/    # Distance Estimation model
|   └── models/                  # Saved trained models
├── los-nlos-model/              # LOS/ NLOS classification model
|   └── models/                  # Saved trained models
├── .gitignore                   # Ignore unnecesary files in version control
├── README.md                    # Project documentation
└── requirements.txt             # Python dependencies
```

## **Setup**
### **1. Create virtual environment**
```bash
python -m venv myenv
```

### **2. Acitvate virual environment**
```bash
myenv\Scripts\activate
```

### **3. Install required packages**
```bash
pip install -r requirements.txt
```

### **4. Select virtual environment as interpreter**
1. Ctrl+Shift+P
2. Search for `Python: Select Interpreter`
3. Select `Python 3.12.x ('myenv')`

## Team Members
|    Name                    |   SIT ID     | GUID                      |
|----------------------------|--------------|---------------------------|
|Chek Yu Ting, Amanda        | 2301035      | 2957852C                  |
|Dayao Jana Venice Tagacay   | 2303402      | 2957966T                  |
|Muhammad Syahmi             | 2301125      | 2957843B                  |
|Putri Nadrah Binte Jefreydin| 2300999      | 2957844B                  |
|Ramesh Monika               | 2301133      | 2957942M                  |

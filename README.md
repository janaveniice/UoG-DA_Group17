# **UoG-DA_Group17**
This project uses the Line of Sight (LOS) & Non Line of Sight (NLOS) UWB dataset to create prediction and estimation models while demonstrating the three stages of Data Analytics - data preparation, data mining, and data visualization with result analysis. 

## **LOS/NLOS Classifier Model**
Details of this model

## **Distance Estimation Model**
Details of this model

## Dataset
This project uses the [UWB LOS/NLOS dataset](https://github.com/ewine-project/UWB-LOS-NLOS-Data-Set) consisting of 21,000 LOS and 21,000 NLOS samples collected from 7 indoor environments (office1, office2, etc.). It consists of 15 features and 1 class.

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

## **Export Jupyter Notebook to HTML**
This is to retain all the outputs as outputs disappear when there is kernel change detected.
### **1. Change to notebook's directory**
```bash
cd distance-estimator-model
```
or
```bash
cd los-nlos-model
```

### **2. Convert Jupyter Notebook to HTML**
```bash
jupyter nbconvert --to html model.ipynb --output notebook-with-outputs
```

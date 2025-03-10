# **UoG-DA_Group17**
This project uses the Line of Sight (LOS) & Non Line of Sight (NLOS) UWB dataset to create prediction and estimation models while demonstrating the three stages of Data Analytics - data preparation, data mining, and data visualization with result analysis. 

## **LOS/NLOS Classifier Model**
Details of this model

## **Distance Estimation Model**
Details of this model

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

### **2. Convert Jupyter Notebook to HTML**
```bash
jupyter nbconvert --to html model.ipynb --output model-with-outputs
```
<h1 align='center'> 🌾 Soil Fertility Prediction System 🌱</h1>

## **1. Project Overview** 📝
The Soil Fertility Prediction System is an **AI-powered application** that helps farmers and agronomists assess soil quality based on **key nutrient levels**: Nitrogen (N), Phosphorous (P), and Potassium (K).  

It predicts **soil fertility categories**:
- **0 – Low Fertility** ⚠️  
- **1 – Medium Fertility** 🟡  
- **2 – High Fertility** ✅  

This enables informed decisions about crop selection and fertilizer use.

---

## **2. Technology Stack** 💻
| Component | Technology |
|-----------|------------|
| Backend API | FastAPI 🐍 |
| Machine Learning Model | Gradient Boosting Classifier (GBM) 🌟 |
| Frontend | HTML, CSS, Jinja2 Templates 🎨 |
| Deployment Server | Uvicorn 🚀 |
| Data Handling | NumPy, Joblib 🧮 |
| Version Control | Git & GitHub 🔗 |

---

## **3. Data and Model** 📊
- **Features used**: Nitrogen (N), Phosphorous (P), Potassium (K)  
- **Target variable**: Soil Fertility Category (Low, Medium, High)  
- **Model**: Gradient Boosting Machine (GBM)  
- **Performance Metric**: F1-Score = **0.9660** 🌟  
- **Model Saving**: `gbm_model.pkl` for production-ready deployment  

---

## **4. System Workflow** 🔄
1. **User Input** ✍️: Enter soil nutrient values (N, P, K).  
2. **Backend Prediction** 🤖: FastAPI receives inputs and predicts fertility.  
3. **Output Display** 🖥️: Predicted fertility category shown on the web interface.  
4. **Optional Probabilities** 📊: Future versions can display probability scores for each class.  

---

## **5. Frontend Design** 🎨
- **Beautiful AI-generated background image** 🖼️  
- **Interactive numeric inputs** for N, P, K  
- **Responsive design** for web and mobile  
- **Prediction results highlighted** with emojis:  
  - ⚠️ Low Fertility  
  - 🟡 Medium Fertility  
  - ✅ High Fertility  

---

## **6. Deployment** 🚀
- **Local Deployment**: FastAPI + Uvicorn  
- **Static Files Handling**: CSS, images served via `/static/`  
- **Template Rendering**: Jinja2 used for dynamic prediction display  
- **Version Control**: Pushed to GitHub

---

## **7. Usage Instructions** 🛠️
1. Clone the repository:
```bash
git clone https://github.com/tayyabsarfraz/Soil-Fertility-Predictor.git

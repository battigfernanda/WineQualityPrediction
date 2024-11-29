# Wine Quality Alcohol Prediction

This project predicts alcohol content in white wine samples using machine learning techniques. 

## Steps to Run
1. Clone the repository: `git clone https://github.com/battigfernanda/WineQualityPrediction.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the Jupyter Notebook or Python scripts for training and predictions.

## License
MIT License

## Abstract
This project focuses on predicting the alcohol content in wine using machine learning techniques. The dataset utilized contains physicochemical properties of white wine samples, with the target variable being the alcohol percentage. 
PyCaret was used to streamline the process of data preprocessing, model comparison, and optimization. 
Various regression models were evaluated, with the CatBoost Regressor emerging as the best-performing model based on metrics such as Mean Absolute Error (MAE) and R-squared (R²). After hyperparameter tuning, the CatBoost model achieved an R² of 0.94 and an MAE of 0.22, demonstrating high accuracy and reliability. 
The model's performance was validated using unseen synthetic data, where it demonstrated strong generalization ability. 
Feature importance analysis was also conducted to provide insights into the key physicochemical factors influencing alcohol content in wine. 
The final model and pipeline were saved for future deployment, enabling efficient and accurate predictions on new wine data. 
This study highlights the potential of machine learning in enhancing predictive accuracy for practical applications in the wine industry.

Please review video below for a detailed overview.

https://youtu.be/5kWPTVOD2lk




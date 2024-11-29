import pandas as pd

# Create a synthetic unseen dataset with the same structure as your training data
synthetic_data = {
    'fixed acidity': [6.5, 7.0, 7.2],
    'volatile acidity': [0.3, 0.27, 0.25],
    'citric acid': [0.35, 0.36, 0.32],
    'residual sugar': [14.0, 20.7, 8.9],
    'chlorides': [0.05, 0.045, 0.046],
    'free sulfur dioxide': [40.0, 45.0, 35.0],
    'total sulfur dioxide': [183.0, 170.0, 160.0],
    'density': [0.998, 1.001, 0.995],
    'pH': [3.01, 3.00, 3.1],
    'sulphates': [0.5, 0.45, 0.48],
    'quality': [6, 6, 5]  # You can set quality to any value if it's not the target
}

# Convert it to a DataFrame
unseen_data = pd.DataFrame(synthetic_data)

# Optionally, save it as a CSV file for later use
unseen_data.to_csv('synthetic_unseen_data.csv', index=False)

print(unseen_data)

import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.preprocessing import LabelEncoder

# Step 1: Load data from CSV file
def load_data(filename):
    data = pd.read_csv(filename)
    return data

# Step 2: Encode categorical features and target variable
def encode_data(data):
    label_encoders = {}
    for column in data.columns:
        le = LabelEncoder()
        data[column] = le.fit_transform(data[column])
        label_encoders[column] = le
    return data, label_encoders

# Step 3: Train Decision Tree
def train_decision_tree(data):
    X = data.drop('class_buys_computer', axis=1)
    y = data['class_buys_computer']
    clf = DecisionTreeClassifier(criterion='entropy', random_state=0)
    clf.fit(X, y)
    return clf, X.columns

# Step 4: Display the Decision Tree structure
def display_tree(clf, feature_names):
    tree_text = export_text(clf, feature_names=feature_names)
    print("Decision Tree Structure:\n", tree_text)

# Step 5: Predict new instance
def predict_instance(clf, instance, label_encoders):
    instance_encoded = {col: label_encoders[col].transform([instance[col]])[0] for col in instance}
    prediction = clf.predict([list(instance_encoded.values())])
    return label_encoders['class_buys_computer'].inverse_transform(prediction)[0]

# Main function
def main():
    filename = 'E:\decision_tree.csv'  # Path to your CSV file
    data = load_data(filename)
    data, label_encoders = encode_data(data)
    clf, feature_names = train_decision_tree(data)
    display_tree(clf, feature_names)

    # Example input for prediction
    user_input = {
        'age': 'youth',
        'income': 'medium',
        'student': 'yes',
        'credit_rating': 'excellent'
    }
    prediction = predict_instance(clf, user_input, label_encoders)
    print("Prediction for class_buys_computer:", prediction)

if __name__ == "__main__":
    main()

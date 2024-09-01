import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier

def perform_analysis(df: pd.DataFrame):
    # Example: Linear Regression
    if 'target' in df.columns:
        X = df.drop(columns='target')
        y = df['target']
        model = LinearRegression()
        model.fit(X, y)
        return model.coef_

    # Example: KMeans Clustering
    kmeans = KMeans(n_clusters=3)
    clusters = kmeans.fit_predict(df)
    return clusters

    # Example: Random Forest Classifier
    if 'label' in df.columns:
        X = df.drop(columns='label')
        y = df['label']
        model = RandomForestClassifier()
        model.fit(X, y)
        return model.feature_importances_

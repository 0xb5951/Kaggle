from sklearn.preprocessing import LabelEncoder

def attach_label(df, target_column):
    le = LabelEncoder()
    le = le.fit(df[target_column])
    df[target_column + 'label'] = le.transform(df[target_column])
    return df
import pandas as pd

df_bug = pd.read_csv("test_bug.csv")

df_nolabel = pd.read_csv("test_normal.csv")

df_bug["class"] = "bug"

df_nolabel["class"] = "normal"


#gesamtes DF zum Trainieren !!
df_total = df_bug.append(df_nolabel, ignore_index=True)



#safe df
df_total.to_csv("total_csv",indes=False)


from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix



y = df_total["class"].to_numpy()
# Bag of Words der Reden extrahieren
vectorizer = CountVectorizer(binary=True)
X = vectorizer.fit_transform(df_total['body']).toarray()

# Daten aufteilen für Training und Test
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3,random_state=42)

# Klassifikator trainieren und testen
classifier = MultinomialNB()
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
# Vorhersage-Genauigkeit auswerten
print(accuracy_score(y_test, y_pred))

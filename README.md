

---

# Spam Detection Model (Naive Bayes + Streamlit)

This project implements a simple spam detection model using a Naive Bayes classifier trained on SMS messages. It also includes a Streamlit app for real-time message classification.

---

## Features

* Preprocessing of SMS data (lowercasing, punctuation removal)
* Vectorization using Bag-of-Words (`CountVectorizer`)
* Classification using `MultinomialNB` (Naive Bayes)
* Web interface using **Streamlit** for interactive predictions
* Model and vectorizer serialization using `pickle`

---

## Model Training

### Dataset

Uses a CSV file with SMS messages labeled as `spam` or `ham`.

### Steps

1. Load and clean the dataset (`spam dataset.csv`)
2. Encode labels (`spam` = 1, `ham` = 0)
3. Remove duplicates
4. Preprocess text (lowercase, remove punctuation)
5. Vectorize text using `CountVectorizer`
6. Split into training and testing sets
7. Train a `MultinomialNB` classifier
8. Evaluate accuracy
9. Save model and vectorizer as `spam_model.pkl` and `vectorizer.pkl`

---

## Requirements

```bash
pip install pandas scikit-learn streamlit
```

---

## Running the App

1. Make sure `spam_model.pkl` and `vectorizer.pkl` are in the same directory.
2. Save the Streamlit app portion as `app.py`.
3. Run the app:

```bash
streamlit run app.py
```

---

## File Structure

```
.
├── spam dataset.csv         # Dataset file
├── untitled1.py             # Training script
├── spam_model.pkl           # Trained Naive Bayes model
├── vectorizer.pkl           # CountVectorizer
└── app.py                   # Streamlit app (optional, from commented section)
```

---

## Example Output

* Input: `"Win a free iPhone now!"`

* Output:  *Spam Message Detected!*

* Input: `"Hey, are we still meeting today?"`

* Output:  *Not a Spam Message!*

---

Live App
You can access the live version of the Streamlit app here:
[https://emailspam-detection-erdstt4zb2njpe5sdudepc.streamlit.app/
](url)

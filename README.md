# 🧠 News Topic Modeling App

A Streamlit-based interactive web application that performs **topic modeling** and **clustering** on the classic [20 Newsgroups dataset](http://qwone.com/~jason/20Newsgroups/) using **LDA (Latent Dirichlet Allocation)** and **KMeans**.

## 🚀 Features

- 📂 Loads the 20 Newsgroups dataset
- 🧹 Cleans and preprocesses text using SpaCy & NLTK
- 🔍 Applies **KMeans Clustering** or **LDA Topic Modeling**
- 🌥️ Generates WordClouds to visualize discovered topics
- 🎛️ Streamlit interface for parameter selection and real-time results

---

 
![Screenshot 2025-07-09 150251](https://github.com/user-attachments/assets/60db5269-7a43-4545-9285-3a5ef4b0e08f)
![Screenshot 2025-07-09 150312](https://github.com/user-attachments/assets/2f6b3f86-1853-4b95-8891-1acedcaae153)
![Screenshot 2025-07-09 150423](https://github.com/user-attachments/assets/97b4757a-b6a7-470b-8ef8-1acfabd6b388)


🔧 Setup
1. Clone the repository
```bash
git clone https://github.com/therehanhussain/news-topic-modeling.git
cd news-topic-modeling
2. Create a virtual environment
bash
Copy
Edit
python -m venv venv
# Activate on Windows
venv\Scripts\activate
# Or activate on Mac/Linux
source venv/bin/activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Download SpaCy model
bash
Copy
Edit
python -m spacy download en_core_web_sm
▶️ Run the App
bash
Copy
Edit
# From the root directory
streamlit run streamlit_app.py
The app will open in your browser at http://localhost:8501.

📁 Project Structure
kotlin
Copy
Edit
news-topic-modeling/
│
├── data/
│   └── fetch_dataset.py
│
├── preprocessing/
│   └── clean_text.py
│
├── models/
│   ├── lda_model.py
│   └── kmeans_model.py
│
├── visualization/
│   └── wordclouds.py
│
├── streamlit_app.py
├── requirements.txt
└── README.md

📦 Requirements
Python 3.8+
Streamlit
Scikit-learn
SpaCy
NLTK
WordCloud
Matplotlib
Pandas

All dependencies are listed in requirements.txt.

🌐 Deployment
To deploy on Streamlit Cloud or Render:
Make sure streamlit_app.py is in the root directory.
Set the start command as:
bash
Copy
Edit
streamlit run streamlit_app.py
Add en_core_web_sm to your build script or install step.

🙋‍♂️ Author
MD Rehan Hussain
GitHub

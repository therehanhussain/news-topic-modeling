🧠 News Topic Modeling Web Application
A production-ready Streamlit application that performs unsupervised topic modeling and text clustering on the classic 20 Newsgroups dataset using Latent Dirichlet Allocation (LDA) and KMeans. This project demonstrates practical application of NLP, machine learning, and interactive data visualization techniques.

✅ Built as part of my Data Science Internship Final Project
👨‍💻 Author: MD Rehan Hussain
📌 Dataset: 20 Newsgroups (scikit-learn)

🚀 Key Features
✅ Automated Text Preprocessing using SpaCy and NLTK
🔍 Unsupervised Topic Modeling via LDA
📊 Text Clustering using KMeans
🌥️ WordCloud Visualizations of extracted topics
🧪 Interactive Parameter Control with Streamlit UI
📁 Modular structure for easy extensibility and maintenance

📸 Application Snapshot
![Screenshot 2025-07-09 150251](https://github.com/user-attachments/assets/60db5269-7a43-4545-9285-3a5ef4b0e08f)
![Screenshot 2025-07-09 150312](https://github.com/user-attachments/assets/2f6b3f86-1853-4b95-8891-1acedcaae153)
![Screenshot 2025-07-09 150423](https://github.com/user-attachments/assets/97b4757a-b6a7-470b-8ef8-1acfabd6b388)

🧱 Tech Stack
| Category         | Tools & Libraries                                |
| ---------------- | ------------------------------------------------ |
| Programming Lang | Python 3.8+                                      |
| Web Interface    | [Streamlit](https://streamlit.io/)               |
| NLP              | SpaCy, NLTK                                      |
| ML Algorithms    | Scikit-learn (KMeans), Gensim (LDA)              |
| Visualization    | WordCloud, Matplotlib, Streamlit Charts          |
| Deployment Ready | Compatible with **Streamlit Cloud** / **Render** |


📂 Project Structure
news-topic-modeling/
│
├── data/               # Dataset fetching scripts
│   └── fetch_dataset.py
│
├── preprocessing/      # NLP preprocessing pipeline
│   └── clean_text.py
│
├── models/             # ML models for topic modeling and clustering
│   ├── lda_model.py
│   └── kmeans_model.py
│
├── visualization/      # WordCloud generation
│   └── wordclouds.py
│
├── streamlit_app.py    # Main Streamlit UI logic
├── requirements.txt    # Python dependencies
└── README.md           # Project overview

 Local Setup Instructions
1. Clone the Repository
bash
git clone https://github.com/therehanhussain/news-topic-modeling.git
cd news-topic-modeling

2. Create and Activate Virtual Environment
bash
python -m venv venv
# Activate on Windows
venv\Scripts\activate
# Activate on Mac/Linux
source venv/bin/activate

3. Install Dependencies
bash
pip install -r requirements.txt

4. Download SpaCy Language Model
bash
python -m spacy download en_core_web_sm

▶️ Launch the App
bash
streamlit run streamlit_app.py
The application will open in your browser at http://localhost:8501

🌐 Deployment Guide (Render / Streamlit Cloud)
To deploy:
Ensure streamlit_app.py is in the root directory
Set the start command as:
bash
streamlit run streamlit_app.py
Include python -m spacy download en_core_web_sm in your build/install step

📌 Learning Outcomes
✅ Implemented modular and reusable machine learning pipelines
✅ Developed a production-grade Streamlit application
✅ Hands-on experience with unsupervised NLP techniques
✅ Gained expertise in text preprocessing, topic extraction, and visualization
✅ Understood best practices for code organization and interactive ML apps

🙋‍♂️ About the Author
MD Rehan Hussain
📍 B.Tech (AIML) | Intern @ Celebal Technologies
linkedin - https://www.linkedin.com/in/md-rehan-hussain-/










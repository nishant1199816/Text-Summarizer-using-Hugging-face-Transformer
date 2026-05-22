# 🧠 Text Summarizer Using Hugging Face Transformer

An AI-powered Text Summarization Web Application built using **Hugging Face Transformers**, **FastAPI**, and **Python**.  
This project can generate concise summaries from long text or conversations using a fine-tuned Transformer model.

---

# 🚀 Features

✅ Transformer-based NLP Model  
✅ Real-Time Text Summarization  
✅ FastAPI Backend  
✅ Clean Web Interface  
✅ Hugging Face Transformers  
✅ Fine-tuned on SAMSum Dataset  
✅ Easy to Run Locally  

---

# 🛠️ Technologies Used

- Python
- FastAPI
- Hugging Face Transformers
- Torch / PyTorch
- HTML
- CSS
- JavaScript
- NLP (Natural Language Processing)

---

# 📂 Project Structure

```bash
text-summarizer-using-Hugging-face-Transformer/
│
├── saved_summary_model/
├── app.py
├── index.html
├── requirements.txt
├── screenshots/
└── README.md

# 🧠 How It Works
User Input
    ↓
FastAPI Backend
    ↓
Transformer Model (T5)
    ↓
Generated Summary
    ↓
Displayed on Web Interface

The application uses a Transformer-based summarization model trained on the SAMSum dialogue dataset.


# 📊 Model Training
The model was trained using:

samsum-train.csv
samsum-validation.csv
samsum-test.csv

After training, the model was saved inside: saved_summary_model/

This saved model is later loaded into the FastAPI backend for real-time inference.

⚙️ Installation & Setup
1️⃣ Clone the Repository
https://github.com/nishant1199816/Text-Summarizer-using-Hugging-face-Transformer.git

2️⃣ Open Project Folder
cd text-summarizer-using-Hugging-face-Transformer

3️⃣ Install Dependencies
pip install -r requirements.txt
           or
pip install fastapi uvicorn transformers torch

▶️ Run the Project
Open terminal inside the project folder and run:-  uvicorn app:app --reload
After running the command, a local server link will appear:-  http://127.0.0.1:8000
Open this link in your browser.

💻 Application Preview

The user can:

- Paste long text or conversations
- Click the Summarize button
- Generate AI-based summaries instantly

# Model Download

The trained model is not uploaded because of GitHub file size limitations.


👨‍💻 Author
Nishant Singh

📧 Email: ns1199816@gmail.com

🔗 GitHub: https://github.com/nishant1199816

🔗 LinkedIn: https://www.linkedin.com/in/nishant-singh-55b57b16a/
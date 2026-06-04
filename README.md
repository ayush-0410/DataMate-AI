# 🧠 AI Data Analyst (Streamlit + OpenAI)

## 📌 Project Overview

The **AI Data Analyst** is an interactive web application built using Streamlit that leverages AI capabilities to analyze, interpret, and assist with data-driven queries. The system integrates OpenAI APIs to provide intelligent responses and supports lightweight data processing workflows.

This project demonstrates practical skills in:

* AI integration using APIs
* Web app development using Streamlit
* Python-based data handling
* Secure environment configuration

---

## 🚀 Key Features

* 💬 AI-powered conversational interface for data-related queries
* 📊 Data analysis support using Python (Pandas)
* ⚡ Fast and lightweight Streamlit UI
* 🔐 Secure API key handling using environment variables
* 🧩 Modular and scalable code structure

---

## 🛠️ Tech Stack

* **Programming Language:** Python 3.10+
* **Frontend/UI:** Streamlit
* **AI Integration:** OpenAI API
* **Data Processing:** Pandas
* **Environment Management:** python-dotenv

---

## 📁 Project Structure

```text
AI_Data_Analyst/
│── app.py                # Main Streamlit application
│── requirements.txt      # Project dependencies
│── .env                  # API keys (not pushed to GitHub)
│── .gitignore            # Ignored files configuration
│── README.md             # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI_Data_Analyst.git
cd AI_Data_Analyst
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Then open:

```
http://localhost:8501
```

---

## 🔐 Security Best Practices

* API keys are stored in `.env` file (not exposed in code)
* `.gitignore` ensures sensitive files are not committed
* No hardcoded credentials used

---

## 📈 Learning Outcomes

Through this project, I gained hands-on experience in:

* Building AI-powered applications
* Integrating REST APIs with Python
* Designing interactive web interfaces
* Managing secure environment configurations
* Structuring production-ready Python projects

---

## 📌 Future Improvements

* Add CSV upload for automated insights
* Enhance dashboard with visual analytics
* Improve prompt engineering for better AI responses
* Deploy on Streamlit Cloud / AWS

---

## 👨‍💻 Author

**Ayush**
IBM Certified Data Scientist

---

## ⭐ Acknowledgements

* OpenAI for API support
* Streamlit for rapid UI development
* Python open-source community

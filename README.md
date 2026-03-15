# HealthAdvice – Agentic AI for Medical Diagnostics

A Python project that builds **specialized AI agents** to analyze medical reports and generate possible diagnoses using **multi-agent reasoning**.

The system simulates a **multidisciplinary medical team** where different AI agents analyze a patient's report from different perspectives and combine their insights to suggest possible health conditions.

⚠️ **Disclaimer:**
This project is created for **educational and research purposes only**. It is **not intended for real medical diagnosis or clinical use**.

---

# 🧠 Project Overview

This project demonstrates how **Agentic AI systems** can collaborate to solve complex problems.

Instead of relying on a single AI model, multiple **specialist agents** analyze the same medical report independently and their outputs are combined to generate a final assessment.

### Workflow

Medical Report
↓
Cardiologist Agent
Psychologist Agent
Pulmonologist Agent
↓
Multidisciplinary Team Agent
↓
Final Diagnosis Report

Each agent focuses on a specific medical domain and provides insights relevant to that specialization.

---

# 🤖 AI Agents in the System

### Cardiologist Agent

Focus: Detect potential heart-related conditions.

Responsibilities:

* Analyze ECG and cardiac symptoms
* Identify arrhythmias or structural heart issues
* Suggest cardiovascular testing or monitoring

---

### Psychologist Agent

Focus: Identify possible psychological conditions.

Responsibilities:

* Detect anxiety or panic disorders
* Evaluate mental health indicators in the report
* Suggest therapy or counseling approaches

---

### Pulmonologist Agent

Focus: Assess respiratory conditions.

Responsibilities:

* Identify asthma, COPD, or lung infections
* Evaluate breathing-related symptoms
* Recommend pulmonary function testing

---

### Multidisciplinary Team Agent

This agent combines the insights from all specialists and produces:

• **3 possible health issues**
• **Reasoning for each condition**
• **Suggested next diagnostic steps**

---

# 🛠️ Technologies Used

Python
LangChain
Google Gemini API
Concurrent Multi-Agent Execution
Prompt Engineering

---

# 📂 Project Structure

```
HealthAdvice-agentic-ai
│
├── Utils
│   └── Agents.py          # AI agent implementations
│
├── Medical Reports        # Sample medical reports
│
├── results
│   └── final_diagnosis.txt
│
├── main.py                # Main execution script
├── requirements.txt       # Python dependencies
├── .gitignore
└── README.md
```

---

# ⚡ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/manishgupta412/HealthAdvice-agentic-ai.git
cd HealthAdvice-agentic-ai
```

---

### 2️⃣ Create a virtual environment

```
python -m venv venv
```

Activate it:

Windows:

```
venv\Scripts\activate
```

Mac/Linux:

```
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Add your API Key

Create a file called:

```
apikey.env
```

Add:

```
GOOGLE_API_KEY=your_gemini_api_key
```

---

### 5️⃣ Run the system

```
python main.py
```

The final diagnosis will be saved in:

```
results/final_diagnosis.txt
```

---

# 📊 Example Output

```
### Final Diagnosis

1. Panic Disorder
Reason: Episodes of sudden anxiety and shortness of breath.

2. Hyperventilation Syndrome
Reason: Rapid breathing patterns observed in patient report.

3. Possible Mild Cardiac Arrhythmia
Reason: Irregular heartbeat symptoms reported.
```

---

# 🔮 Future Improvements

Planned improvements include:

* Adding more specialist agents (Neurologist, Endocrinologist, Immunologist)
* Integration with **local LLMs (Llama, Mistral)** for offline usage
* Medical image analysis using **multimodal AI models**
* Structured output using **JSON schemas**
* Adding a **web interface for uploading reports**
* Agent memory and reasoning chains

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

Manish Gupta
B.Tech Computer Science Engineering

Project Focus:
Agentic AI • Multi-Agent Systems • AI in Healthcare

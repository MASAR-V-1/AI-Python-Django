# 🤖 AI-Python Service

This repository manages the AI integration features, chatbot capabilities, and dynamic PDF generation utilities for the platform. It is built using Python, Streamlit/Django, and integrated with advanced AI APIs.

---

## 🛠️ Requirements & Tech Stack
* **Language:** Python 3.11+
* **Environment Management:** Docker & Docker Compose
* **Core Libraries:** Integrated with Gemini API, Streamlit, and custom PDF generation engines (`my_pdf_maker.py`).

---

## 🚀 Getting Started (Local Setup)

Any developer can spin up this project locally using one of the two methods below.

### Method 1: Using Docker (Recommended & Fastest)
Ensure you have [Docker](https://www.docker.com/) installed on your machine. This method configures all dependencies and runtime environment layers automatically.

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd AI-PYTHON

--- 


### Method 2: Manual Python Setup (Alternative)
If you prefer running the code natively without Docker, follow these steps:

Create and activate a virtual environment:
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Install dependencies:
pip install -r requirements.txt


# Configure your .env file:
Ensure you have a .env file in the root directory with your GEMINI_API_KEY.

# Run the Application:

To execute the main pipeline: python main.py

To run the web server framework (if using django context):python manage.py runserver


## 📊 Features & Main Components

### 1. Dynamic PDF Generation (`my_pdf_maker.py`)
This service contains dedicated logic to compile system data and generate formatted reports dynamically into PDF structures. 
* To test the PDF generation standalone:
  ```bash
  python my_pdf_maker.py
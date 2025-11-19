1. Create & Activate Virtual Environment
   `python3 -m venv venv
   source venv/bin/activate        # macOS
   `
2. Install dependencies:
   `pip install -r requirements.txt` or `pip install .`
3. Add Your Documents inside
   `data/`
4. Build the FAISS Index
   `python build_index.py`
   faiss_index/
   ├── index.faiss
   ├── index.pkl
5. Run the Chatbot
   `streamlit run app.py`

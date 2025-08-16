# 🛍️ Multimodal Product Recommendation System  

A product recommendation engine for e-commerce platforms that combines **text + image features** to recommend similar products. Deployed with **Streamlit** for interactive exploration.  

---

## 🚀 Features  
- 🔹 **Text-based filtering** using BoW, TF-IDF, and IDF vectorization  
- 🔹 **Image-based filtering** using ResNet-50 embeddings  
- 🔹 **Hybrid recommendations** by combining text + image similarity  
- 🔹 **Interactive UI** deployed with Streamlit  

---

## 🏗️ Tech Stack  
- **NLP:** BoW, TF-IDF, IDF  
- **CV:** ResNet-50 (PyTorch, torchvision)  
- **Frameworks:** Scikit-learn, PyTorch, Streamlit  
- **Data:** Product descriptions + images  

---

## ⚡ Quick Start  
```bash
git clone https://github.com/yourusername/multimodal-recommender.git
cd multimodal-recommender
pip install -r requirements.txt
streamlit run app.py

---

### 📄 3. `app.py` (Streamlit App Skeleton)
```python
import streamlit as st
import pandas as pd
from utils import recommend_products

# Load product data
data = pd.read_csv("data/products.csv")

st.title("🛍️ Multimodal Product Recommendation System")
st.write("Search for a product and get recommendations based on text + image similarity.")

product_id = st.selectbox("Select a Product ID", data['product_id'])

if st.button("Recommend"):
    recommendations = recommend_products(product_id, data)
    for rec in recommendations:
        st.image(rec['image'], width=150)
        st.write(rec['title'])
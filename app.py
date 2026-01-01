import streamlit as st
import json

st.title("📚 Books Viewer")

# Upload JSON file
uploaded_file = st.file_uploader("Upload your EMIS JSON file", type="json")

if uploaded_file:
    try:
        data = json.load(uploaded_file)
        
        star_line = "*" * 30
        st.subheader(f"School Name  : {data.get('school_name', 'N/A')}")
        st.subheader(f"School Code  : {data.get('school_code', 'N/A')}")
        st.markdown(f"```\n{star_line}\n```")
        
        for book in data.get("_list_books", []):
            if book.get("class") in ("9", "11"):
                st.write(f"**Class ({book.get('class')})  {book.get('book')}**")
                st.write(f"Used Books Stock : {book.get('old_stock')} | New Book Stock : {book.get('new_stock')}")
                st.markdown("---")

    except json.JSONDecodeError:
        st.error("⚠️ Invalid JSON file. Please upload a correct EMIS JSON.")

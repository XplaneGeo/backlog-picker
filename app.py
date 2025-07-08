import streamlit as st
import pandas as pd
import random

# כותרת
st.set_page_config(page_title="Backlog Picker", layout="centered")
st.title("🎮 חמישיית הבאקלוג שלך")

# העלאת קובץ הבאקלוג
uploaded_file = st.file_uploader("העלה את קובץ הבאקלוג שלך (CSV)", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    # מילון קטגוריות עם מילות מפתח
    category_keywords = {
        "RPG כבד": ["RPG", "Chronicle", "Persona", "Suikoden", "XCOM", "Arma"],
        "משחק קצר": ["Sleeper", "GRIS", "Operator", "Unpacking", "Portal", "Donut"],
        "משחק נרטיבי": ["Voice", "Doki", "Life is Strange", "Telltale", "Narrative", "Heaven's Vault"],
        "משחק מרגש": ["Sakuna", "GRIS", "To the Moon", "Eiyuden", "Emotional", "Brothers"],
        "כיבוי מוח": ["Tetris", "Balatro", "Lamb", "Golf", "Vampire Survivors", "Shogun", "Slay the Spire"]
    }

    # כפתור רענון
    if st.button("🎲 רענן בחירה רנדומלית"):
        st.experimental_rerun()

    # בחירת משחק רנדומלי לכל קטגוריה
    for category, keywords in category_keywords.items():
        matches = df[df["Title"].apply(lambda title: any(kw.lower() in str(title).lower() for kw in keywords))]
        if not matches.empty:
            game = matches.sample(1).iloc[0]
            st.markdown(f"### {category}")
            st.write(f"**{game['Title']}** ({game['Platform']})")
            st.caption(f"סטטוס: {game['Status']}")
        else:
            st.markdown(f"### {category}")
            st.warning("לא נמצאו משחקים תואמים בבאקלוג שלך.")
else:
    st.info("אנא העלה קובץ CSV עם עמודת 'Title' ו-'Platform' לפחות.")

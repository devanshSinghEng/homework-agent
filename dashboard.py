import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="Homework Generator Analytics", layout="wide")

st.title("AI Homework Generator - Analytics Dashboard")
st.write("Tracking AI-generated homework sheets from handwritten class notes.")

conn = sqlite3.connect("homework_tracker.db")
conn.execute("""
    CREATE TABLE IF NOT EXISTS homework_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        source_pdf TEXT,
        topic TEXT,
        num_questions INTEGER,
        generated_on TEXT
    )
""")
df = pd.read_sql_query("SELECT * FROM homework_log", conn)
conn.close()

if df.empty:
    st.warning("No data yet. Run main.py first to generate some homework sheets.")
else:
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Sheets Generated", len(df))
    col2.metric("Total Questions Generated", int(df["num_questions"].sum()))
    col3.metric("Unique Topics", df["topic"].nunique())

    st.subheader("Homework Sheets by Topic")
    topic_counts = df.groupby("topic")["id"].count().sort_values(ascending=False)
    st.bar_chart(topic_counts)

    st.subheader("Generation History")
    st.dataframe(
        df[["source_pdf", "topic", "num_questions", "generated_on"]]
        .sort_values("generated_on", ascending=False),
        use_container_width=True
    )
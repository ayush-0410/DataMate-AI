import streamlit as st
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

st.set_page_config(page_title="AI Data Analyst Assistant")

st.title("📊 AI Data Analyst Assistant")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Dataset Information")

    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric(
        "Missing Values",
        int(df.isnull().sum().sum())
    )

    summary = f"""
Rows: {df.shape[0]}
Columns: {df.shape[1]}

Statistics:
{df.describe(include='all').to_string()}
"""

    prompt = f"""
You are a Senior Business Analyst.

Analyze this dataset:

{summary}

Provide:
1. Key Trends
2. Business Insights
3. Risks
4. Opportunities
5. Recommendations
"""

    if st.button("Generate AI Insights"):

        with st.spinner("Analyzing..."):

            response = client.chat.completions.create(
                model="deepseek/deepseek-chat",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            st.subheader("🤖 AI Insights")

            st.write(response.choices[0].message.content)
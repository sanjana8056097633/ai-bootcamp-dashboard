import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set page config
st.set_page_config(page_title="SNS AI Bootcamp Dashboard", layout="wide")

# Title and subtitle
st.title("🎉 SNS Institutions – Generative AI Bootcamp")
st.subheader("Final Outcome Report | College-wise Summary")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("data.csv")

try:
    data = load_data()

    # Convert counts to completion rates
    deliverables = ["Lesson Plan", "PPT", "In-Class Assessments", 
                   "IAE Question Paper", "IAE Answer Key", "Question Bank"]
    
    data["Total Deliverables"] = data["Total Faculty"] * 6
    data["Completed Deliverables"] = data[deliverables].sum(axis=1)
    data["Completion Rate (%)"] = (data["Completed Deliverables"] / data["Total Deliverables"]) * 100

    # Overall summary
    st.markdown("## 🏫 College-wise Completion Summary")

    cols = st.columns(3)
    for idx, row in data.iterrows():
        with cols[idx % 3]:
            st.markdown(f"### {row['College']}")
            st.markdown(f"🧑‍🏫 Faculty: {row['Total Faculty']}")
            st.markdown(f"✅ Completion: **{row['Completion Rate (%)']:,.1f}%**")
            st.progress(int(row['Completion Rate (%)']) / 100)

    # Bar chart for completion rates
    st.markdown("## 📊 Completion Rate Across Colleges")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(data['College'], data['Completion Rate (%)'], color='skyblue', edgecolor='navy')
    ax.set_ylabel("Completion Rate (%)")
    ax.set_xlabel("College")
    ax.set_title("AI Bootcamp: College-wise Completion Rate")
    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig)

    # Key insights
    st.markdown("## 💡 Key Observations")
    st.write("""
    - All 10 colleges actively participated in the Generative AI Bootcamp.
    - Multiple colleges achieved near 100% compliance in AI-generated academic content.
    - Opportunities exist to strengthen PPT coverage and in-class assessments across departments.
    - The initiative marks a significant step toward AI-integrated education at SNS Institutions.
    """)

    # Footer
    st.markdown("---")
    st.markdown("📊 Dashboard built with ❤️ using Streamlit | Prepared for Technical Director")

except Exception as e:
    st.error("Error loading data. Please ensure 'data.csv' is correctly formatted.")
    st.write(e)

import streamlit as st
from agents.extractor import extract_info
from agents.debater import run_debate
from agents.summarizer import summarize_debate

st.title("🧠 DecisionForge MVP")
st.write("Simulate policy decisions with agentic AI")

user_input = st.text_area("Describe your decision dilemma")

if st.button("Run Simulation") and user_input:
    with st.spinner("Extracting stakeholders and decision process..."):
        extracted = extract_info(user_input)
        st.subheader("🔍 Extracted Information")
        st.json(extracted)

    with st.spinner("Running debate simulation..."):
        debate = run_debate(extracted)
        st.subheader("🎭 AI Debate")
        for line in debate:
            st.markdown(f"**{line['agent']}**: {line['message']}")

    with st.spinner("Summarizing discussion..."):
        summary = summarize_debate(debate)
        st.subheader("📝 Summary and Recommendation")
        st.markdown(summary)
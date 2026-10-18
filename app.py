
import streamlit as st

from src.log_loader import load_log_file
from src.log_analyzer import analyze_log

st.set_page_config(
    page_title="LLM Log Analyzer",
    page_icon="🔍",
    layout="wide",
)

st.title("🔍 LLM Log Analyzer")
st.caption("Find the exact error, likely root cause, and what needs to be checked.")

uploaded_file = st.file_uploader(
    "Upload application log",
    type=["log", "txt"],
    max_upload_size=5,
)

if uploaded_file is not None:
    try:
        log_content = load_log_file(uploaded_file)

        col1, col2 = st.columns(2)
        col1.metric("File Size", f"{uploaded_file.size / 1024:.2f} KB")
        col2.metric("Characters", f"{len(log_content):,}")

        if st.button("Find Exact Error", type="primary"):
            with st.spinner("Analyzing logs..."):
                result = analyze_log(log_content)

            st.subheader("Analysis Result")

            if result.get("sensitive_data_masked"):
                st.warning(
                    "Sensitive data was detected and masked before sending logs to the LLM."
                )
            else:
                st.info("No sensitive data was detected by the current masking rules.")

            with st.expander("View masked logs sent to LLM"):
                st.text(result["masked_log_content"])

            st.markdown(result["content"])

            with st.expander("Token Usage"):
                st.write(f"Model: {result['model']}")
                st.write(f"Input tokens: {result['prompt_tokens']:,}")
                st.write(f"Output tokens: {result['completion_tokens']:,}")
                st.write(f"Total tokens: {result['total_tokens']:,}")

    except ValueError as exc:
        st.error(str(exc))
    except Exception as exc:
        st.error(f"Analysis failed: {exc}")

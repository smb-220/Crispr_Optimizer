import streamlit as st
from blockchain.log_results import contract
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 gRNA Analytics Dashboard")

total = contract.functions.getTotalEntries().call()
entries = []

for i in range(total):
    seq, gene, score, ts = contract.functions.getEntry(i).call()
    entries.append({
        "Sequence": seq,
        "Gene": gene,
        "Score": score / 1000,
        "Timestamp": pd.to_datetime(ts, unit='s')
    })

df = pd.DataFrame(entries)

if df.empty:
    st.warning("No data yet.")
else:
    st.write("### 📈 Top gRNAs")
    st.dataframe(df.sort_values("Score", ascending=False).head(10))

    st.write("### 🧬 Gene Frequency")
    st.bar_chart(df["Gene"].value_counts())

    st.write("### 📅 Timeline of gRNA submissions")
    st.line_chart(df.set_index("Timestamp")["Score"].resample("D").mean())

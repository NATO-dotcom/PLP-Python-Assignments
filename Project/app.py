import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data():
    df = pd.read_csv('metadata.csv', engine='python', on_bad_lines='skip')
    df = df[["title", "abstract", "publish_time", "authors", "journal", "source_x"]]
    df.dropna(subset=["title", "publish_time"], inplace=True)
    df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
    df["year"] = df["publish_time"].dt.year
    return df

df = load_data()

st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers")

# Year filter
min_year, max_year = int(df["year"].min()), int(df["year"].max())
year_range = st.slider("Select year range", min_year, max_year, (2020, 2021))
filtered = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1])]

# Publications by year
st.write("### Publications by Year")
year_counts = filtered["year"].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values)
st.pyplot(fig)

# Top journals
st.write("### Top 10 Journals")
top_journals = filtered["journal"].value_counts().head(10)
fig, ax = plt.subplots()
sns.barplot(y=top_journals.index, x=top_journals.values, ax=ax)
st.pyplot(fig)

# Show data sample
st.write("### Sample Data")
st.write(filtered.head(20))

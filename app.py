import streamlit as st
import pandas as pd
import plotly.express as px
from collections import Counter

st.set_page_config(
    page_title="Exhibition Title Language Dashboard",
    page_icon="🎨",
    layout="wide"
)

@st.cache_data
def load_data():
    return pd.read_csv("exhibition_titles.csv")

df = load_data()

st.title("🎨 Exhibition Title Language Dashboard")
st.caption("A Streamlit dashboard analyzing repeated words, language types, and conceptual patterns in Korean contemporary art exhibition titles.")

st.markdown("""
This project looks at exhibition titles not only as simple labels, but also as a form of artistic and institutional language.
By collecting and visualizing exhibition titles from Korean contemporary art institutions, the dashboard explores how museums and galleries repeatedly use concepts such as memory, body, time, space, image, nature, archive, and relationship.
""")

# Sidebar filters
st.sidebar.header("Filters")

year_options = sorted(df["year"].dropna().unique())
venue_options = sorted(df["venue"].dropna().unique())
language_options = sorted(df["language_type"].dropna().unique())
keyword_options = sorted(df["keyword_category"].dropna().unique())

selected_years = st.sidebar.multiselect("Year", year_options, default=year_options)
selected_venues = st.sidebar.multiselect("Venue", venue_options, default=venue_options)
selected_languages = st.sidebar.multiselect("Language Type", language_options, default=language_options)
selected_keywords = st.sidebar.multiselect("Keyword Category", keyword_options, default=keyword_options)

filtered_df = df[
    (df["year"].isin(selected_years)) &
    (df["venue"].isin(selected_venues)) &
    (df["language_type"].isin(selected_languages)) &
    (df["keyword_category"].isin(selected_keywords))
]

# Metrics
st.subheader("Overview")

col1, col2, col3, col4 = st.columns(4)

total_exhibitions = len(filtered_df)
total_venues = filtered_df["venue"].nunique()
most_common_language = filtered_df["language_type"].mode()[0] if not filtered_df.empty else "N/A"
most_common_keyword = filtered_df["keyword_category"].mode()[0] if not filtered_df.empty else "N/A"

col1.metric("Total Exhibitions", total_exhibitions)
col2.metric("Venues", total_venues)
col3.metric("Most Common Language", most_common_language)
col4.metric("Most Common Keyword", most_common_keyword)

st.divider()

# Chart 1: Keyword category frequency
st.subheader("1. Keyword Category Frequency")
st.write("This chart shows which conceptual categories appear most often in the exhibition titles.")

if not filtered_df.empty:
    keyword_counts = (
        filtered_df["keyword_category"]
        .value_counts()
        .reset_index()
    )
    keyword_counts.columns = ["keyword_category", "count"]

    fig_keyword = px.bar(
        keyword_counts,
        x="keyword_category",
        y="count",
        text="count",
        title="Most Frequent Keyword Categories"
    )
    fig_keyword.update_layout(xaxis_title="Keyword Category", yaxis_title="Number of Exhibitions")
    st.plotly_chart(fig_keyword, use_container_width=True)
else:
    st.warning("No data available for the selected filters.")

# Chart 2: Language type distribution
st.subheader("2. Language Type Analysis")
st.write("This chart compares Korean-only, English-only, and mixed-language exhibition titles.")

if not filtered_df.empty:
    language_counts = (
        filtered_df["language_type"]
        .value_counts()
        .reset_index()
    )
    language_counts.columns = ["language_type", "count"]

    fig_language = px.bar(
        language_counts,
        x="language_type",
        y="count",
        text="count",
        title="Language Type Distribution"
    )
    fig_language.update_layout(xaxis_title="Language Type", yaxis_title="Number of Exhibitions")
    st.plotly_chart(fig_language, use_container_width=True)

# Chart 3: Venue comparison
st.subheader("3. Keyword Patterns by Venue")
st.write("This chart compares which keyword categories appear across different museums and galleries.")

if not filtered_df.empty:
    venue_keyword = (
        filtered_df.groupby(["venue", "keyword_category"])
        .size()
        .reset_index(name="count")
    )

    fig_venue = px.bar(
        venue_keyword,
        x="venue",
        y="count",
        color="keyword_category",
        barmode="group",
        title="Keyword Category by Venue"
    )
    fig_venue.update_layout(xaxis_title="Venue", yaxis_title="Number of Exhibitions")
    st.plotly_chart(fig_venue, use_container_width=True)

# Raw keyword frequency from main_keywords
st.subheader("4. Word Frequency from Main Keywords")
st.write("This chart counts individual words from the `main_keywords` column.")

if not filtered_df.empty:
    words = []
    for item in filtered_df["main_keywords"].dropna():
        words.extend([word.strip().lower() for word in item.split(",")])

    word_counts = Counter(words)
    word_df = pd.DataFrame(word_counts.items(), columns=["word", "count"]).sort_values("count", ascending=False).head(15)

    fig_words = px.bar(
        word_df,
        x="word",
        y="count",
        text="count",
        title="Top 15 Repeated Words"
    )
    fig_words.update_layout(xaxis_title="Word", yaxis_title="Frequency")
    st.plotly_chart(fig_words, use_container_width=True)

st.divider()

# Data table
st.subheader("Exhibition Title Dataset")
st.write("The table below shows the dataset used for this dashboard. The current version uses sample or semi-realistic data and can later be expanded with verified exhibition information from official museum and gallery websites.")

st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True
)

# Interpretation section
st.subheader("Project Interpretation")
st.markdown("""
This dashboard suggests that exhibition titles can be analyzed as more than informational labels.
Repeated concepts such as memory, archive, body, space, time, image, nature, and relationship reveal how contemporary art institutions frame exhibitions before viewers encounter the artworks.

The project can be further developed by replacing the sample dataset with a larger collection of verified exhibition data from official museum and gallery websites.
""")

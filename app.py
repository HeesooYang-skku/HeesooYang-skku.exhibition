import streamlit as st
import pandas as pd
import plotly.express as px
from collections import Counter
from io import StringIO

st.set_page_config(
    page_title="Exhibition Title Language Dashboard",
    page_icon="🎨",
    layout="wide"
)

COLUMNS = [
    "title",
    "venue",
    "year",
    "language_type",
    "main_keywords",
    "keyword_category",
    "category",
    "url"
]

LANGUAGE_TYPES = ["Korean-only", "English-only", "Mixed"]
KEYWORD_CATEGORIES = [
    "Memory",
    "Body",
    "Time",
    "Space",
    "Image",
    "Nature",
    "Archive",
    "Relationship",
    "Institution",
    "Other"
]

def load_data():
    df = pd.read_csv("exhibition_titles.csv")
    for col in COLUMNS:
        if col not in df.columns:
            df[col] = ""
    return df[COLUMNS]

def convert_df_to_csv(dataframe):
    return dataframe.to_csv(index=False, encoding="utf-8-sig").encode("utf-8-sig")

df = load_data()

st.title("🎨 Exhibition Title Language Dashboard")
st.caption("A Streamlit dashboard analyzing repeated words, language types, and conceptual patterns in Korean contemporary art exhibition titles.")

st.markdown("""
This project looks at exhibition titles not only as simple labels, but also as a form of artistic and institutional language.
You can edit the dataset directly in this app, add new exhibition titles, and download the updated CSV file.
""")

st.info(
    "How to use: Add or edit rows in the dataset editor below. "
    "After editing, download the updated CSV file and replace `exhibition_titles.csv` in your GitHub repository."
)

# Editable dataset section
st.subheader("Editable Exhibition Dataset")

edited_df = st.data_editor(
    df,
    num_rows="dynamic",
    use_container_width=True,
    hide_index=True,
    column_config={
        "title": st.column_config.TextColumn("Title", help="Official exhibition title"),
        "venue": st.column_config.TextColumn("Venue", help="Museum or gallery name"),
        "year": st.column_config.NumberColumn("Year", min_value=2000, max_value=2030, step=1),
        "language_type": st.column_config.SelectboxColumn(
            "Language Type",
            options=LANGUAGE_TYPES,
            help="Korean-only, English-only, or Mixed"
        ),
        "main_keywords": st.column_config.TextColumn(
            "Main Keywords",
            help="Use comma-separated keywords, e.g. memory, archive, body"
        ),
        "keyword_category": st.column_config.SelectboxColumn(
            "Keyword Category",
            options=KEYWORD_CATEGORIES,
            help="Choose the main conceptual category"
        ),
        "category": st.column_config.TextColumn("Category", help="solo exhibition, group exhibition, collection, etc."),
        "url": st.column_config.LinkColumn("URL", help="Official source website")
    }
)

edited_df = edited_df.dropna(how="all")
edited_df["year"] = pd.to_numeric(edited_df["year"], errors="coerce")

csv = convert_df_to_csv(edited_df)

st.download_button(
    label="⬇️ Download Updated CSV",
    data=csv,
    file_name="exhibition_titles.csv",
    mime="text/csv"
)

st.caption(
    "Important: On Streamlit Cloud, edits are not automatically saved back to GitHub. "
    "Download the CSV and upload it to GitHub to permanently update the dataset."
)

st.divider()

# Filters
st.sidebar.header("Filters")

clean_df = edited_df.dropna(subset=["title"]).copy()

year_options = sorted(clean_df["year"].dropna().astype(int).unique()) if not clean_df.empty else []
venue_options = sorted(clean_df["venue"].dropna().unique()) if not clean_df.empty else []
language_options = sorted(clean_df["language_type"].dropna().unique()) if not clean_df.empty else []
keyword_options = sorted(clean_df["keyword_category"].dropna().unique()) if not clean_df.empty else []

selected_years = st.sidebar.multiselect("Year", year_options, default=year_options)
selected_venues = st.sidebar.multiselect("Venue", venue_options, default=venue_options)
selected_languages = st.sidebar.multiselect("Language Type", language_options, default=language_options)
selected_keywords = st.sidebar.multiselect("Keyword Category", keyword_options, default=keyword_options)

if clean_df.empty:
    filtered_df = clean_df
else:
    filtered_df = clean_df[
        (clean_df["year"].astype("Int64").isin(selected_years)) &
        (clean_df["venue"].isin(selected_venues)) &
        (clean_df["language_type"].isin(selected_languages)) &
        (clean_df["keyword_category"].isin(selected_keywords))
    ]

# Overview
st.subheader("Overview")

col1, col2, col3, col4 = st.columns(4)

total_exhibitions = len(filtered_df)
total_venues = filtered_df["venue"].nunique() if not filtered_df.empty else 0
most_common_language = filtered_df["language_type"].mode()[0] if not filtered_df.empty and not filtered_df["language_type"].mode().empty else "N/A"
most_common_keyword = filtered_df["keyword_category"].mode()[0] if not filtered_df.empty and not filtered_df["keyword_category"].mode().empty else "N/A"

col1.metric("Total Exhibitions", total_exhibitions)
col2.metric("Venues", total_venues)
col3.metric("Most Common Language", most_common_language)
col4.metric("Most Common Keyword", most_common_keyword)

st.divider()

# Chart 1
st.subheader("1. Keyword Category Frequency")
st.write("This chart shows which conceptual categories appear most often in the exhibition titles.")


if not filtered_df.empty:
    keyword_counts = filtered_df["keyword_category"].value_counts().reset_index()
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

# Chart 2
st.subheader("2. Language Type Analysis")
st.write("This chart compares Korean-only, English-only, and mixed-language exhibition titles.")

if not filtered_df.empty:
    language_counts = filtered_df["language_type"].value_counts().reset_index()
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

# Chart 3
st.subheader("3. Keyword Patterns by Venue")
st.write("This chart compares which keyword categories appear across different museums and galleries.")

if not filtered_df.empty:
    venue_keyword = filtered_df.groupby(["venue", "keyword_category"]).size().reset_index(name="count")
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

# Chart 4
st.subheader("4. Word Frequency from Main Keywords")
st.write("This chart counts individual words from the `main_keywords` column.")

if not filtered_df.empty:
    words = []
    for item in filtered_df["main_keywords"].dropna():
        words.extend([word.strip().lower() for word in str(item).split(",") if word.strip()])

    if words:
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

st.subheader("Filtered Data Table")
st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True
)

st.subheader("Project Interpretation")
st.markdown("""
This dashboard suggests that exhibition titles can be analyzed as more than informational labels.
Repeated concepts such as memory, archive, body, space, time, image, nature, and relationship reveal how contemporary art institutions frame exhibitions before viewers encounter the artworks.
""")

[README.md](https://github.com/user-attachments/files/28193404/README.md)
# Exhibition Language & Keyword Dashboard

## Project Overview

This project is a Streamlit web dashboard that analyzes keywords and conceptual patterns in Korean contemporary art exhibition titles and descriptions.

The project originally began as an analysis of exhibition titles. However, while collecting data, I realized that many contemporary art exhibition titles are poetic, abstract, or metaphorical. Therefore, the title alone was not enough to understand the conceptual direction of each exhibition.

For this reason, the project expanded from title analysis to keyword-based analysis. It uses both exhibition titles and exhibition descriptions to classify exhibitions into broader conceptual categories such as Archive, Nature, Body, Relationship, Space, Image, Memory, and Time.

## Research Questions

- What conceptual keywords appear most often in Korean contemporary art exhibitions?
- Which keyword categories are most frequently used by museums and galleries?
- Do different institutions show different keyword patterns?
- How do exhibition titles and descriptions frame contemporary art before audiences encounter the artworks?
- What can repeated keywords reveal about current tendencies in contemporary art institutions?

## Dataset

The dataset includes the following columns:

| Column | Description |
|---|---|
| title | Official exhibition title |
| venue | Museum or gallery name |
| year | Exhibition year |
| language_type | Korean-only, English-only, or mixed title |
| main_keywords | Main concepts extracted from the exhibition title and description |
| keyword_category | Broader conceptual category |
| category | Exhibition type |
| url | Source website |

## Keyword Categories

The project classifies exhibitions into broad conceptual categories:

| Category | Meaning |
|---|---|
| Archive | Collection, record, storage, documentation, art history, institutional memory |
| Nature | Ecology, climate, nonhuman beings, earth, plants, environment, Anthropocene |
| Body | Body, performance, vulnerability, gender, senses, physical experience |
| Relationship | Community, connection, intimacy, exchange, conflict, solidarity |
| Space | Place, site, architecture, city, museum space, location |
| Image | Photography, painting, screen, representation, visuality, media image |
| Memory | Historical memory, trauma, personal memory, remembrance, testimony |
| Time | History, duration, transition, continuity, future, contemporaneity |
| Institution | Museum system, art institution, cultural policy, art field structure |
| Other | Concepts that do not clearly fit into the above categories |

## Dashboard Features

- Editable data table
- Add new exhibition rows
- Download updated CSV
- Interactive filters
- Keyword category frequency chart
- Language type analysis chart
- Keyword patterns by venue
- Word frequency chart based on main keywords

## Important Editing Note

On Streamlit Cloud, changes made inside the app are not automatically saved back to GitHub.

To permanently update the dataset:

1. Edit or add rows in the dashboard.
2. Click **Download Updated CSV**.
3. Replace the old `exhibition_titles.csv` file in the GitHub repository with the downloaded file.
4. Commit the change on GitHub.
5. Streamlit Cloud will redeploy the app with the updated data.

## Tools Used

- Python
- Pandas
- Streamlit
- Plotly

## How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Project Meaning

This project looks at exhibition language not only as information, but also as a way that contemporary art institutions produce meaning. Exhibition titles are often the first text that audiences encounter, but the title alone cannot always reveal the full conceptual direction of the exhibition.

By combining titles with exhibition descriptions and classifying them into keyword categories, this dashboard shows how recurring ideas such as archive, nature, body, relationship, space, image, memory, and time appear across contemporary art exhibitions.

The project therefore shifts from a narrow title analysis to a broader analysis of exhibition language and conceptual keywords.

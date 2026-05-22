# Exhibition Title Language Dashboard

## Project Overview

This project is a Streamlit web dashboard that analyzes the language used in contemporary art exhibition titles in Korea.  
Instead of simply listing exhibitions by venue or date, the dashboard focuses on repeated words, language types, and conceptual patterns found in exhibition titles.

As a Fine Art student, I am interested in how exhibitions introduce themselves before the audience even sees the artworks. The exhibition title is often the first text that viewers encounter, and it can shape their expectations and interpretation of the exhibition.

## Research Questions

- What words or concepts appear most often in Korean contemporary art exhibition titles?
- Do Korean museums and galleries use Korean-only, English-only, or mixed-language titles?
- Are certain keyword categories more common in specific museums or galleries?
- How do exhibition titles function as artistic and institutional language?

## Dataset

The dataset includes the following columns:

| Column | Description |
|---|---|
| title | Official exhibition title |
| venue | Museum or gallery name |
| year | Exhibition year |
| language_type | Korean-only, English-only, or mixed title |
| main_keywords | Main concepts found in the title |
| keyword_category | Broader conceptual category |
| category | Exhibition type |
| url | Source website |

The current dataset uses sample or semi-realistic data. It can later be expanded with verified exhibition information from official museum and gallery websites.

## Dashboard Features

- Overview metric cards
- Interactive sidebar filters
- Keyword category frequency chart
- Language type analysis chart
- Venue comparison chart
- Word frequency chart
- Interactive exhibition data table

## Tools Used

- Python
- Pandas
- Streamlit
- Plotly

## How to Run

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the Streamlit app:

```bash
streamlit run app.py
```

## Project Meaning

This project looks at exhibition titles not only as simple labels, but also as a form of artistic and institutional language.  
By visualizing repeated words and concepts, the dashboard shows how contemporary art institutions frame exhibitions before the audience encounters the artworks.

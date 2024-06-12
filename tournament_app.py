import streamlit as st
import pandas as pd
import pickle

with open('uefa_euro_dict_table_result', 'rb') as input_file:
    dict_table = pickle.load(input_file)

df_fixture_knockout_copy = pd.read_csv("df_fixture_knockout.csv")
df_fixture_quarter = pd.read_csv("df_fixture_quarter.csv")
df_fixture_semi = pd.read_csv("df_fixture_semi.csv")
df_fixture_final = pd.read_csv("df_fixture_final.csv")
df_europe_history = pd.read_csv("uefa_euro_all_data.csv")

# Function to display group standings
def display_group_standings(group_name):
    st.write(f"## {group_name} Standings")
    st.dataframe(dict_table[group_name])

# Function to display knockout fixtures with year formatted as integer
def display_knockout_fixtures(stage_name, df_fixture):
    # Format the 'year' column as integer
    formatted_df = df_fixture.copy()
    formatted_df['year'] = formatted_df['year'].astype(str)  # Convert 'year' column to integer

    st.write(f"## {stage_name}")
    # Display the formatted DataFrame
    st.dataframe(formatted_df)

# Function to display team history in Europe Championship
def display_team_history(team, year):
    st.write(f"## {team} History in Europe Championship ({year})")
    filtered_data = df_europe_history[(df_europe_history['home'] == team) & (df_europe_history['year'] == year)]
    filtered_data['year'] = filtered_data['year'].astype(str)  # Convert 'year' column to integer
    st.dataframe(filtered_data)


# Streamlit application layout
st.title("Euro 2024 Football Championship Prediction")

# Sidebar navigation
st.sidebar.title("Navigation")
stage = st.sidebar.radio("Go to", ["Group Stage", "Round of 16", "Quarterfinals", "Semifinals", "Final", "Team History"])

# Content display based on selection
if stage == "Group Stage":
    group = st.sidebar.selectbox("Select Group", list(dict_table.keys()))
    display_group_standings(group)
elif stage == "Round of 16":
    display_knockout_fixtures("Round of 16", df_fixture_knockout_copy)
elif stage == "Quarterfinals":
    display_knockout_fixtures("Quarterfinals", df_fixture_quarter)
elif stage == "Semifinals":
    display_knockout_fixtures("Semifinals", df_fixture_semi)
elif stage == "Final":
    display_knockout_fixtures("Final", df_fixture_final)
elif stage == "Team History":
    st.sidebar.subheader("Select Team and Year")
    team = st.sidebar.selectbox("Select Team", df_europe_history['home'].unique())
    year = st.sidebar.selectbox("Select Year", df_europe_history['year'].unique())
    display_team_history(team, year)
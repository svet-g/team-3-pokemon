import streamlit as st 
import pandas as pd
import display_image as di
import graph
import more_graphs

#Set screen with
st.set_page_config(layout="wide", initial_sidebar_state="expanded")

#Set title of app
st.title("Pick-Your-Pokemon")

#Display a simple message
st.write("Welcome to the Pick-Your-Pokemon app. Select your favourite pokemon to discover more about them :)")

# Import some data into a Panda Dataframe
df = pd.read_csv("pokemon.csv")

pokemon = df["name"].to_list()

option = st.selectbox(
    "What pokemon do you want?",
    pokemon
)

st.write(f"You selected: {option}")

pokemon_row = df.loc[df["name"] == option]

st.metric(label="Weight (kg)", value=pokemon_row["weight_kg"].values[0])
st.metric(label="Height (m)", value=pokemon_row["height_m"].values[0])
st.metric(label="Main Ability", value=pokemon_row["ability_1"].values[0])

# call display picture function
di.view_image(df, option, pokemon)

# df of the pokemon being compared against

others_df = df[df["name"] != option].sample(10, random_state=None)

# display graph of weight vs height
graph.show_graph(df, option, others_df)

# display more graphs
more_graphs.show_more_graphs(df, option, others_df)
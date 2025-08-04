import streamlit as st 
import pandas as pd
import display_image as di
import graph

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

# display graph of weight vs height
graph.show_graph(df, option)

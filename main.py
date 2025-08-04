import streamlit as st 
import pandas as pd
import display_image as di
import graph
import more_graphs

# streamlit page config
st.set_page_config(page_title="Pick-Your-Pokémon App", layout="centered")

st.markdown("""<HR>""", unsafe_allow_html=True,)

# Set title of app
st.title("Pick-Your-Pokémon")

# Display a simple message
st.markdown(
    '''<h2 style="color: darkslategray;">Welcome to the Pick-Your-Pokémon app.</h2>
    <h4 style="color: darkslategray;">
    Select your favourite Pokémon to discover more 
    about them :)</a></h4>
    ''',
    unsafe_allow_html=True
    )

# Import some data into a Panda Dataframe
df = pd.read_csv("pokemon.csv")

pokemon = df["name"].to_list()

st.markdown("""<HR>""", unsafe_allow_html=True,)

col1, col2 = st.columns(2, gap="large", vertical_alignment="top")

st.markdown("""<HR>""", unsafe_allow_html=True,)

with col1:    
    st.markdown(
        '''
        <p></p>
        <h5>What Pokémon do you want to learn more about?</h5>''',
        unsafe_allow_html=True
        )
    
    option = st.selectbox(
        ' ',
        pokemon
        )

    pokemon_row = df.loc[df["name"] == option] 
      
    st.markdown('<BR>', unsafe_allow_html=True)
    st.metric(label="Weight (kg)", value=pokemon_row["weight_kg"].values[0])
    st.metric(label="Height (m)", value=pokemon_row["height_m"].values[0])
    st.metric(label="Main Ability", value=pokemon_row["ability_1"].values[0])
    
    optional_col = list()

    for col in df.columns:
        if col not in ["name", "weight_kg", "height_m", "ability_1", "Unnamed: 0", "pokedex_number"]:
            optional_col.append(col)        

    #st.write("More attributes?")
    new_field = st.selectbox(
        "Choose additional attributes to display:",
        optional_col
    )
  
    
with col2:
    st.markdown('<BR>', unsafe_allow_html=True)
    # call display picture function
    di.view_image(df, option, pokemon)
    st.markdown('<BR>', unsafe_allow_html=True)
    st.markdown('<BR>', unsafe_allow_html=True)
    st.metric(label=new_field.replace("_", " ").title(), value=pokemon_row[new_field].values[0])

# df of the pokemon being compared against

others_df = df[df["name"] != option].sample(25, random_state=None)

# display graph of weight vs height
graph.show_graph(df, option, others_df)

st.markdown("""<HR>""", unsafe_allow_html=True,)

# display more graphs
more_graphs.show_more_graphs(df, option, others_df)
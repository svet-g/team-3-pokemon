import streamlit as st 
import pandas as pd
import display_image as di
import graph

st.markdown("""<HR>""", unsafe_allow_html=True,)

# Set title of app
st.title("Pick-Your-Pokemon")

# Display a simple message
st.markdown(
    '''<h2 style="color: darkslategray;">Welcome to the Pick-Your-Pokemon app.</h2>
    <h4 style="color: darkslategray;">
    Select your favourite pokemon to discover more 
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
        <h5>What pokemon do you want?</h5>''',
        unsafe_allow_html=True
        )
    
    option = st.selectbox(
        ' ',
        pokemon
        )

    pokemon_row = df.loc[df["name"] == option] 
      
    st.markdown('<BR>', unsafe_allow_html=True)
    # st.markdown("""<HR>""", unsafe_allow_html=True,)
    st.metric(label="Weight (kg)", value=pokemon_row["weight_kg"].values[0])
    st.metric(label="Height (m)", value=pokemon_row["height_m"].values[0])
    st.metric(label="Main Ability", value=pokemon_row["ability_1"].values[0])

with col2:
    # st.markdown('''<h3 style="color: darkslategray;">You selected:</h3>''',
    #             unsafe_allow_html=True
    #             )
    # st.markdown(f'''<h4 style="color: darkslategray;">{option}</h4>''',
    #             unsafe_allow_html=True
    #             )
    # st.markdown("""<HR>""", unsafe_allow_html=True,)
    st.markdown('<BR>', unsafe_allow_html=True)
    # call display picture function
    di.view_image(df, option, pokemon)

# display graph of weight vs height
graph.show_graph(df, option)

st.markdown("""<HR>""", unsafe_allow_html=True,)
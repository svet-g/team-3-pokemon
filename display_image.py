# import pandas as pd
import streamlit as st
import random


def view_image(pokemon_df, options, my_list):
    '''
    Displays pokemon image from free to use PokéAPI images
    \nTo call display picture function use:
    \ndisplay_image.view_image(df, option, pokemon)
    
    Args:
        pokemon_df → full pokemon dataframe
        options → selected pokemon 'name' from pokemon_df dataframe
        my_list → pokemon_df 'nme' columnt .to_list()

    Returns:
        None. Simply displays the image.
    '''

    if len(options) > 0:
        # find the pokedex number in the selected pokemon row
        my_mask = pokemon_df['name'] == options
        selectedpokemon_df = pokemon_df[my_mask]
        pokedex_number = selectedpokemon_df['pokedex_number'].to_list()
        pokedex_number = pokedex_number[0]
        # display the selected pokemon image
        st.image(
            'https://raw.githubusercontent.com/PokeAPI/sprites/master/' +
            f'sprites/pokemon/other/official-artwork/{pokedex_number}.png',
            use_container_width=True,
        )
    else:  # in case nothing selected - display random pokemon
        pokedex_number = random.randint(0, len(my_list))
        st.subheader(f'Randomly selected {options} displayed')
        st.image(
            'https://raw.githubusercontent.com/PokeAPI/sprites/master/' +
            f'sprites/pokemon/other/official-artwork/{pokedex_number}.png',
            use_container_width=True,
        )

    st.write(
        'Ⓒ PokéAPI is free and open to use. ' +
        'All images subject to fair use policy.',
        )

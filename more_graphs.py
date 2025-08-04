import seaborn as sns
import pandas as pd
import streamlit as st


# Load the example planets dataset

def show_more_graphs(df, chosen_pokemon, other_pokemon):
    
    sns.set_theme(style="whitegrid")
    sns.set(font_scale=0.7)
    
    st.subheader("Pokémon Attack and Defense Attributes by Status")
    
    chosen_pokemon_df = df[df["name"] == chosen_pokemon]
    concat_df = pd.concat([chosen_pokemon_df, other_pokemon])
    cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)
    g = sns.relplot(
        data=concat_df,
        x="status", y="name",
        hue="attack", size="defense",
        palette=cmap, sizes=(10, 120),
    )
    g.ax.xaxis.grid(True, "minor", linewidth=.25)
    g.ax.yaxis.grid(True, "minor", linewidth=.25)
    g.despine(left=True, bottom=True)
    return st.pyplot(g)
import streamlit as st
import pandas as pd
import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt 
import random

def show_graph(df, selected_name, others_df):
    st.set_page_config(page_title="Pokémon Height vs Weight", layout="centered")
    st.subheader("Pokémon Height vs Weight (from CSV)")

    main_pokemon = df[df["name"] == selected_name].iloc[0]
    main_height = main_pokemon["height_m"]
    main_weight = main_pokemon["weight_kg"]
        
    def compare_with_random(main_height, main_weight, main_name, df, others_df):
        
        heights = others_df["height_m"].tolist()
        weights = others_df["weight_kg"].tolist()
        names = others_df["name"].tolist()

        # Add main Pokémon info
        heights.append(main_height)
        weights.append(main_weight)
        names.append(f"{main_name} (You)")
        
        fig, ax = plt.subplots()
        ax.scatter(heights[:-1], weights[:-1], label="Other Pokémon", color="blue")
        ax.scatter(heights[-1], weights[-1], label=names[-1], color="red", s=100)
        
        ax.set_xlabel("Height (m)")
        ax.set_ylabel("Weight (kg)")
        ax.set_title("Height vs Weight Comparison")
        ax.legend()
        return fig

    if selected_name:
        fig = compare_with_random(main_height, main_weight, selected_name, df, others_df)
        st.pyplot(fig)
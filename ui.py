import streamlit as st
import requests
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# FastAPI endpoint
API_URL = "http://127.0.0.1:8000/optimize"

st.title("Furniture Arrangement Optimizer")

# User inputs for room size and furniture count
room_width = st.number_input("Room Width", min_value=5, max_value=20, value=10)
room_height = st.number_input("Room Height", min_value=5, max_value=20, value=10)
furniture_count = st.number_input("Number of Furniture Items", min_value=1, max_value=10, value=3)

if st.button("Optimize Layout"):
    # Call FastAPI
    response = requests.post(API_URL, json={"width": room_width, "height": room_height, "num_furniture": furniture_count})
    
    if response.status_code == 200:
        layout = response.json()["layout"]
        st.success("Layout optimized successfully!")

        # Plot the layout
        fig, ax = plt.subplots()
        ax.set_xlim(0, layout["width"])
        ax.set_ylim(0, layout["height"])
        ax.set_xticks(range(layout["width"] + 1))
        ax.set_yticks(range(layout["height"] + 1))
        ax.grid(True)
        
        for item in layout["furniture"]:
            rect = patches.Rectangle((item["x"], item["y"]), item["width"], item["height"], linewidth=1, edgecolor='r', facecolor='blue', alpha=0.5)
            ax.add_patch(rect)
            ax.text(item["x"] + 0.2, item["y"] + 0.2, item["name"], fontsize=8, color='white')
        
        st.pyplot(fig)
    else:
        st.error("Error optimizing layout. Check API connection.")

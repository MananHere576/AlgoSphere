# utils/chart.py

import matplotlib.pyplot as plt
import streamlit as st

# Function to generate Pie chart for Hits/Misses
def generate_pie_chart(hits, misses):
    labels = ['Hits', 'Misses']
    sizes = [hits, misses]
    colors = ['#00FF00', '#FF0000']
    
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle.
    
    st.pyplot(fig)

# Function to generate Gantt chart
def generate_gantt_chart(gantt_data):
    fig, ax = plt.subplots(figsize=(10, 3))
    
    for i, (start, end, process) in enumerate(gantt_data):
        ax.barh(process, end - start, left=start, height=0.5, color='skyblue')

    ax.set_xlabel('Time')
    ax.set_ylabel('Processes')
    ax.set_title('Gantt Chart')
    st.pyplot(fig)

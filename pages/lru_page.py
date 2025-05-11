# pages/lru_page.py

import streamlit as st
import pandas as pd
from algorithms.lru import lru_algorithm
from utils.chart import generate_pie_chart

def show_lru_page():
    st.title("📄 LRU (Least Recently Used) Page Replacement Algorithm")
    st.write("""
    ## 📚 About LRU:
    **Least Recently Used (LRU)** is a page replacement algorithm that replaces the page that has not been used for the longest time.

    ### ⚙️ How it works:
    - Pages are loaded into memory frames.
    - When a page fault occurs and memory is full, the page **least recently accessed** is replaced.
    - Pages accessed recently are given higher priority to stay in memory.
    
    This approach tries to mimic real-world usage where pages used recently are more likely to be used again soon. 📈
    """)

    st.subheader("🛠️ Input Parameters")
    frame_size = st.number_input("🔢 Frame Size:", min_value=1, max_value=10, value=3)
    page_references = st.text_area("📝 Page References (comma-separated):", "7,0,1,2,0,3,0,4,2,3,0,3,2")

    if st.button("▶️ Run LRU Algorithm"):
        page_references = list(map(int, page_references.split(',')))

        # Run LRU algorithm
        hits, misses, page_frames = lru_algorithm(frame_size, page_references)

        # Prepare the transitions data correctly
        data = {
            "Step": [],
            "Page Reference": [],
            "Memory Frames": [],
            "Hit/Miss": []
        }

        memory_set = set()  # Track pages currently in memory
        for i, frame in enumerate(page_frames):
            current_page = page_references[i]
            hit = current_page in memory_set  # Check BEFORE updating memory

            data["Step"].append(i + 1)
            data["Page Reference"].append(current_page)
            data["Memory Frames"].append(str(frame))
            data["Hit/Miss"].append("✅ Hit" if hit else "❌ Miss")

            memory_set = set(frame)  # Update memory after processing

        df = pd.DataFrame(data)

        st.subheader("🔍 Step-by-Step Page Frame Transitions")
        st.table(df)

        st.subheader("📊 Results Summary")
        total_references = len(page_references)
        hit_ratio = hits / total_references
        miss_ratio = misses / total_references

        st.write(f"**📌 Total Page References:** {total_references}")
        st.write(f"**✅ Total Hits:** {hits}")
        st.write(f"**❌ Total Misses (Page Faults):** {misses}")
        st.write(f"**📈 Hit Ratio:** {hit_ratio:.2f}")
        st.write(f"**📉 Miss Ratio:** {miss_ratio:.2f}")

        # Pie Chart of Hits and Misses
        generate_pie_chart(hits, misses)

if __name__ == "__main__":
    show_lru_page()

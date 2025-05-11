import streamlit as st
import pandas as pd
from algorithms.fifo import fifo_algorithm
from utils.chart import generate_pie_chart

def show_fifo_page():
    st.title("FIFO (First In First Out) - Page Replacement Algorithm")
    st.write("""
    ### 📚 What is FIFO?
    **First-In-First-Out (FIFO)** is the simplest page replacement algorithm.  
    When a page needs to be replaced, the page that has been in memory the longest (i.e., the oldest page) is selected.

    ---
    ### 🔥 How FIFO Works (Step-by-Step):
    - **Page Hit**: If the page is already in memory, no replacement is needed.
    - **Page Fault**: If the page is not in memory:
        - If there’s space available, load the page directly.
        - Otherwise, **replace the page that arrived first** (oldest page).

    - FIFO uses a **queue** structure: first page in → first page out.
    ---
    """)

    # Inputs
    frame_size = st.number_input("🗃️ Enter Frame Size:", min_value=1, max_value=10, value=3)
    page_references = st.text_area("📝 Enter Page Reference String (comma-separated):", "1,2,3,4,1,2,5,1,2,3")

    if st.button("🚀 Run FIFO Algorithm"):
        # Preprocessing input
        page_references = list(map(int, page_references.split(',')))

        # Run FIFO algorithm
        hits, misses, page_frames = fifo_algorithm(frame_size, page_references)

        # Displaying Results
        st.subheader("📋 Step-by-Step Page Frame Status:")

        # Prepare data for table
        table_data = {
            "Step": [],
            "Page Requested": [],
            "Frame Status": [],
            "Result (Hit/Miss)": []
        }

        frames_set = set()
        for i, frame in enumerate(page_frames):
            page = page_references[i]
            if page in frames_set:
                result = "Hit ✅"
            else:
                result = "Miss ❌"
                frames_set.add(page)
                if len(frames_set) > frame_size:
                    frames_set = set(frame)
            table_data["Step"].append(i + 1)
            table_data["Page Requested"].append(page)
            table_data["Frame Status"].append(frame)
            table_data["Result (Hit/Miss)"].append(result)

        df = pd.DataFrame(table_data)
        st.dataframe(df, use_container_width=True)

        # Final Results
        st.subheader("📈 Summary:")
        total_requests = len(page_references)
        hit_ratio = hits / total_requests
        miss_ratio = misses / total_requests

        st.markdown(f"- **Total Requests:** `{total_requests}`")
        st.markdown(f"- **Total Hits:** `{hits}`")
        st.markdown(f"- **Total Misses:** `{misses}`")
        st.markdown(f"- **Hit Ratio:** `{hit_ratio:.2f}`")
        st.markdown(f"- **Miss Ratio:** `{miss_ratio:.2f}`")

        # Pie Chart Visualization
        st.subheader("🎯 Hit vs Miss Visualization:")
        generate_pie_chart(hits, misses)

# Run the page
if __name__ == "__main__":
    show_fifo_page()

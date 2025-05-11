# pages/optimal_page.py

import streamlit as st
from algorithms.optimal import optimal_algorithm
from utils.chart import generate_pie_chart

def show_optimal_page():
    st.title("🖼️Optimal Page Replacement Algorithm")
    st.write("""
    **Optimal Page Replacement Algorithm** 🧠 is the ideal page replacement strategy that **minimizes page faults** by selecting the page that will not be used for the longest period of time in the future.

    **How it works:**
    - When a page needs to be loaded into memory but there is no free space, the **optimal algorithm** selects the page to replace based on future reference.
    - It **looks ahead** through the list of page references and selects the page that is referenced **last** (i.e., the one that will not be needed for the longest time).
    - This algorithm is considered the **best** in terms of performance, as it leads to the **fewest page faults**. 📈

    **Example:**
    Imagine a situation where you have three memory frames and a sequence of page references. When a new page needs to be loaded into one of the frames, the algorithm looks ahead at the future references and replaces the page that will not be used for the longest period of time. This reduces the number of page faults, which is the goal of any page replacement algorithm. 👀💡

    **However**, despite its theoretical optimality, the **Optimal Algorithm is not practical** in real-world systems, as it requires **future knowledge of page references**. This would be impossible to implement in most cases since we cannot predict the future. 📅🔮

    Nonetheless, it serves as a **benchmark** to compare other, more practical algorithms, such as FIFO and LRU, which make decisions based on past page accesses. 🔄

    ### Key Characteristics:
    - **Minimizes page faults** to the theoretical minimum.
    - Requires **future knowledge of page accesses**, making it impractical for real-time systems.
    - Used primarily as a reference or benchmark for comparing other algorithms.

    Now, let's dive in and see how the Optimal Page Replacement Algorithm performs with your inputs! 🎮
    """)

    # Input fields for frame size and page references
    frame_size = st.number_input("🖼 Frame Size:", min_value=1, max_value=10, value=3)
    page_references = st.text_area("📜 Page References (comma-separated):", "1,2,3,4,1,2,5,1,2,3")

    if st.button("🔄 Run Optimal Algorithm"):
        # Convert page references to a list of integers
        page_references = list(map(int, page_references.split(',')))

        # Run Optimal algorithm
        hits, misses, page_frames = optimal_algorithm(frame_size, page_references)

        # Display Hits and Misses count
        st.write(f"✅ **Hits**: {hits}  |  ❌ **Misses (Page Faults)**: {misses}")
        
        # Page Frame Transitions Table
        st.subheader("🔍 Step-by-Step Page Frame Transitions")
        page_transitions = []
        for i, frame in enumerate(page_frames):
            page_transitions.append([i, page_references[i], frame, "✅ Hit" if i < hits else "❌ Miss"])
        
        # Display transitions in a table
        st.table(page_transitions)

        # Results Summary Section
        st.subheader("📊 Results Summary")
        st.write(f"📌 **Total Page References**: {len(page_references)}")
        st.write(f"✅ **Total Hits**: {hits}")
        st.write(f"❌ **Total Misses (Page Faults)**: {misses}")
        
        # Calculate and display Hit/Miss ratio
        hit_ratio = hits / len(page_references)
        miss_ratio = misses / len(page_references)
        st.write(f"📈 **Hit Ratio**: {hit_ratio:.2f}")
        st.write(f"📉 **Miss Ratio**: {miss_ratio:.2f}")

        # Generate Pie Chart for Hits and Misses
        generate_pie_chart(hits, misses)

# Run the page
if __name__ == "__main__":
    show_optimal_page()

# algorithms/lru.py

def lru_algorithm(frame_size, page_references):
    frames = []
    page_faults = 0
    hits = 0
    page_frames = []
    page_order = []

    for page in page_references:
        if page not in frames:
            if len(frames) < frame_size:
                frames.append(page)
            else:
                # Remove the least recently used page
                lru = page_order.pop(0)
                frames.remove(lru)
                frames.append(page)
            page_faults += 1
        else:
            hits += 1
        
        # Track page order for LRU
        if page in page_order:
            page_order.remove(page)
        page_order.append(page)
        
        page_frames.append(list(frames))

    misses = page_faults
    return hits, misses, page_frames

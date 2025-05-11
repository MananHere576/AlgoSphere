# algorithms/fifo.py

def fifo_algorithm(frame_size, page_references):
    frames = []
    page_faults = 0
    hits = 0
    page_frames = []

    for page in page_references:
        if page not in frames:
            if len(frames) < frame_size:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)
            page_faults += 1
        else:
            hits += 1
        
        page_frames.append(list(frames))

    misses = page_faults
    return hits, misses, page_frames

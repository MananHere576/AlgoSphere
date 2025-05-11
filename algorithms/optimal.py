# algorithms/optimal.py

def optimal_algorithm(frame_size, page_references):
    frames = []
    page_faults = 0
    hits = 0
    page_frames = []

    for i in range(len(page_references)):
        page = page_references[i]
        
        if page not in frames:
            if len(frames) < frame_size:
                frames.append(page)
            else:
                # Find the page that will not be used for the longest time
                farthest = -1
                index_to_replace = -1
                for j in range(len(frames)):
                    try:
                        next_use = page_references[i+1:].index(frames[j])
                    except ValueError:
                        next_use = float('inf')
                    if next_use > farthest:
                        farthest = next_use
                        index_to_replace = j
                frames[index_to_replace] = page
            page_faults += 1
        else:
            hits += 1
        
        page_frames.append(list(frames))

    misses = page_faults
    return hits, misses, page_frames

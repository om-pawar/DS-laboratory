def keyword_counter(text):
    freq_table = {}  # Hash Table
    words = text.lower().split()
    
    for word in words:
        freq_table[word] = freq_table.get(word, 0) + 1
        
    for k, v in freq_table.items():
        print(f"'{k}': {v}")

if __name__ == "__main__":
    text = "data structures and data algorithms"
    keyword_counter(text)

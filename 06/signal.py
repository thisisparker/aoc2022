def find_isogrammatic_chunk_ending_index(length, signal):
    for i in range(length, len(signal)):
        chunk = signal[i-length:i]
        if len(set(chunk)) == length:
            return i

def main():
    with open('input') as f:
        signal = f.read().strip()

    print(find_isogrammatic_chunk_ending_index(4, signal))
    print(find_isogrammatic_chunk_ending_index(14, signal))

if __name__ == '__main__':
    main()

def generate_candidate_gRNAs(sequence):
    return [sequence[i:i+20] for i in range(len(sequence) - 20)]

def slices(series, length):
    if length == 0: raise ValueError("slice length cannot be zero")
    if length < 0: raise ValueError("slice length cannot be negative")
    if len(series) == 0: raise ValueError("series cannot be empty")
    if len(series) < length: raise ValueError("slice length cannot be greater than series length")

    return [series[start:start+length] for start in range(len(series) - length + 1)]
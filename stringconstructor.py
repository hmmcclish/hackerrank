def stringConstruction(s):
    string_set = set(s)
    return len(string_set)

if __name__ == "__main__":
    string_inputs = []
    q = int(raw_input().strip())
    for a0 in xrange(q):
        s = raw_input().strip()
        string_inputs.append(s)
    for x in string_inputs:
        print stringConstruction(x)

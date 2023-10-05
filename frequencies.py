def frequencies(items):
    frequencies = {};
   
    for i in range (len(items)):
        items[i] = str(items[i]);
        frequencies[items[i]] = 1;
        count = 0;
        for j in range (len(items)):
            if items[i] == items[j]:
                count = count + 1;
                frequencies[items[i]] = count;
                
    return frequencies

def is_pangram(st):
    sentence = st.lower()
    sentence_list = []
    i=0
    j=0
    k=0
    count = 1
    
    for i in range(len(sentence)):
        sentence_list.append(sentence[i])
        if ((sentence[i] == " ") or (sentence[i] == "?") or (sentence[i] == "!"))  :
            continue
        
    while count != len(sentence):
        while k < len(sentence):
            if sentence[j] != sentence [k]:
                print (sentence[j])
                print (sentence[k])
                k+=1
            elif sentence[j] == sentence [k]:
                print(False)
                break
        k=0
        j+=1
        count+=1

    if count == len(sentence):
        print(True)



is_pangram("This isn't a pangram!")
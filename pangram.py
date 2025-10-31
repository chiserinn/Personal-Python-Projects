def is_pangram(st):
    sentence = st.lower()
    sentence_list = []
    i=0
    j=0
    k=0
    current_verdict = None
    
    for i in range(len(sentence)):
        sentence_list.append(sentence[i])
        if ((sentence[i] == " ") or (sentence[i] == "?") or (sentence[i] == "!"))  :
            continue
    
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    
    while k != (len(alphabet)):
        print(sentence_list[j])
        print(alphabet[k])
        
        if alphabet[k] == sentence[j]:
            current_verdict = True
            k+=1
            j=0
        else:
            j+=1
        
        
        if j == len(sentence):
            current_verdict = False
            return (current_verdict)
            

    if k == len(alphabet):
        return (current_verdict)

    


is_pangram("This isn't a pangram!")
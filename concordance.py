import string

punctuations = ["[", "]", "(", ")", "{", "}", "<", ">", \
         ":", ";", ",", "`", "'", "\"", "-", ".", \
         "|", "\\", "?", "/", "!", "-", "_", "@", \
         "\#", "$", "%", "^", "&", "*", "+", "~", "=", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
punctuationmiddle = ["[", "]", "(", ")", "{", "}", "<", ">", \
         ":", ";", ",", "`", "\"",  ".", \
         "|", "\\", "?", "/", "!", "_", "@", \
         "\#", "$", "%", "^", "&", "*", "+", "~", "=", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
         
def check(word):
    newword = ""
    for alpha in word:
        
        if alpha in punctuationmiddle:
            
            newword = newword + ""
        else:
            newword = newword + alpha
    return(newword)
    
    
def removepunc(line):
    data1 = line.split()
    word_list = []
    for word in data1:
    
        if len(word) == 1 and word[0] in punctuations:
            continue
        
        elif word[0] in punctuations:
            word = word[1:]
            if word[-1] in punctuations:
                word = word[:-1]
        elif word[-1] in punctuations:
            word = word[:-1]
    
        x = check(word)
        word_list.append(x)
    return word_list

def concordance(file, unique):
    if unique == True:
        with open('test.txt') as fp:
            lines = fp.read().split("\n")
        line_count = 1 
        word_dict = {}
        for line in lines:
            words_without_punc = removepunc(line)
            
            for word in words_without_punc:
                if (word.lower() in word_dict) and not(line_count in word_dict[word.lower()]):
                    word_dict[word.lower()].append(line_count)
                else:
                    word_dict[word.lower()] = [line_count]
            line_count += 1
        return word_dict
    else:
        
        with open('test.txt') as fp:
            lines = fp.read().split("\n")
        line_count = 1 
        word_dict = {}
        for line in lines:
            words_without_punc = removepunc(line)
            
            for word in words_without_punc:
                if word.lower() in word_dict:
                    word_dict[word.lower()].append(line_count)
                else:
                    word_dict[word.lower()] = [line_count]
            line_count += 1
        return word_dict


if __name__ == "__main__":
    output = concordance("test.txt", unique = True)
    
    print(output)
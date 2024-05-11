import operator
      
def symbols_Clean(all_words):
    no_symbol=[]
    symbols="“’—,.é!^+%&/()=?_<>£#$½{[]}\|@-*:;æß"+"1234567890"+chr(775)+chr(34)#symbols and numbers i want removed
    for word in all_words:
        for symbol in symbols:
            if symbol in word:
                symbol_index=word.index(symbol)
                word=word.replace(symbol," ")
                word=word[0:symbol_index]
        if (len(word)>0):
            no_symbol.append(word)
    return no_symbol

def stopwords(all_words):
    clean=[]
    #I wrote a function to delete stopwords
    stopwords = {"able","about","above","abroadaccording","accordingly","across","actually","adj","after","afterwards","again",
                 "against","agoahead","ain't","all","allow","allows","almost","alone","along","alongside","already","also","although","always",
                 "am","amid","amidst","among","amongst","an","and","another","any","anybody","anyhow","anyone","anything","anyway","anyways",
                 "anywhere","apart","appear","appreciate","appropriate","are","aren't","around","as","a's","aside","ask","asking","associated",
                 "at","available","away","awfully","back","backward","backwards","be","became","because","become","becomes","becoming",
                 "been","before","beforehand","begin","behind","being","believe","below","beside","besides","best","better","between",
                 "beyond","both","brief","but","by","came","can","cannot","cant","can't","caption","cause","causes","certain","certainly",
                 "changes","clearly","c'mon","co","co.","com","come","comes","concerning","consequently","consider","considering","contain",
                 "containing","contains","corresponding","could","couldn't","course","c's","currently","dare","daren't","definitely","described",
                 "despite","did","didn't","different","directly","do","does","doesn't","doing","done","don't","down","downwards","during","each",
                 "edu","eg","eight","eighty","either","else","elsewhere","end","ending","enough","entirely","especially","et","etc","even","ever",
                 "evermore","every","everybody","everyone","everything","everywhere","ex","exactly","example","except","fairly","far","farther",
                 "few","fewer","fifth","first","five","followed","following","follows","for","forever","former","formerly","forth","forward",
                 "found","four","from","further","furthermore","get","gets","getting","given","gives","go","goes","going","gone","got","gotten",
                 "greetings","had","hadn't","half","happens","hardly","has","hasn't","have","haven't","having","he","he'd","he'll","hello","help",
                 "hence","her","here","hereafter","hereby","herein","here's","hereupon","hers","herself","he's","hi","him","himself","his","hither",
                 "hopefully","how","howbeit","however","hundred","i'd","ie","if","ignored","i'll","i'm","immediate","in","inasmuch","inc","inc.",
                 "indeed","indicate","indicated","indicates","inner","inside","insofar","instead","into","inward","is","isn't","it","it'd","it'll",
                 "its","it's","itself","i've","just","k","keep","keeps","kept","know","known","knows","last","lately","later","latter","latterly","least",
                 "less","lest","let","let's","like","liked","likely","likewise","little","look","looking","looks","low","lower","ltd","made","mainly",
                 "make","makes","many","may","maybe","mayn't","me","mean","meantime","meanwhile","merely","might","mightn't","mine","minus","miss",
                 "more","moreover","most","mostly","mr","mrs","much","must","mustn't","my","myself","name","namely","nd","near","nearly","necessary",
                 "need","needn't","needs","neither","never","neverf","neverless","nevertheless","new","next","nine","ninety","no","nobody","non",
                 "none","nonetheless","noone","no-one","nor","normally","not","nothing","notwithstanding","novel","now","nowhere","obviously","of",
                 "off","often","oh","ok","okay","old","on","once","one","ones","one's","only","onto","opposite","or","other","others","otherwise",
                 "ought","oughtn't","our","ours","ourselves","out","outside","over","overall","own","particular","particularly","past","per","perhaps",
                 "placed","please","plus","possible","presumably","probably","provided","provides","que","quite","qv","rather","rd","re","really","reasonably",
                 "recent","recently","regarding","regardless","regards","relatively","respectively","right","round","said","same","saw","say","saying",
                 "says","second","secondly","see","seeing","seem","seemed","seeming","seems","seen","self","selves","sensible","sent","serious","seriously",
                 "seven","several","shall","shan't","she","she'd","she'll","she's","should","shouldn't","since","six","so","some","somebody","someday",
                 "somehow","someone","something","sometime","sometimes","somewhat","somewhere","soon","sorry","specified","specify","specifying","still",
                 "sub","such","sup","sure","take","taken","taking","tell","tends","th","than","thank","thanks","thanx","that","that'll","thats","that's",
                 "that've","the","their","theirs","them","themselves","then","thence","there","thereafter","thereby","there'd","therefore","therein","there'll",
                 "there're","theres","there's","thereupon","there've","these","they","they'd","they'll","they're","they've","thing","things","think","third",
                 "thirty","this","thorough","thoroughly","those","though","three","through","throughout","thru","thus","till","to","together","too","took",
                 "toward","towards","tried","tries","truly","try","trying","t's","twice","two","un","under","underneath","undoing","unfortunately","unless",
                 "unlike","unlikely","until","unto","up","upon","upwards","us","use","used","useful","uses","using","usually","v","value","various","versus",
                 "very","via","viz","vs","want","wants","was","wasn't","way","we","we'd","welcome","well","we'll","went","were","we're","weren't","we've",
                 "what","whatever","what'll","what's","what've","when","whence","whenever","where","whereafter","whereas","whereby","wherein","where's",
                 "whereupon","wherever","whether","which","whichever","while","whilst","whither","who","who'd","whoever","whole","who'll","whom","whomever",
                 "who's","whose","why","will","willing","wish","with","within","without","wonder","won't","would","wouldn't","yes","yet","you","you'd","you'll",
                 "your","you're","yours","yourself","yourselves","you've","zero","a","how's","i","when's","why's",
                 "o","p","q","r","s","t","u","uucp","w","x","y","z","I","www","amount","bill","bottom","call","computer","con","couldnt","cry","de","describe",
                 "detail","due","eleven","empty","fifteen","fifty","fill","find","fire","forty","front","full","give","hasnt","herse","himse","interest","itse”",
                 "mill","move","myse”","part","put","show","side","sincere","sixty","system","ten","thick","thin","top","twelve","twenty","abst","accordance",
                 "act","added","adopted","affected","affecting","affects","ah","announce","anymore","apparently","approximately","aren","arent","arise","auth",
                 "beginning","beginnings","begins","biol","briefly","ca","date","ed","effect","et-al","ff","fix","gave","giving","heres","hes","hid","home",
                 "id","im","immediately","importance","important","index","information","invention","itd","keys","kg","km","largely","lets","line","'ll",
                 "means","mg","million","ml","mug","na","nay","necessarily","nos","noted","obtain","obtained","omitted","ord","owing","page","pages","poorly",
                 "possibly","potentially","pp","predominantly","present","previously","primarily","promptly","proud","quickly","ran","readily","ref","refs","related",
                 "research","resulted","resulting","results","run","sec","section","shed","shes","showed","shown","showns","shows","significant","significantly",
                 "similar","similarly","slightly","somethan","specifically","state","states","stop","strongly","substantially","successfully","sufficiently",
                 "suggest","thered","thereof","therere","thereto","theyd","theyre","thou","thoughh","thousand","throug","til","tip","ts","ups","usefully","usefulness",
                 "'ve","vol","vols","wed","whats","wheres","whim","whod","whos","widely","words","world","youd","youre"}
    
    for word in all_words:
        for i in stopwords:
            if i == word:
                word=word.replace(i,"")#I removed the stopwords
        if (len(word)>1):
            clean.append(word)
    return clean

def dict(all_words):
    #I listed binary words by number.   
    word_number1={}    
    i=0
    ciftkelimeler = []
    while(i<len(all_words)-1):
        ciftkelimeler.append(all_words[i] + " " + all_words[i + 1])
        i+=1   
    for word in ciftkelimeler:
            if word in word_number1:                        
                word_number1[word]+=1#I increased the counter as I found the word               
            else:
                word_number1[word]=1
    return word_number1
    
def dict1(all_words):
    word_number={}
    #I listed the single words by number.
    for word in all_words:
        if word in word_number:
            word_number[word]+=1#I increased the counter as I found the word
        else:
            word_number[word]=1#If there is no word I did not increase
    return word_number

def Word_Order_Frequency_One_Book(book_1, value, result_1):
    
    with open (book_1,"r", encoding = "utf-8-sig") as dosya:
           content=dosya.read()
           all_words=content.lower().split()#I separated the words from each other
           
           
           all_words=symbols_Clean(all_words)
           all_words=stopwords(all_words)
           word_number=dict1(all_words)
           word_number1=dict(all_words)
           
           
    
    if value==1:
           file = open(result_1,"w", encoding = "utf-8-sig")
           file.write("+--------------------------------+\n")
           file.write("|WORD       |WORD                |\n") 
           file.write("|ORDER      |ORDER               |\n")            
           file.write("|FREQUENCY  |SEQUENCE            |\n")  
           file.write("+--------------------------------+\n")    
           file.close()
           b=0
           for key,value in sorted(word_number.items(),key=operator.itemgetter(1),reverse=True):#I sorted the words
               b+=1    
               file = open(result_1,"a", encoding = "utf-8-sig")
               file.write("     ")
               file.write(str(value))
               file.write("          ")
               file.write(str(key))
               file.write("\n")
               file.close()
               
               if (b==100):#When it reached the number I made it exit the loop
                   break    

    if value==2:           
            file = open(result_1,"w", encoding = "utf-8-sig")
            file.write("+--------------------------------+\n")
            file.write("|WORD       |WORD                |\n") 
            file.write("|ORDER      |ORDER               |\n")            
            file.write("|FREQUENCY  |SEQUENCE            |\n")  
            file.write("+--------------------------------+\n")  
            file.close()
            b=0
            for key,value in sorted(word_number1.items(),key=operator.itemgetter(1),reverse=True):#I sorted the words
                b+=1
                file = open(result_1,"a", encoding = "utf-8-sig")
                file.write("     ")
                file.write(str(value))
                file.write("          ")
                file.write(str(key))
                file.write("\n")
                file.close()
    
                if (b==100):#When it reached the number I made it exit the loop
                    break   

def Word_Order_Frequency_Two_Books(book_1, book_2, value, result_2):
    
    with open (book_1,"r", encoding = "utf-8-sig") as dosya:
        content=dosya.read()
        all_words=content.lower().split()#I separated the words from each other
        dosya.close()

    with open (book_2,"r", encoding = "utf-8-sig") as dosya2:
        content2=dosya2.read()
        all_words2=content2.lower().split()#I separated the words from each other
        dosya2.close()

        all_wordssum=all_words+all_words2 #I combined the words of the first book and the second book
        
        #i called the functions
        all_wordssum=symbols_Clean(all_wordssum)
        all_wordssum=stopwords(all_wordssum)
        word_numbersum1=dict1(all_wordssum)
        word_numbersum2=dict(all_wordssum)
        word_number=dict1(all_words)
        word_number1=dict1(all_words2)
        word_number2=dict(all_words)
        word_number3=dict(all_words2)
        
    if value == 1:
        
           
        file = open(result_2,"w", encoding = "utf-8-sig")
        file.write("+--------------------------------------------------------+\n") 
        file.write("|TOTAL     |BOOK 1    |BOOK 2    |WORD                   |\n") 
        file.write("|ORDER     |ORDER     |ORDER     |ORDER                  |\n") 
        file.write("|FREQUENCY |FREQUENCY |FREQUENCY |SEQUENCE               |\n") 
        file.write("+--------------------------------------------------------+\n")
        file.close() 
        b=0
        for keysum,value in sorted(word_numbersum1.items(),key=operator.itemgetter(1),reverse=True):
            b+=1
            file = open(result_2,"a", encoding = "utf-8-sig")
            file.write("    ")
            file.write(str(value))
            file.write("         ")
            if keysum in word_number:
                file.write(str(word_numbersum1[keysum]))  
            else:
                file.write("0")  
            file.write("          ")    
            if keysum in word_number1:
                file.write(str(word_numbersum1[keysum]))  
            else:
                file.write("0")  
            file.write("        ")
            file.write(str(keysum))
            file.write("\n")
            file.close()
                
            if (b==100):
                break 

    if value == 2:
        
                    
        file = open(result_2,"w", encoding = "utf-8-sig")
        file.write("+--------------------------------------------------------+\n") 
        file.write("|TOTAL     |BOOK 1    |BOOK 2    |WORD                   |\n") 
        file.write("|ORDER     |ORDER     |ORDER     |ORDER                  |\n") 
        file.write("|FREQUENCY |FREQUENCY |FREQUENCY |SEQUENCE               |\n") 
        file.write("+--------------------------------------------------------+\n") 
        file.close()
        b=0
        for keysum,value in sorted(word_numbersum2.items(),key=operator.itemgetter(1),reverse=True):
            b+=1
            file = open(result_2,"a", encoding = "utf-8-sig")
            file.write("    ")
            file.write(str(value))
            file.write("         ")
            if keysum in word_number2:
                file.write(str(word_numbersum2[keysum]))  
            else:
                file.write("0")  
            file.write("          ")    
            if keysum in word_number3:
                file.write(str(word_numbersum2[keysum]))  
            else:
                file.write("0")  
            file.write("        ")
            file.write(str(keysum))
            file.write("\n")
            file.close()
                    
            if (b==100):
                break

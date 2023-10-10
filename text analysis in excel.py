import string
import nltk
import pandas as pd
from nltk.corpus import stopwords

possc_list=[]
negsc_list=[]
polsc_list=[]
subsc_list=[]
wc_list=[]
avsl_list=[]
avgwl_list=[]
avnow_list=[]
compwc_list=[]
sypw_list=[]
fogind_list=[]
prepron_list=[]
perc_cw_list=[]
removepunch = ['“', '”', '...', '©', 'WHAT', 'WE', 'DO', 'THINK', 'Blackcoffer', 'Insights', 'OUR', 'SUCESS', 'STORIES', 'HOW', 'TO', 'SCHEDULE', 'DEMO', 'CONTACT', 'Artificial', 'IntelligenceBig', 'DataData', 'VisualizationMachine', 'LearningWhat', 'We', 'Think''Blackcoffer', 'Insights', '29', 'Sanskriti', 'Sunderum', 'and', 'Aayushi', 'Nauhwar', 'SRCC', 'Delhi', 'University', 'TAGS', 'AI', 'algorithm', 'Covid', 'Healthcare', 'Ml', 'pandemic', 'patient', 'outcomes', 'Previous', 'article', 'What', 'if', 'the', 'Creation', 'is', 'Taking', 'Over', 'the', 'Creator', 'Next', 'article', 'Future', 'of', 'AI', 'and', 'Machine', 'Roles', 'in', 'the', 'Medical', 'Sector', 'RELATED', 'ARTICLESMORE', 'FROM', 'AUTHOR', 'What', 'We', 'Think', 'How', 'does', 'marketing', 'influence', 'businesses', 'and', 'consumers', 'Marketing', 'How', 'advertisement', 'increase', 'your', 'market', 'value', 'What', 'We', 'Think', 'Negative', 'effects', 'of', 'marketing', 'on', 'society', 'Advertisement', 'MOST', 'POPULAR', 'INSIGHTS', 'Rising', 'IT', 'cities', 'will', 'impact', 'the', 'economy', 'environment', 'infrastructure', 'and', 'city', 'October', '17', '2022', 'Online', 'gaming', 'Adolescent', 'online', 'gaming', 'effects', 'demotivated', 'depression', 'musculoskeletal', 'and', 'psychosomatic', 'June', '23', '2020', 'Coronavirus', 'Effect', 'on', 'the', 'Hospitality', 'Industry', 'April', '30', '2020', 'Big', 'Data', 'Analytics', 'through', 'IoT', 'in', 'Oil', 'and', 'Gas', 'Industry', 'September', '10', '2018', 'Load', 'more', 'RECOMMENDED', 'INSIGHTS', 'Our', 'Success', 'Stories', 'Power', 'BI', 'Data-Driven', 'Map', 'Dashboard', 'Our', 'Success', 'Stories', 'Construction', 'Accounts', 'Payable', 'Payroll', 'Analytics', 'in', 'POWER', 'BI', 'Entertainment', 'Analytics', 'Advantages', 'in', 'Broadcasting', 'Industry', 'What', 'We', 'Think', 'Lessons', 'from', 'the', 'past', 'Some', 'key', 'learnings', 'relevant', 'to', 'the', 'coronavirus', 'EDITOR', 'PICKS', 'Design', 'Develop', 'BERT', 'Question', 'Answering', 'model', 'explanations', 'with', 'visualization', 'September', '16', '2022', 'Design', 'and', 'develop', 'solution', 'to', 'anomaly', 'detection', 'classification', 'problems', 'September', '16', '2022', 'An', 'ETL', 'Solution', 'for', 'Currency', 'Data', 'to', 'Google', 'Big', 'Query', 'September', '16', '2022', 'POPULAR', 'POSTS', 'AI', 'in', 'healthcare', 'to', 'Improve', 'Patient', 'Outcomes', 'June', '26', '2021', 'How', 'is', 'Login', 'Logout', 'Time', 'Tracking', 'for', 'Employees', 'in', 'Office', 'done', 'September', '28', '2021', 'Should', 'celebrities', 'be', 'allowed', 'to', 'join', 'politics', 'April', '16', '2020', 'POPULAR', 'CATEGORY', 'What', 'We', 'Think', '159', 'Our', 'Success', 'Stories', '122', 'Blackcoffer', '112', 'Healthcare', '50', 'Artificial', 'Intelligence', '50', 'IT', '46', 'Big', 'Data', '44', 'Lifestyle', 'eCommerce', 'Online', 'Market', 'Place', '37', 'IT', 'Services', '34', 'ABOUT', 'US', 'We', 'provide', 'intelligence', 'accelerate', 'innovation', 'and', 'implement', 'technology', 'with', 'extraordinary', 'breadth', 'and', 'depth', 'global', 'insights', 'into', 'the', 'big', 'data', 'data-driven', 'dashboards', 'applications', 'development', 'and', 'information', 'management', 'for', 'organizations', 'through', 'combining', 'unique', 'specialist', 'services', 'and', 'high-lvel', 'human', 'expertise', 'Contact', 'us', 'hello', 'blackcoffer.com', 'FOLLOW', 'US', 'Home', 'About', 'Services', 'Products', 'Contact', 'All', 'Right', 'Reserved', 'Blackcoffer', 'OPC', 'Pvt', 'Ltd']
def syllable_count(word):
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
            if word.endswith("e"):
                count -= 1
    if count == 0:
        count += 1
    return count
stop_words = set(stopwords.words('english'))
df = pd.read_csv("Output Data Structure.csv")
e=0
for i in df['URL']:
    e=e+1
    file_content = open("link"+str(e)+"s.txt", encoding="utf-8").read()
    tokens = nltk.word_tokenize(file_content)
    tokens_nopunch = list(filter(lambda token: token not in removepunch, tokens))
#removing stop words
    file = open("link"+str(e)+"s.txt", encoding="utf-8")
    cleaned_tokens = list(filter(lambda words: words not in stop_words, tokens_nopunch))
#removing punctuations
    tokens_noallpunch = list(filter(lambda token: token not in string.punctuation, cleaned_tokens))
#calculating positive and negative score
    filep = open("positive-words.txt", 'r')
    pos_words = filep.read().split()
    c = 0
    for j in tokens_noallpunch:
        if j in pos_words:
            c = c+1
    positive_score = c
    possc_list.append(positive_score)
    positive_score = c
    print(str(e)+":", positive_score)
    filen = open('negative-words.txt', 'r')
    neg_words = filen.read().split()
    d = 0
    for k in tokens_noallpunch:
        if k in neg_words:
            d = d+1
    negative_score = d
    negsc_list.append(negative_score)
    Polarity_Score = (positive_score - negative_score)/ ((positive_score + negative_score) + 0.000001)
    polsc_list.append(Polarity_Score)
    Subjectivity_Score = (positive_score + negative_score)/ ((len(tokens_noallpunch)) + 0.000001)
    subsc_list.append(Subjectivity_Score)
#calculated num of words
    for r in tokens_noallpunch:
        appendFile = open("cleaned"+str(e)+"text.txt",'a',encoding="utf-8")
        appendFile.write(" "+r)
        appendFile.close()	
    file = open("cleaned"+str(e)+"text.txt")
    data = file.read()
    words = data.split()
    w=len(words)
    wc_list.append(w)
#calculating num of sentences
    for p in cleaned_tokens:
        appendFile1 = open("filtered"+str(e)+"text.txt",'a',encoding="utf-8")
        appendFile1.write(" "+p)
        appendFile1.close()
    file_sen = open("filtered"+str(e)+"text.txt", 'r')
    lines = list(file_sen)
    file_contents = file_sen.read()
    file_sen.close()
    full_stops = 0
    for stop in lines:
       full_stops = full_stops + len(stop.split('.'))
    #calculating sum of characters in each word
    avg = sum(len(word) for word in words)
    avgwl = avg/len(words)
    avgwl_list.append(avgwl)
    AvgNumofWps = (len(words)/full_stops)
    avnow_list.append(AvgNumofWps)
    avgsl = len(words)/full_stops
    avsl_list.append(avgsl)
    #counting syllables
    cw = 0
    syllsum = 0
    for i in tokens_noallpunch:
       syll = syllable_count(i)
       syllsum = syllsum + syll
       if syll > 2:
         cw = cw + 1
    compwc_list.append(cw)
    a = syllsum
    avgsyl = a/len(words)
    avgsyl+=1
    sypw_list.append(avgsyl)
    Pocw = cw / len(words)
    perc_cw_list.append(str(Pocw))
    FogIndex = 0.4*(avgsl+Pocw)
    fogind_list.append(str(FogIndex))
#finding personal pronouns
    pronoun = ['I','we','my','ours','us']
    prepronoun = list(filter(lambda token: token in pronoun, tokens_noallpunch))
    prepron_list.append(len(prepronoun))
df["POSITIVE SCORE"] = possc_list
df["NEGATIVE SCORE"] = negsc_list
df["POLARITY SCORE"] = polsc_list
df['SUBJECTIVITY SCORE'] = subsc_list
df['WORD COUNT'] = wc_list
df['AVG WORD LENGTH'] = avgwl_list
df['AVG NUMBER OF WORDS PER SENTENCE'] = avnow_list
df['AVG SENTENCE LENGTH'] = avsl_list
df['COMPLEX WORD COUNT'] = compwc_list
df['SYLLABLE PER WORD'] = sypw_list
df['PERCENTAGE OF COMPLEX WORDS'] = perc_cw_list
df['FOG INDEX'] = fogind_list
df['PERSONAL PRONOUNS'] = prepron_list
df.to_csv("Output Data Structure.csv", index=False)
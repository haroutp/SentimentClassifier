punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(wrd):
    new_wrd = ""
    idx = 0
    while idx < len(wrd):
        if wrd[idx] not in punctuation_chars:
            new_wrd = new_wrd + wrd[idx]
        idx = idx + 1
    return new_wrd


def get_pos(sentences):
    count = 0
    for wrd in sentences.lower().split():
        word = strip_punctuation(wrd)
        if word in positive_words:
            count = count + 1
    return count


def get_neg(sentences):
    count = 0
    for wrd in sentences.lower().split():
        word = strip_punctuation(wrd)
        if word in negative_words:
            count = count + 1
    return count


# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


tweets_file = open('project_twitter_data.csv', 'r')
tweets = tweets_file.readlines()
#print(tweets)
outfile = open('resulting_data.csv', 'w')
#output the header row
outfile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n')
#print(tweets)
for tweet in tweets[1:]:
    data = tweet.strip().split(',')
    retweets = data[1]
    replies = data[2]
    positive_score = get_pos(data[0])
    negative_score = get_neg(data[0])
    net_score = positive_score - negative_score
    outfile.write('{},{},{},{},{}\n'.format(retweets, replies, positive_score, negative_score, net_score))
tweets_file.close()
outfile.close()

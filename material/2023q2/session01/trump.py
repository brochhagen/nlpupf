df_trump = pd.read_csv('https://raw.githubusercontent.com/ecdedios/into-heart-of-darkness/master/trump_20200530_clean.csv')
df_trump = df_trump.head(1000) #just the first 1000 tweets for ease of processing 

tweets = ' '.join(list(df_trump['tweet']))

doc = nlp(tweets)
# all tokens that arent stop words or punctuations
words = [token.text
         for token in doc
         if not token.is_stop and not token.is_punct]
word_freq = Counter(words)

trump_freq_df = pd.DataFrame.from_records(list(dict(word_freq).items()), columns=['word','frequency'])
trump_freq_df = trump_freq_df.sort_values(by=['frequency'], ascending=False)

print(trump_freq_df)
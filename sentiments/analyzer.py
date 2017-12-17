import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""

        #Initialize the positive list
        self.positives = list()
        #Open the file and go through each line, removing line breaks and skipping comments
        with open(positives) as lines:
            for line in lines:
                if line.startswith(';') == 0:
                    self.positives.append(line.strip("\n"))

        #Repeat the above for the negatives file
        self.negatives = list()
        with open(negatives) as lines:
            for line in lines:
                if line.startswith(';') == 0:
                    self.negatives.append(line.strip("\n"))


    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)
        finalCount = 0
        for word in tokens:
            if word.lower() in self.positives:
                finalCount += 1
            elif word.lower() in self.negatives:
                finalCount -= 1

        return finalCount

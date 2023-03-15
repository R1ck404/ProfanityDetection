class BadWordDetector:
    def __init__(self, filename):
        self.bad_words = []
        self.read_bad_words(filename)

    def read_bad_words(self, filename):
        with open(filename, 'r') as f:
            self.bad_words = [word.strip() for word in f.readlines()]

    def detect(self, text):
        words = text.lower().split()
        detected_bad_words = []
        for word in words:
            closest_match = self.get_closest_match(word, self.bad_words)
            if closest_match:
                similarity = self.get_similarity(word, closest_match)
                detected_bad_words.append((word, closest_match, similarity))
        return detected_bad_words

    def get_closest_match(self, word, candidates, threshold=0.5):
        closest_match = None
        max_similarity = threshold
        for candidate in candidates:
            similarity = self.get_similarity(word, candidate)
            if similarity > max_similarity:
                closest_match = candidate
                max_similarity = similarity
        return closest_match

    def get_similarity(self, word1, word2):
        if word1 == word2:
            return 1.0
        elif len(word1) == 0 or len(word2) == 0:
            return 0.0
        else:
            pairs1 = self.get_letter_pairs(word1)
            pairs2 = self.get_letter_pairs(word2)
            intersection = 0
            union = len(pairs1) + len(pairs2)
            for pair1 in pairs1:
                for pair2 in pairs2:
                    if pair1 == pair2:
                        intersection += 1
                        pairs2.remove(pair2)
                        break
            return 2.0 * intersection / union

    def get_letter_pairs(self, word):
        pairs = []
        for i in range(len(word)-1):
            pairs.append(word[i:i+2])
        return pairs
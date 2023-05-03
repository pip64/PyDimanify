import random

class марков:
    def __init__(self, corpus, размер_состояния=2):
        self.state_size = размер_состояния
        self.lookup_dict = self._generate_lookup_dict(corpus)

    def _generate_lookup_dict(self, corpus):
        lookup_dict = {}
        corpus = corpus.split()

        for i in range(len(corpus) - self.state_size):
            state = ' '.join(corpus[i:i+self.state_size])
            next_word = corpus[i+self.state_size]
            if state not in lookup_dict:
                lookup_dict[state] = {}
            if next_word not in lookup_dict[state]:
                lookup_dict[state][next_word] = 0
            lookup_dict[state][next_word] += 1

        return lookup_dict

    def _get_next_word(self, state):
        if state not in self.lookup_dict:
            return None
        next_words = self.lookup_dict[state]
        total = sum(next_words.values())
        rand = random.randint(1, total)
        for next_word, count in next_words.items():
            rand -= count
            if rand <= 0:
                return next_word

    def создать(self, слов=20):
        words = list(self.lookup_dict.keys())
        state = random.choice(words)

        sentence = state.capitalize()
        for i in range(слов - self.state_size):
            next_word = self._get_next_word(state)
            if next_word is None:
                break
            sentence += ' ' + next_word
            words = sentence.split()
            state = ' '.join(words[-self.state_size:])

        sentence += ''

        return sentence

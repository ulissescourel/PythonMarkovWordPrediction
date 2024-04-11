import random
import string

def create_markov_model():
  # From all sentences, create a table (word --> next word)
  ngram_freq = {}
  a, b = [], []
  for sentence in sentences:
    for i in range(len(sentence)-1):
      a.append(sentence[i])
      b.append(sentence[i+1])
  for i, word in enumerate(a):
    if word not in ngram_freq:
      ngram_freq[word] = {}
    for next_word in b[i:]:
      ngram_freq[word][next_word] = ngram_freq[word].get(next_word, 0) + 1
  return ngram_freq

sentence = ["Hello,", "how", "are", "you", "today", "?"]
print_sentence = "".join(sentence)
print("Sent: ", print_sentence)
memory = {}
rand = "".join(random.sample(set(string.ascii_lowercase), 1))
x = rand
while x not in [".", "?", "!"]:
  if x in ngram_freq:
    memory.setdefault(x, 0) += 1
    x = random.choice(ngram_freq[x].keys())
  else:
    break
print("Next word is: ", x)
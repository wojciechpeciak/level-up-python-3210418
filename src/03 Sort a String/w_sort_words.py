
def sort_words(phrase):
  word_list = phrase.split(' ')
  srtd_word_list = sorted(word_list, key=str.lower)
  return ' '.join(srtd_word_list)

print(sort_words('banana ORANGE apple'))
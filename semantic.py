import spacy
nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("mouse")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

'''
1. What I think is interesting about the similarities between cat, monkey and banana is that
   monkey and banana have a higher similarity score than cat and banana, so the model recognises
   that cats are less likely to be associated with bananas than monkeys. Also, 'mouse' is more similar
   to cat than monkey according to the model, so the model puts together that mice are more likely to
   be prey for cats rather than monkeys.
   
2. In comparison to the 'en_core_web_sm' model, the 'en_core_web_md' model seems to generate higher
   semantic similarity scores overall.
'''

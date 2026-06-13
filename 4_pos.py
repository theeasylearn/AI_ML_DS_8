import nltk

from nltk.tokenize import word_tokenize
text = """The quick brown fox jumps over the lazy dog, and it runs very quickly through the forest. Wow! John and Mary watch the animal from a wooden bridge while the birds sing sweetly above them. Because the weather is pleasant, they decide to stay longer. The fox is chasing a rabbit, but the rabbit is not afraid. “I will escape,” said the rabbit. The rabbit said that it would escape. Are the animals safe? Please close the gate. The scene is peaceful and beautiful. A cat is smaller than a tiger, while a lion is larger. Honest is a synonym of truthful, and honest is an antonym of dishonest. The fox catches the rabbit. The rabbit is caught by the fox. If the sun sets, the animals will return to their homes. Everyone enjoys the wonderful evening."""

tokens = word_tokenize(text)
print(tokens)

pos_tags = nltk.pos_tag(tokens)
print(pos_tags)

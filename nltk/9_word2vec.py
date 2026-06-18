from gensim.models import Word2Vec

topics = [
    ["cricket", "bat", "ball", "wicket", "stump", "umpire", "run", "boundary", "six", "over"],
    ["football", "goal", "pitch", "referee", "kick", "pass", "card", "penalty", "offside", "foul"],
    ["hockey", "ice", "puck", "stick", "skate", "rink", "goalie", "net", "period", "penalty"],
    ["chess", "board", "king", "queen", "rook", "bishop", "knight", "pawn", "checkmate", "move"],
]

# Optimized configuration for tiny datasets
model = Word2Vec(
    sentences=topics,
    epochs=800,       # Sufficiently high for 4 sentences
    min_count=1,     # Don't ignore rare words
    vector_size=10,  # Lowered from 100! 10 dimensions is plenty for 40 unique words.
    window=10,       # Increased to 10 so the model sees the entire sentence context
    sg=1             # Skip-gram is superior for small datasets/rare words
)

# Fixed the print statement labels for precision
print("Similar words to 'wicket':", model.wv.most_similar('wicket', topn=4))
print("Similar words to 'queen':", model.wv.most_similar('queen', topn=4))
print("Similar words to 'hockey':", model.wv.most_similar('hockey', topn=4))
print("Similar words to 'referee':", model.wv.most_similar('referee', topn=4))
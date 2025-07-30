import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


data = {
    'title': [
        'The Matrix', 'John Wick', 'Avengers: Endgame', 'Iron Man', 
        'The Dark Knight', 'Inception', 'Interstellar', 'The Prestige'
    ],
    'description': [
        'A computer hacker learns about the true nature of reality and his role in the war against its controllers.',
        'An ex-hitman comes out of retirement to track down the gangsters that killed his dog.',
        'The Avengers assemble once more to reverse Thanos\' actions and restore balance.',
        'After being held captive, a billionaire builds a high-tech suit to escape and fight evil.',
        'Batman faces the Joker, a criminal mastermind who causes chaos in Gotham.',
        'A thief steals corporate secrets through dream-sharing technology.',
        'A team of explorers travel through a wormhole in space in an attempt to ensure humanity\'s survival.',
        'Two magicians engage in a battle to create the ultimate illusion while sacrificing everything.'
    ]
}


df = pd.DataFrame(data)


tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['description'])


cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)


indices = pd.Series(df.index, index=df['title'])


def recommend(title, cosine_sim=cosine_sim):
    if title not in indices:
        return ["Movie not found in the list."]
    
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:4] 
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices].tolist()


if __name__ == "__main__":
    print("Available Movies:")
    for movie in df['title']:
        print("-", movie)

    user_input = input("\nEnter a movie title from the list above: ")
    recommendations = recommend(user_input)

    print("\nRecommended Movies:")
    for movie in recommendations:
        print("-", movie)

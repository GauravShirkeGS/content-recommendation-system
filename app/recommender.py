from sklearn.metrics.pairwise import cosine_similarity


def get_genre_based_recommendations(movie_title, movie_df, top_n=5):
    genre_cols = [col for col in movie_df.columns if col.startswith('genre_')]

    movie_vector = movie_df[movie_df['title'] == movie_title][genre_cols]
    if movie_vector.empty:
        return []

    genre_matrix = movie_df[genre_cols]
    similarity_scores = cosine_similarity(movie_vector, genre_matrix)[0]

    movie_df['similarity'] = similarity_scores
    recommendations = movie_df.sort_values(by='similarity', ascending=False)

    return recommendations[['title', 'similarity']].iloc[1:top_n + 1]

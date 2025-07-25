from app.data_loader import load_movie_metadata
from app.recommender import get_genre_based_recommendations


def main():
    movies = load_movie_metadata()
    print("\n✅ Loaded movie metadata.")

    movie_title = input("Enter a movie title (e.g., Toy Story (1995)): ")
    recommendations = get_genre_based_recommendations(movie_title, movies)

    if len(recommendations) == 0:
        print("No recommendations found.")
    else:
        print("\nTop similar movies based on genre:")
        print(recommendations)


if __name__ == "__main__":
    main()

import pandas as pd


def load_movie_metadata(path='dataset/u.item'):
    columns = ['movie_id', 'title', 'release_date', 'video_release_date', 'imdb_url'] + \
              [f'genre_{i}' for i in range(19)]

    movies = pd.read_csv(
        path,
        sep='|',
        encoding='latin-1',
        header=None,
        names=columns,
        usecols=range(24)
    )

    return movies

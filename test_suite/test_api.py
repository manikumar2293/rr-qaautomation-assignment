import logging
import pytest
from datetime import datetime
from conftest import movies as movies_fixture

# ----------------------
# Helper functions
# ----------------------
def filter_by_year(movies, year):
    return [m for m in movies if m.get("release_date") and datetime.strptime(m["release_date"], "%Y-%m-%d").year == year]

def filter_by_rating(movies, min_rating=0, max_rating=10):
    return [m for m in movies if min_rating <= m.get("vote_average", 0) <= max_rating]

def filter_by_genre(movies, genre_id):
    return [m for m in movies if genre_id in m.get("genre_ids", [])]

def paginate(movies, page_size=20, page=1):
    start = (page - 1) * page_size
    end = start + page_size
    return movies[start:end]

# ----------------------
# Test Cases
# ----------------------
def test_movies_loaded(movies):
    logging.info("Checking movies.json loaded")
    assert len(movies) > 0

def test_movies_2023(movies):
    result = filter_by_year(movies, 2023)
    logging.info(f"Movies from 2023: {len(result)}")
    assert isinstance(result, list)

def test_low_rated_movies(movies):
    result = filter_by_rating(movies, 0, 5)
    logging.info(f"Low rated movies: {len(result)}")
    for m in result:
        assert 0 <= m["vote_average"] <= 5

def test_animation_movies(movies):
    genre_id = 16
    result = filter_by_genre(movies, genre_id)
    logging.info(f"Animation movies: {len(result)}")
    assert isinstance(result, list)

def test_pagination(movies):
    page_1 = paginate(movies, page_size=5, page=1)
    page_2 = paginate(movies, page_size=5, page=2)
    logging.info(f"Page 1 items: {len(page_1)}, Page 2 items: {len(page_2)}")
    assert len(page_1) == 5
    assert len(page_2) == 5
    # Ensure different content
    ids_1 = [m["id"] for m in page_1]
    ids_2 = [m["id"] for m in page_2]
    assert ids_1 != ids_2

def test_invalid_page(movies):
    invalid = paginate(movies, page_size=5, page=999)
    logging.info(f"Invalid page items: {len(invalid)}")
    assert invalid == []

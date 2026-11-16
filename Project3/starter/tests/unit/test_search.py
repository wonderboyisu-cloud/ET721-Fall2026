import pytest
from app import create_app
from app.models import Fruit, FruitMetrics, db

@pytest.fixture(scope='module')
def test_app():
    # Setup: create a Flask app instance
    app = create_app()
    # Push an application context
    ctx = app.app_context()
    ctx.push()

    # Setup the database
    with app.app_context():
        db.create_all()

    yield app  # this is where the testing happens

    # Teardown: remove the application context
    ctx.pop()

# Add tests for the search functionality
# Start by adding some fruits to the database

# Test 1: Search by name
# Test 2: Search by variety
# Test 3: Search by season
# Test 4: Search by min quantity
# Test 5: Search by max quantity 
# Test 6: Search does not return any results

def test_searchByName_withExistingFruitName_returnsFruitsWithName(test_app):
    """
    Test the search functionality by name in the Fruit model.
    Verifies that the search method returns the correct fruits when searching by name.
    """
    # Setup - add fruits to the database
    fruits = [
        Fruit(name="Apple", quantity=10, variety="Gala", season="Winter"),
        Fruit(name="Banana", quantity=20, variety="Cavendish", season="All"),
        Fruit(name="Apple", quantity=15, variety="Fuji", season="Winter"),
    ]
    with test_app.app_context():  # Make sure you're in the db context
        db.session.bulk_save_objects(fruits)
        db.session.commit()

        # Add your test here


@pytest.fixture
def seeded_db(test_app):
    """
    Resets the Fruit table before every test and loads a known set of fruits,
    so each test starts from the same data regardless of execution order.
    """
    with test_app.app_context():
        Fruit.query.delete()
        db.session.add_all([
            Fruit(name="Apple", quantity=10, variety="Gala", season="Winter"),
            Fruit(name="Banana", quantity=20, variety="Cavendish", season="All"),
            Fruit(name="Apple", quantity=15, variety="Fuji", season="Winter"),
            Fruit(name="Cherry", quantity=5, variety="Bing", season="Summer"),
        ])
        db.session.commit()

    yield test_app


# Test 1: Search by name
def test_searchByName_withExistingName_returnsMatchingFruits(seeded_db):
    """
    Test the search functionality by name in the Fruit model.
    Verifies that only fruits with the matching name are returned.
    """
    with seeded_db.app_context():
        results = Fruit.search(name="Apple")
        assert len(results) == 2
        assert all(f.name == "Apple" for f in results)
        assert {f.variety for f in results} == {"Gala", "Fuji"}


# Test 2: Search by variety
def test_searchByVariety_withExistingVariety_returnsMatchingFruits(seeded_db):
    """
    Test the search functionality by variety.
    Verifies that only fruits with the matching variety are returned.
    """
    with seeded_db.app_context():
        results = Fruit.search(variety="Cavendish")
        assert len(results) == 1
        assert results[0].name == "Banana"
        assert results[0].variety == "Cavendish"


# Test 3: Search by season
def test_searchBySeason_withExistingSeason_returnsFruitsInSeason(seeded_db):
    """
    Test the search functionality by season.
    Verifies that all fruits in the given season are returned.
    """
    with seeded_db.app_context():
        results = Fruit.search(season="Winter")
        assert len(results) == 2
        assert all(f.season == "Winter" for f in results)


# Test 4: Search by min quantity
def test_searchByMinQuantity_withMinimum_returnsFruitsAtOrAboveMinimum(seeded_db):
    """
    Test the search functionality by minimum quantity.
    Verifies that fruits with quantity >= min_quantity are returned (inclusive).
    """
    with seeded_db.app_context():
        results = Fruit.search(min_quantity=15)
        assert len(results) == 2
        assert all(f.quantity >= 15 for f in results)
        assert {f.quantity for f in results} == {15, 20}


# Test 5: Search by max quantity
def test_searchByMaxQuantity_withMaximum_returnsFruitsAtOrBelowMaximum(seeded_db):
    """
    Test the search functionality by maximum quantity.
    Verifies that fruits with quantity <= max_quantity are returned (inclusive).
    """
    with seeded_db.app_context():
        results = Fruit.search(max_quantity=10)
        assert len(results) == 2
        assert all(f.quantity <= 10 for f in results)
        assert {f.quantity for f in results} == {5, 10}


# Test 6: Search does not return any results
def test_search_withNoMatchingFruits_returnsEmptyList(seeded_db):
    """
    Test the search functionality when nothing matches.
    Verifies that an empty list is returned.
    """
    with seeded_db.app_context():
        assert Fruit.search(name="Dragonfruit") == []
        assert Fruit.search(name="Apple", min_quantity=100) == []
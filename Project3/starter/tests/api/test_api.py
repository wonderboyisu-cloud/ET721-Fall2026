import json
import pytest
from app import create_app
from app.models import db, Fruit

@pytest.fixture
def app():
    app = create_app({"TESTING": True, "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"})
    with app.app_context():
        db.create_all()
        # Put some initial data into the database
        fruits = [
            Fruit(name="Apple", quantity=10, variety="Gala", season="Winter"),
            Fruit(name="Banana", quantity=20, variety="Cavendish", season="All"),
        ]
        db.session.bulk_save_objects(fruits)
        db.session.commit()
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_getAllFruits_whenDatabaseHasFruits_returnsFruitsList(client):
    """
    Test fetching all fruits from the database
    Validates that the GET request to '/api/fruits' returns a 200 status code,
    the correct number of fruits, and specific data of the fruits
    """
    response = client.get('/api/fruits')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert len(data) == 2  # Adjust based on your initial data
    assert data[0]['name'] == 'Apple'


def test_addFruit_withValidData_returnsSuccessMessageAndFruitId(client):
    """
    Test adding a new fruit to the database
    Validates that the POST request to '/api/fruits' adds the fruit correctly,
    and returns a 201 status code along with a success message and the fruit's ID
    """
    new_fruit = {"name": "Orange", "quantity": 5, "variety": "Navel", "season": "Winter"}
    response = client.post('/api/fruits', json=new_fruit)
    data = json.loads(response.data)
    assert response.status_code == 201
    assert data['message'] == 'Fruit added successfully'
    assert 'id' in data


def test_home_returnsDocumentationMessage(client):
    """
    Test the home route
    Validates that GET '/' returns a 200 status code and a message pointing to the documentation
    """
    response = client.get('/')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert 'documentation' in data['message']


def test_addFruit_withValidData_fruitAppearsInInventory(client):
    """
    Test that a fruit added through POST is persisted
    Validates that a follow-up GET to '/api/fruits' includes the new fruit
    """
    new_fruit = {"name": "Orange", "quantity": 5, "variety": "Navel", "season": "Winter"}
    post_response = client.post('/api/fruits', json=new_fruit)
    new_id = json.loads(post_response.data)['id']

    data = json.loads(client.get('/api/fruits').data)
    assert len(data) == 3
    added = [f for f in data if f['id'] == new_id][0]
    assert added['name'] == 'Orange'
    assert added['quantity'] == 5


def test_updateFruit_withExistingId_updatesOnlyProvidedFields(client):
    """
    Test updating an existing fruit
    Validates that PUT returns 200, changes the provided field, and leaves the others untouched
    """
    response = client.put('/api/fruits/1', json={"quantity": 99})
    assert response.status_code == 200
    assert json.loads(response.data)['message'] == 'Fruit updated successfully'

    data = json.loads(client.get('/api/fruits').data)
    updated = [f for f in data if f['id'] == 1][0]
    assert updated['quantity'] == 99
    assert updated['name'] == 'Apple'
    assert updated['variety'] == 'Gala'
    assert updated['season'] == 'Winter'


def test_updateFruit_withNonExistentId_returns404(client):
    """
    Test updating a fruit that does not exist
    Validates that PUT returns a 404 status code and a not found message
    """
    response = client.put('/api/fruits/999', json={"quantity": 1})
    assert response.status_code == 404
    assert json.loads(response.data)['message'] == 'Fruit not found'


def test_deleteFruit_withExistingId_removesFruit(client):
    """
    Test deleting an existing fruit
    Validates that DELETE returns 200 and the fruit is no longer in the inventory
    """
    response = client.delete('/api/fruits/1')
    assert response.status_code == 200
    assert json.loads(response.data)['message'] == 'Fruit deleted successfully'

    data = json.loads(client.get('/api/fruits').data)
    assert len(data) == 1
    assert all(f['id'] != 1 for f in data)


def test_deleteFruit_withNonExistentId_returns404(client):
    """
    Test deleting a fruit that does not exist
    Validates that DELETE returns a 404 status code and a not found message
    """
    response = client.delete('/api/fruits/999')
    assert response.status_code == 404
    assert json.loads(response.data)['message'] == 'Fruit not found'


def test_searchFruits_withMatchingName_returnsMatchingFruits(client):
    """
    Test searching by name through the API
    Validates that GET '/api/fruits/search' returns only the fruits matching the name
    """
    response = client.get('/api/fruits/search?name=Apple')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]['name'] == 'Apple'


def test_searchFruits_withQuantityRange_returnsFruitsInRange(client):
    """
    Test searching by quantity range through the API
    Validates that min_quantity and max_quantity are applied together
    """
    response = client.get('/api/fruits/search?min_quantity=15&max_quantity=25')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]['name'] == 'Banana'


def test_searchFruits_withNoMatches_returnsNoResultsMessage(client):
    """
    Test searching with criteria that match nothing
    Validates that the API returns a 200 status code and the no results message
    """
    response = client.get('/api/fruits/search?name=Dragonfruit')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['message'] == 'No fruits found matching the search criteria'
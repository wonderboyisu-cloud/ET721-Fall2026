import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


# -------------------
# HOME TEST
# -------------------
def test_home(client):
    response = client.get('/')
    assert response.status_code == 200


# -------------------
# CREATE AN ITEM, POST METHOD 
# -------------------
def test_create_item(client):
    response = client.post('/items', json={'name': 'Book', 'price': 10})

    assert response.status_code == 201

    # test the template with id 1
    data = response.get_json()
    assert 'id' in data
    assert data['item']['name'] == 'Book'
    assert data['item']['price'] == 10


# -------------------
# READ SINGLE ITEM
# -------------------
def test_get_single_item(client):
    client.post('/items', json = {'name': 'Laptop'})
    response = client.get('/items/2')

    assert response.status_code == 200
    assert response.get_json()['name'] == 'Laptop'


# -------------------
# READ ALL ITEMS
# -------------------
def test_get_items(client):
    client.post('/items', json = {'name': 'Pen'})
    client.post('/items', json = {'name': 'Notebook'})

    response = client.get('/items')

    assert response.status_code == 200
    
    data = response.get_json()
    assert len(data) == 4


# -------------------
# UPDATE ITEM
# -------------------
def test_update_item(client):
    client.put('/items/3', json = {'name': 'Phone'})

    response = client.get('items')

    assert response.status_code == 200

    data = response.get_json()
    assert len(data) == 4
    
    assert data['3']['name'] == 'Phone'
    
    



















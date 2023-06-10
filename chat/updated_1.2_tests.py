import json
import pytest
from app import app

Idi kuda try chey ...........


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_update_task(client):
    # Test case for updating a task that does not exist
    response = client.put('/update/task/5', json={"title": "Updated Task", "priority": "Urgent", "status": "In progress", "assignto": "Mark"})
    assert response.status_code == 404
    data = json.loads(response.data)
    assert data == {'message': 'The task ID you entered does not exist'}

    # Test case for updating a task that exists
    response = client.put('/update/task/1', json={"title": "Updated Task", "priority": "Urgent", "status": "In progress", "assignto": "Mark"})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data == {'message': 'Task updated successfully'}


def test_filter_task(client):
    # Test case for filtering tasks with a status that does not exist
    response = client.get('/filter/task/Done')
    assert response.status_code == 404
    data = json.loads(response.data)
    assert data == {'message': 'The status you entered does not exist'}

    # Test case for filtering tasks with an existing status
    response = client.get('/filter/task/Backlog')
    assert response.status_code == 200
    expected_data = [
        {"assignto": "Mark", "id": 1, "priority": "Urgent", "status": "Backlog", "title": "Fix Bug"}
    ]
    data = json.loads(response.data)
    assert data == expected_data

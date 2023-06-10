import os
import pytest
import json
from app import app, db
import unittest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
'''
class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
'''
class TestAPI:
    client = app.test_client()

    @pytest.fixture(autouse=True, scope='session')
    def setup(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        db.create_all()
        yield db
        os.remove('test.db')

    def test_home(self):
        response = self.client.get('/')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data == {'message': 'Welcome to Kanban Board Flask application hosted on Docker'}

    def test_add_task_without_title(self):
        payload = {"title": "", "priority": "Urgent", "assignto": "Mark"}
        response = self.client.post('/add/task', json=payload)
        assert response.status_code == 400
        data = json.loads(response.data)
        assert data == {'message': 'Please fill in all the required fields'}

    def test_add_task_without_priority(self):
        payload = {"title": "Fix Bug", "priority": "", "assignto": "Mark"}
        response = self.client.post('/add/task', json=payload)
        assert response.status_code == 400
        data = json.loads(response.data)
        assert data == {'message': 'Please fill in all the required fields'}

    def test_add_task_without_assignto(self):
        payload = {"title": "Fix Bug", "priority": "Urgent", "assignto": ""}
        response = self.client.post('/add/task', json=payload)
        assert response.status_code == 400
        data = json.loads(response.data)
        assert data == {'message': 'Please fill in all the required fields'}

    def test_add_task(self):
        payloads = [
            {"title": "Fix Bug", "priority": "Urgent", "assignto": "Mark"},
            {"title": "Resolve Tickets", "priority": "Low", "assignto": "John"},
            {"title": "Devops Session", "priority": "Medium", "assignto": "David"}
        ]
        expected_message = {'message': 'Task added successfully'}
        for payload in payloads:
            response = self.client.post('/add/task', json=payload)
            assert response.status_code == 201
            data = json.loads(response.data)
            assert data == expected_message

    def test_list_task(self):
        response = self.client.get('/list/task')
        assert response.status_code == 200
        expected_data = [
            {"assignto": "Mark", "id": 1, "priority": "Urgent", "status": "Backlog", "title": "Fix Bug"},
            {"assignto": "John", "id": 2, "priority": "Low", "status": "Backlog", "title": "Resolve Tickets"},
            {"assignto": "David", "id": 3, "priority": "Medium", "status": "Backlog", "title": "Devops Session"}
        ]
        data = json.loads(response.data)
        assert data == expected_data

    def test_update_task_without_title(self):
        payload = {"title": "", "priority": "Urgent", "status": "In progress", "assignto": "Mark"}
        response = self.client.put('/update/task/1', json=payload)
        assert response.status_code == 400
        data = json.loads(response.data)
        assert data == {'message': 'Please fill in all the required fields'}

    def test_update_task_without_priority(self):
        payload = {"title": "Fix Bug", "priority": "", "status": "In progress", "assignto": "Mark"}
        response = self.client.put('/update/task/1', json=payload)
        assert response.status_code == 400
        data = json.loads(response.data)
        assert data == {'message': 'Please fill in all the required fields'}

    def test_update_task_without_status(self):
        payload = {"title": "Fix Bug", "priority": "Urgent", "status": "", "assignto": "Mark"}
        response = self.client.put('/update/task/1', json=payload)
        assert response.status_code == 400
        data = json.loads(response.data)
        assert data == {'message': 'Please fill in all the required fields'}

    def test_update_task_without_assignto(self):
        payload = {"title": "Fix Bug", "priority": "Urgent", "status": "In progress", "assignto": ""}
        response = self.client.put('/update/task/1', json=payload)
        assert response.status_code == 400
        data = json.loads(response.data)
        assert data == {'message': 'Please fill in all the required fields'}

    
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


    def test_delete_task(self):
        response = self.client.delete('/delete/task/5')
        assert response.status_code == 404
        data = json.loads(response.data)
        assert data == {'message': 'The task ID you entered does not exist'}

        response = self.client.delete('/delete/task/1')
        assert response.status_code == 204



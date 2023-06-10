import os
import pytest
import json
from app import app, db


class Test_API:
    client = app.test_client()

    @pytest.fixture(autouse=True, scope='session')
    def setup(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  
        db.create_all()
        yield db
        os.remove('test.db')


    def test_home(self):
        '''
        In this method, you should send the request to "/" URL  
        assert the response status code it should contain "200"
        assert the JSON response it should contain {"message": "Welcome to Kanban Board Flask application hosted on Docker"}
        '''
        assert None


    def test_add_task_without_title(self):
        '''
        In this method, you should send the request to "/add/task" URL with the following data payload 
        {"title": "", "priority": "Urgent", "assignto": "Mark"}
        assert the response status code it should contain "400"
        assert the JSON response it should contain {"message": "Please fill in all the required fields"}
        '''
        assert None

        
    def test_add_task_without_priority(self):
        '''
        In this method, you should send the request to "/add/task" URL with the following data payload 
        {"title": "Fix Bug", "priority": "", "assignto": "Mark"}
        assert the response status code it should contain "400"
        assert the JSON response it should contain {"message": "Please fill in all the required fields"}
        '''
        assert None
 

    def test_add_task_without_assignto(self):
        '''
        In this method, you should send the request to "/add/task" URL with the following data payload 
        {"title": "Fix Bug", "priority": "Urgent", "assignto": ""}
        assert the response status code it should contain "400"
        assert the JSON response it should contain {"message": "Please fill in all the required fields"}
        '''
        assert None


    def test_add_task(self):
        '''
        In this method, you should send the request to "/add/task" URL with the following data payloads 
        {"title": "Fix Bug", "priority": "Urgent", "assignto": "Mark"}
        {"title": "Resolve Tickets", "priority": "Low", "assignto": "John"}
        {"title": "Devops Session", "priority": "Medium", "assignto": "David"}
        assert the response status code it should contain "201"
        assert the JSON response it should contain {"message": "Task added successfully"}
        '''
        assert None
    

    def test_list_task(self):
        '''
        In this method, you should send the request to "/list/task" URL
        assert the response status code it should contain "200"
        assert the JSON response it should contain 
        [{"assignto": "Mark", "id": 1, "priority": "Urgent", "status": "Backlog", "title": "Fix Bug"},
        {"assignto": "John", "id": 2, "priority": "Low", "status": "Backlog", "title": "Resolve Tickets"},
        {"assignto": "David", "id": 3, "priority": "Medium", "status": "Backlog", "title": "Devops Session"}]
        '''
        assert None

    
    def test_update_task_without_title(self):
        '''
        In this method, you should send the request to "/update/task/1" URL with the following data payload 
        {"title": "", "priority": "Urgent", "status": "In progress", "assignto": "Mark"}
        assert the response status code it should contain "400"
        assert the JSON response it should contain {"message": "Please fill in all the required fields"}
        '''
        assert None
    

    def test_update_task_without_priority(self):
        '''
        In this method, you should send the request to "/update/task/1" URL with the following data payload 
        {"title": "Fix Bug", "priority": "", "status": "In progress", "assignto": "Mark"}
        assert the response status code it should contain "400"
        assert the JSON response it should contain {"message": "Please fill in all the required fields"}
        '''
        assert None
    

    def test_update_task_without_status(self):
        '''
        In this method, you should send the request to "/update/task/1" URL with the following data payload 
        {"title": "Fix Bug", "priority": "Urgent", "status": "", "assignto": "Mark"}
        assert the response status code it should contain "400"
        assert the JSON response it should contain {"message": "Please fill in all the required fields"}
        '''
        assert None
      

    def test_update_task_without_assignto(self):
        '''
        In this method, you should send the request to "/update/task/1" URL with the following data payload 
        {"title": "Fix Bug", "priority": "Urgent", "status": "In progress", "assignto": ""}
        assert the response status code it should contain "400"
        assert the JSON response it should contain {"message": "Please fill in all the required fields"}
        '''
        assert None


    def test_update_task(self):
        '''
        In this method, you should send the request to "/update/task/5" URL with the following data payload 
        {"title": "Fix Bug", "priority": "Urgent", "status": "In progress", "assignto": ""}
        assert the response status code it should contain "404"
        assert the JSON response it should contain {"message": "The task ID you entered does not exist"}

        Send the request to "/update/task/1" URL with the following data payload
        {"title": "Fix Bug", "priority": "Urgent", "status": "In progress", "assignto": "Mark"}
        assert the response status code it should contain "200"
        assert the JSON response it should contain {"message": "Task updated successfully"}
        '''
        assert None


    def test_filter_task(self):
        '''
        In this method, you should send the request to "/filter/task/Done" URL
        assert the response status code it should contain "404"
        assert the JSON response it should contain {"message": "The status you entered does not exist"}
         
        Send the request to "/filter/task/Backlog" URL
        assert the response status code it should contain "200"
        assert the JSON response it should contain 
        [{"assignto": "John", "id": 2, "priority": "Low", "status": "Backlog", "title": "Resolve Tickets"},
        {"assignto": "David", "id": 3, "priority": "Medium", "status": "Backlog", "title": "Devops Session"}]
        '''
        assert None


    def test_delete_task(self):
        '''
        In this method, you should send the request to "/delete/task/5" URL  
        assert the response status code it should contain "404"
        assert the JSON response it should contain {"message": "The task ID you entered does not exist"}
         
        Send the request to "/delete/task/1" URL
        assert the response status code it should contain "204"
        '''
        assert None
    


    
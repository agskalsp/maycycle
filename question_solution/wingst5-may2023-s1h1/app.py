from flask import Flask, jsonify, request
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
import os
import warnings


with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=UserWarning)
    from flask_marshmallow import Marshmallow

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "Keepitsecret"

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app=app, db=db)

class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    priority = db.Column(db.String, nullable=False)
    status = db.Column(db.String, default="Backlog")
    assignto = db.Column(db.String, nullable=False)


class TaskSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'priority', 'status', 'assignto')

Task_schema = TaskSchema()
Task_schema = TaskSchema(many=True)

db.create_all()

# This endpoint is used to display the welcome message
@app.route('/')
def home():
    return jsonify(message="Welcome to Kanban Board Flask application hosted on Docker"), 200

  
# This endpoint is used to add a task
@app.route('/add/task', methods=['POST'])
def addtask():
    data = request.get_json()
    title = data['title']
    priority = data['priority']
    assignto = data['assignto']

    if len(title) == 0 or len(priority) == 0 or len(assignto) == 0:
        return jsonify(message="Please fill in all the required fields"), 400
    else:
        newtask = Task(title=title, priority=priority, assignto=assignto)
        db.session.add(newtask)
        db.session.commit()
        return jsonify(message="Task added successfully"), 201


# This endpoint is used to list all the tasks
@app.route('/list/task', methods=['GET'])
def listtask():
    temptask = Task.query.all()
    result = Task_schema.dump(temptask)
    return jsonify(result), 200


# This endpoint is used to update a task
@app.route('/update/task/<int:id>', methods=['PUT'])
def updatetask(id: int):
    data = request.get_json()
    title = data['title']
    priority = data['priority']
    status = data['status']
    assignto = data['assignto']

    temptask = Task.query.filter_by(id=id).first()
    
    if not temptask: 
        return jsonify(message="The task ID you entered does not exist"), 404

    elif len(title) == 0 or len(priority) == 0 or len(status) == 0 or len(assignto) == 0:
        return jsonify(message="Please fill in all the required fields"), 400

    else:
        temptask.title = title
        temptask.priority = priority
        temptask.status = status
        temptask.assignto = assignto
        db.session.commit()
        return jsonify(message="Task updated successfully"), 200
        

# This endpoint is used to filter a task based on status ('Backlog', 'Todo', 'Inprogress', 'Done')
@app.route('/filter/task/<string:status>', methods=['GET'])
def filtertask(status: str):
    temptask = Task.query.filter_by(status=status)
    result = Task_schema.dump(temptask)

    if result:
        return jsonify(result), 200
    else:
        return jsonify(message="The status you entered does not exist"), 404


# This endpoint is used to delete a task
@app.route('/delete/task/<int:id>', methods=['DELETE'])
def deletetask(id: int):
    temptask = Task.query.filter_by(id=id).first()

    if temptask:
        db.session.delete(temptask)
        db.session.commit()
        return '', 204
    else:
        return jsonify(message="The task ID you entered does not exist"), 404

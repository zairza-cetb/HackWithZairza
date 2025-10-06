import unittest
from unittest.mock import patch
import os
import json
from datetime import datetime
import main as todo

# Use a separate file for testing
TEST_FILE = os.path.expanduser("~/.todo_cli_test.json")
todo.DATA_FILE = TEST_FILE

class TestTodoCLI(unittest.TestCase):

    def setUp(self):
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)
        self.tasks = []

    def tearDown(self):
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)

    # Utility Functions Tests
    def test_get_next_id_empty(self):
        self.assertEqual(todo.get_next_id([]), 1)

    def test_get_next_id_nonempty(self):
        self.tasks = [{"id": 1}, {"id": 3}]
        self.assertEqual(todo.get_next_id(self.tasks), 4)

    def test_save_and_load_tasks(self):
        task = {"id": 1, "description": "Test", "priority": "medium", "due_date": None, 
                "created_at": datetime.now().isoformat(), "completed": False, "completed_at": None}
        todo.save_tasks([task])
        loaded = todo.load_tasks()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0]["description"], "Test")

    # Test add_task
    @patch("builtins.input", side_effect=["My Task", "", "high", "y"])
    def test_add_task(self, mock_inputs):
        todo.add_task(self.tasks)
        self.assertEqual(len(self.tasks), 1)
        self.assertEqual(self.tasks[0]["description"], "My Task")
        self.assertEqual(self.tasks[0]["priority"], "high")
        self.assertFalse(self.tasks[0]["completed"])

    @patch("builtins.input", side_effect=["", "", "", "n"])
    def test_add_task_empty_description(self, mock_inputs):
        todo.add_task(self.tasks)
        self.assertEqual(len(self.tasks), 0)

    # Test complete_task
    @patch("builtins.input", side_effect=["1"])
    def test_complete_task(self, mock_inputs):
        task = {"id":1, "description":"Test", "priority":"medium", "due_date":None,
                "created_at": datetime.now().isoformat(), "completed":False, "completed_at":None}
        self.tasks.append(task)
        todo.complete_task(self.tasks)
        self.assertTrue(self.tasks[0]["completed"])
        self.assertIsNotNone(self.tasks[0]["completed_at"])

    # Test delete_task
    @patch("builtins.input", side_effect=["1", "y"])
    def test_delete_task(self, mock_inputs):
        task = {"id":1, "description":"Test", "priority":"medium", "due_date":None,
                "created_at": datetime.now().isoformat(), "completed":False, "completed_at":None}
        self.tasks.append(task)
        todo.delete_task(self.tasks)
        loaded = todo.load_tasks()
        self.assertEqual(len(loaded), 0)

    # Test edit_task
    @patch("builtins.input", side_effect=["1", "Edited Task", "2025-10-10", "high"])
    def test_edit_task(self, mock_inputs):
        task = {"id":1, "description":"Original", "priority":"low", "due_date":None,
                "created_at": datetime.now().isoformat(), "completed":False, "completed_at":None}
        self.tasks.append(task)
        todo.edit_task(self.tasks)
        self.assertEqual(self.tasks[0]["description"], "Edited Task")
        self.assertEqual(self.tasks[0]["priority"], "high")
        self.assertEqual(self.tasks[0]["due_date"], "2025-10-10")

    # Test filter_tasks by priority
    @patch("builtins.input", side_effect=["1", "high"])
    def test_filter_by_priority(self, mock_inputs):
        tasks = [
            {"id":1,"description":"Task1","priority":"high","due_date":None,"created_at":datetime.now().isoformat(),"completed":False,"completed_at":None},
            {"id":2,"description":"Task2","priority":"low","due_date":None,"created_at":datetime.now().isoformat(),"completed":False,"completed_at":None}
        ]
        todo.filter_tasks(tasks)

    # Test filter_tasks by due date
    @patch("builtins.input", side_effect=["2", "2025-10-10"])
    def test_filter_by_due_date(self, mock_inputs):
        tasks = [
            {"id":1,"description":"Task1","priority":"high","due_date":"2025-10-05","created_at":datetime.now().isoformat(),"completed":False,"completed_at":None},
            {"id":2,"description":"Task2","priority":"low","due_date":"2025-11-01","created_at":datetime.now().isoformat(),"completed":False,"completed_at":None}
        ]
        todo.filter_tasks(tasks)

if __name__ == "__main__":
    unittest.main()

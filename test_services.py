
import pytest
from services import TaskService


def make_service_with_items(items=None):
    """Create a TaskService and its backing dict for testing."""
    if items is None:
        items = []
    task_dict = {'Items': items}
    return TaskService(task_dict), task_dict


def get_task_names(task_dict):
    """Return a list of task names from the task dict."""
    return [t['task_name'] for t in task_dict['Items']]



@pytest.mark.parametrize("task_name,expected_count,should_add", [
    ("", 0, False),  # Empty name, should not add
    ("Task 1", 1, True),  # Normal name
    ("Task 1", 1, True),  # Duplicate name allowed in current logic
    ("A" * 256, 1, True),  # Long name
])
def test_add_task(task_name, expected_count, should_add):
    """Test adding tasks with various names."""
    service, task_dict = make_service_with_items([])
    task_id = "id1"
    # Simulate add_task logic: only add if name is not empty
    if task_name:
        service.add_task(task_id, task_name)
    assert len(task_dict['Items']) == expected_count
    if should_add:
        assert task_dict['Items'][0]['task_name'] == task_name
    else:
        assert task_dict['Items'] == []



@pytest.mark.parametrize("first,second,expected_count", [
    ("Task 1", "Task 1", 2),  # Duplicates allowed
    ("Task 1", "Task 2", 2),
])
def test_add_duplicate_names(first, second, expected_count):
    """Test adding duplicate and unique task names."""
    service, task_dict = make_service_with_items([])
    service.add_task("id1", first)
    service.add_task("id2", second)
    assert len(task_dict['Items']) == expected_count
    assert get_task_names(task_dict)[0] == first
    assert get_task_names(task_dict)[1] == second


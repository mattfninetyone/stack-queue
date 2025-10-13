from main import Stack, Queue, MattStack, MattQueue, T
import pytest

@pytest.fixture
def stack() -> Stack:
    # create and return a new queue implementation
    return MattStack()

@pytest.fixture
def queue() -> Queue:
    # create and return a new queue implementation
    return MattQueue()
    
ITEM = 12

def test_stack_push(stack):
    # Arrange
    
    # Act
    stack.push(ITEM)

    # Assert
    assert not stack.is_empty()
    assert stack.peek() == ITEM


def test_stack_pop(stack):
    # Arrange

    # Act
    stack.push(ITEM)
    popped_item = stack.pop()

    # Assert
    assert popped_item is ITEM
    assert stack.is_empty()

def test_stack_peek(stack):
    # Arrange
    
    # Act
    stack.push(ITEM)
    top_item = stack.peek()

    # Assert
    assert top_item == ITEM
    assert not stack.is_empty()

def test_stack_is_empty(stack):
    # Arrange

    # Act

    # Assert
    assert stack.is_empty()

def test_queue_enqueue(queue):
    # Arrange

    # Act
    queue.enqueue(ITEM)
    # Assert
    assert not queue.is_empty()
    assert queue.peek() == ITEM

def test_queue_dequeue(queue):
    # Arrange

    # Act
    queue.enqueue(ITEM)
    dequeued_item = queue.dequeue()

    # Assert
    assert dequeued_item == ITEM
    assert queue.is_empty()

def test_queue_peek(queue):
    # Arrange

    # Act
    queue.enqueue(ITEM)
    front_item = queue.peek()

    # Assert
    assert front_item == ITEM
    assert not queue.is_empty()

def test_queue_is_empty(queue):
    # Arrange

    # Act

    # Assert
    assert queue.is_empty()

def test_stack_multi_push(stack):
    
    stack.push(ITEM)
    stack.push(ITEM)
    stack.push(ITEM)

    #assert 














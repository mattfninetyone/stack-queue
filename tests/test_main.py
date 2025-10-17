from main import Stack, Queue, MattQueueLink, MattStackArrAll, MattQueueLinkX2
import pytest
import math

data_type = object


# FIXTURES
@pytest.fixture
def stack() -> Stack:
    return MattStackArrAll(data_type)


@pytest.fixture
def queue() -> Queue:
    return MattQueueLink()


@pytest.fixture
def queue_v2() -> Queue:
    return MattQueueLinkX2()


# ----- STACK TESTS ----- #


# BASIC FUNCTIONALITY CASES
def test_stack_push(stack):
    # Arrange
    item = 12
    # Act
    stack.push(item)
    # Assert
    assert not stack.is_empty()
    assert stack.peek() == item


def test_stack_pop(stack):
    item = 12
    stack.push(item)
    popped_item = stack.pop()
    assert popped_item == item
    assert stack.is_empty()


def test_stack_peek(stack):
    item = 12
    stack.push(item)
    top_item = stack.peek()
    assert top_item == item
    assert not stack.is_empty()


def test_stack_is_empty(stack):
    assert stack.is_empty()


# HANDLING MULTIPLE VALS
def test_stack_multi_push(stack):
    for i in range(10):
        stack.push(i)
    for i in reversed(range(10)):
        assert stack.pop() == i


# BOUNDARY GROWTH CASE
def test_stack_grow(stack):
    val = 8
    for i in range(val + 1):
        stack.push(i)
    assert stack.peek() == val
    assert stack.pop() == val
    assert len(stack) == (2 ** (max(1, math.ceil(math.log2(val)))))


# VALUE ERROR ON EMPTY POP/PEEK CASE
def test_stack_value_error(stack):
    with pytest.raises(ValueError) as e1:
        stack.pop()
    with pytest.raises(ValueError) as e2:
        stack.peek()

    assert str(e1.value) == "Stack is empty"
    assert str(e2.value) == "Stack is empty"


# ONE TYPE PER STACK
def test_stack_one_type(stack):
    stack.push(1)
    with pytest.raises(TypeError) as e:
        stack.push("")
    assert str(e.value) == "item should be of type " + str(data_type)


# PEEK IDEMPOTENCE CASE
def test_peek_idempotent(stack):
    stack.push(1)
    assert stack.peek()
    assert stack.peek()


# ----- QUEUE TESTS ----- #

# PARAMETERISE CLASS OBJECTS
models = [MattQueueLink, MattQueueLinkX2]


# BASIC FUNCTIONALITY CASES
@pytest.mark.parametrize("QImp", models)
def test_queue_enqueue(QImp):
    queue = QImp()
    # Arrange
    item = 12
    # Act
    queue.enqueue(item)
    # Assert
    assert not queue.is_empty()
    assert queue.peek() == item


@pytest.mark.parametrize("QImp", models)
def test_queue_dequeue(QImp):
    queue = QImp()
    item = 12
    queue.enqueue(item)
    dequeued_item = queue.dequeue()
    assert dequeued_item == item
    assert queue.is_empty()


@pytest.mark.parametrize("QImp", models)
def test_queue_peek(QImp):
    queue = QImp()
    item = 12
    queue.enqueue(item)
    front_item = queue.peek()
    assert front_item == item
    assert not queue.is_empty()


@pytest.mark.parametrize("QImp", models)
def test_queue_is_empty(QImp):
    queue = QImp()
    assert queue.is_empty()


# HANDLING MULTIPLE VALS
@pytest.mark.parametrize("QImp", models)
def test_queue_multi_push(QImp):
    queue = QImp()
    for i in range(10):
        queue.enqueue(i)
    for i in range(10):
        assert queue.dequeue() == i


# VALUE ERROR ON EMPTY DEQUEUE/PEEK CASE
@pytest.mark.parametrize("QImp", models)
def test_queue_value_error(QImp):
    queue = QImp()
    with pytest.raises(ValueError) as e1:
        queue.dequeue()
    with pytest.raises(ValueError) as e2:
        queue.peek()

    assert str(e1.value) == "Empty"
    assert str(e2.value) == "Empty"


# ALL TYPE CASE
@pytest.mark.parametrize("QImp", models)
def test_queue_any_as_input(QImp):
    queue = QImp()
    for item in [0, False, "", None]:
        queue.enqueue(item)
        assert not queue.is_empty()
        assert queue.dequeue() is item


# ONE TYPE PER QUEUE
@pytest.mark.parametrize("QImp", models)
def test_queue_one_type(QImp):
    queue = QImp()
    queue.enqueue(1)
    with pytest.raises(TypeError) as e:
        queue.enqueue("")
    assert str(e.value) == "item should be of type " + str(queue._first_type)


# HEAD, TAIL, PREV CASES
@pytest.mark.parametrize("QImp", models)
def test_head_tail_empty(QImp):
    queue = QImp()
    queue.enqueue(1)
    assert queue.dequeue() == 1
    assert queue.head is None
    assert queue.tail is None


# DBL LINK LIST FORWARD, BACKWARD, HEAD NONE CASE
def test_double_link_next_prev(queue_v2):
    num = 100
    for i in range(num + 1):
        queue_v2.enqueue(i)
    assert queue_v2.head.value == 0
    assert queue_v2.head.next.value == 1
    assert queue_v2.head.next.next.value == 2
    assert queue_v2.tail.value == num
    assert queue_v2.tail.prev.value == num - 1
    assert queue_v2.tail.prev.prev.value == num - 2
    assert queue_v2.dequeue() == 0
    assert queue_v2.head.prev is None

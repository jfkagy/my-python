"""Stone hopping problem."""


class queue:
  """For didactical purposes; collections.deque is a faster implementation."""
  def __init__(self, items):
    self.items = items

  def dequeue(self):
    return self.items.pop()

  def enqueue(self, item):
    self.items = [item] + self.items

  def peek(self):
    return self.items[-1]

  @property
  def empty(self):
    return not self.items


def hopping(stones: list[str], moves: tuple[int]):
  """Solves the stone hopping problem in linear time.

  Args:
    stones: Sequence of 'x' (stones) and '_' (water). The first and last elements are
      assumed to be 'x'.
    moves: Eligible jump sizes.
  """

  # Start from the initial stone.
  # Try all moves. If landing on a stone, add to to_visit.
  # Iterate through positions in to_visit.
  # When the last stone is visited, return True.
  # Otherwise when to_visit is exhausted, return False.
  
  can = [None] * len(stones)
  can[0] = can[-1] = True

  to_visit = queue([0])

  while not to_visit.empty:
    visiting = to_visit.dequeue()
    if stones[visiting] == "_":
      # not a stone -> set to False
      can[visiting] = False
    else:
      # is a stone -> set to True
      can[visiting] = True
      for move in moves:
        if visiting + move == len(stones) - 1:
          return True
        # is outside the board
        if visiting + move < 0 or visiting + move >= len(stones):
          continue
        # already visited -> ignore
        if can[visiting + move] is not None:
          continue
        to_visit.enqueue(visiting + move)

  return False

# Test case 1.
# The last stone can be reached with the following hops: +3 -> -1 -> +3 -> +3
stones = ['x', '_', 'x', 'x', '_', 'x', '_', '_', 'x']
moves = (-1, 3)
assert hopping(stones, moves)

# Test case 2.
# The last stone cannot be reached.
stones = ['x', '_', 'x', 'x', '_', 'x', '_', '_', 'x']
moves = (-1, 2)
assert not hopping(stones, moves)

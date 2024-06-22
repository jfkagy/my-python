"""Generate all valid parentheses without function recursion.

For a timing comparison vs backtracking, see this notebook:
https://colab.research.google.com/drive/1_kxpS1sUXncC-pyW-TwUr5surUU3VOJ1?authuser=2#scrollTo=UWD8LxZz6fp9

"""


def parentheses(n: int) -> list[str]:
  """Returns a list of all valid sequences of n parentheses.

  Based on LeetCode #22.

  A sequence is valid if:
  1) it has exactly n left parentheses and n right parenthesis;
  2) up to any index in the sequence, the number of right parentheses 
     does not exceed the number of left parentheses.

  E.g., "(()())" is a valid sequence, but "())(()" is not, since by index 2
  there are two right parentheses but only one left parenthesis.
  """

  # At each step j, `seqs` accumulates all valid sequences having exactly j "(".
  # Each sequence is represented by a tuple: the first element is the number of 
  # ")" emitted so far, and the second element is the actual sequence.
  seqs = [(0, "")]
  for j in range(1, n):
    new_seqs = []
    for count, seq in seqs:
      # The number of consecutive ")" that can be appended to any sequence
      # is at most the number of "(" emitted so far (=j) minus the number of 
      # ")" already emitted (=sum(count)).
      new_seqs.extend(
          [(count + z, seq + "(" + ")" * z) for z in range(0, j + 1 - count)])
    seqs = new_seqs

  # Complete each sequence by appending the last "(" and padding it with the 
  # remaining budget of ")".
  return [seq + "(" + ")" * (n - count) for count, seq in seqs]





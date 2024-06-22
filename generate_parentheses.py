"""Generate all valid parentheses without function recursion."""

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

  if n == 1:
    return ['()']

  # At step j, `counts` encodes all valid sequences of "(" and ")" having
  # exactly j + 1 ")". Each element of `counts` is a sequence of int of
  # length j - 1 indicating the number of consecutive ")" that follows each 
  # "(". E.g., counts = [[1, 1], [0, 1], [1, 0]] denotes the sequences 
  # "()()", "(()" and "()(".
  counts = [[]]
  for j in range(1, n):
    new_counts = []
    for ix, count in enumerate(counts):
      # The number of consecutive ")" that can be appended to any sequence
      # is at most the number of "(" emitted so far (=j) minus the number of 
      # ")" already emitted (=sum(count)).
      new_counts.extend([count + [z] for z in range(0, j + 1 - sum(count)) ])
    counts = new_counts

  # Generate sequences based on `counts`.
  results = []
  for c in counts:
    s = ""
    for i in c:
        s += '(' + ')' * i
    if sum(c) < n:
        s += '(' + ')' * (n - sum(c))
    results.append(s)

  return results


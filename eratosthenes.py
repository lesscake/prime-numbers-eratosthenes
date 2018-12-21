def all_primes(n):
  table = [ True ] * n
  table[0] = table[1] = False
  primes = []

  for i, boolean in enumerate(table):
    if boolean:
      primes.append(i)
      for j in range(i, n, i):
        table[j] = False

  return primes

if __name__ == '__main__':
  print(all_primes(100))
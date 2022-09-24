import eulerlib
import itertools
import math


def compute():
	def cond(i): return all((count_distinct_prime_factors(i + j) == 4)
                         for j in range(4))
	ans = next(filter(cond, itertools.count()))
	return str(ans)


def count_distinct_prime_factors(n):
	count = 0
	while n > 1:
		count += 1
		for i in range(2, int(math.sqrt(n)) + 1):
			if n % i == 0:
				while True:
					n //= i
					if n % i != 0:
						break
				break
		else:
			break  # n is prime
	return count


if __name__ == "__main__":
	print(compute())

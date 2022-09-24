import eulerlib
import math

def list_primality(n: int):
	# Sieve of Eratosthenes
	result = [True] * (n + 1)
	result[0] = result[1] = False
	for i in range(int(math.sqrt(n)) + 1):
		if result[i]:
			for j in range(i * i, len(result), i):
				result[j] = False
	return result

def compute():
	ans = 0
	isprime = list_primality(999999)
	primes = eulerlib.primes(999999)
	consecutive = 0
	for i in range(len(primes)):
		sum = primes[i]
		consec = 1
		for j in range(i + 1, len(primes)):
			sum += primes[j]
			consec += 1
			if sum >= len(isprime):
				break
			if isprime[sum] and consec > consecutive:
				ans = sum
				consecutive = consec
	return str(ans)


if __name__ == "__main__":
	print(compute())

class Solution:
	def isHappy(self, n: int) -> bool:

		seen = set()

		while n not in seen:

			seen.add(n)
			if n == 1:
				return True

			n = self.calculatesum(n)

		return False

	def calculatesum(self, n: int) -> int:

		k = 0
		while n:

			digit = n % 10
			k += digit ** 2
			n = n // 10

		return k

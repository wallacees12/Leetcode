class Solution
	def generate_paranthesis(self, n: int) -> List[str]:

		# We need that 3 open 3 closed
		# We need closed < open
		#


		stack = []
		res = []

		def backtrack(openN, closedN):

			if openN == closedN == n:
				res.append("".join(stack))
				return
			if openN < n:
				stack.append("(")
				backtrack(openN+1, closedN)
				stack.pop()
			if closedN < openN:
				stack.append(")")
				backtrack(openN, closedN + 1)
				stack.pop()

		backtrack(0,0)

		return n


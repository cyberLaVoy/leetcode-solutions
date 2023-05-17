class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        answer = []
        for i in range(1, n+1):
            # answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            # answer[i] == "Fizz" if i is divisible by 3.
            elif i % 3 == 0:
                answer.append("Fizz")
            # answer[i] == "Buzz" if i is divisible by 5.
            elif i % 5 == 0:
                answer.append("Buzz")
            # answer[i] == i (as a string) if none of the above conditions are true.
            else:
                answer.append(str(i))
        return answer
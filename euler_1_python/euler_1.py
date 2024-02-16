import sys

def euler_1(threshold):
  """Computes the sum of the numbers divisible by 3 or 5 below the threshold"""
  return sum([n for n in range(threshold) if n %3 == 0 or n % 5 == 0])

assert euler_1(0) == 0
assert euler_1(10) == 23, f'got {euler_1(10)} instead of 23'

if __name__ == '__main__':
  print(euler_1(int(sys.argv[1])))


import math as m


def main(y, z, x):
  n = len(x)
  f = 0
  for i in range(1, n + 1):
    f += pow(25 * pow(x[n - i], 3) + z[i - 1] /
    12 + pow(y[m.floor((i - 1) / 2)], 2), 5) / 41
  return f

if __name__ == '__main__':
  print(f"{main([0.13, -0.44, -0.4, 0.64, -0.43], [0.13, -0.11, -0.49, 0.64, -0.38], [0.66, -0.55, -0.71, -0.71, 0.72])=}") 

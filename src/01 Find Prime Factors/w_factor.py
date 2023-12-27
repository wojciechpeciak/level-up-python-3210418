def get_prime_factors(number):
  limit = int(number)**(0.5)
  factor = 2
  factors = []

  while not factor > limit:
    while number % factor == 0:
      factors.append(factor)
      number = number // factor
    if number == 1:
      return factors
    else:
      factor+=1
  factors.append(number)
  return factors


print(get_prime_factors(73))
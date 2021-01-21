from networkModel import universe

getProbability = universe.probability([["exercise", "healthy", "no heart disease", "no heartache", "no chest pain", "not high"]])

print(getProbability)

getProbability = universe.probability([["no exercise", "not healthy", "heart disease", "heartache", "chest pain", "high"]])

print(getProbability)
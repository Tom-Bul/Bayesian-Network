from pomegranate import *

exercise = Node(DiscreteDistribution({
  "exercise": 0.7,
  "no exercise": 0.3
}), name="exercise")

diet = Node(DiscreteDistribution({
  "healthy": 0.25,
  "not healthy": 0.75
}), name="diet")

heart_disease = Node(ConditionalProbabilityTable([
  ["exercise", "healthy", "heart disease", 0.25],
  ["exercise", "healthy", "no heart disease", 0.75],
  ["exercise", "not healthy", "heart disease", 0.45],
  ["exercise", "not healthy", "no heart disease", 0.55],
  ["no exercise", "healthy", "heart disease", 0.55],
  ["no exercise", "healthy", "no heart disease", 0.45],
  ["no exercise", "not healthy", "heart disease", 0.75],
  ["no exercise", "not healthy", "no heart disease", 0.25],
], [exercise.distribution, diet.distribution]), name="heart disease")

heartache = Node(ConditionalProbabilityTable([
  ["healthy", "heartache", 0.2],
  ["healthy", "no heartache", 0.8],
  ["not healthy", "heartache", 0.85],
  ["not healthy", "no heartache", 0.15],
], [diet.distribution]), name="heartache")

chest_pain = Node(ConditionalProbabilityTable([
  ["heart disease", "heartache", "chest pain", 0.8],
  ["heart disease", "heartache", "no chest pain", 0.2],
  ["heart disease", "no heartache", "chest pain", 0.6],
  ["heart disease", "no heartache", "no chest pain", 0.4],
  ["no heart disease", "heartache", "chest pain", 0.4],
  ["no heart disease", "heartache", "no chest pain", 0.6],
  ["no heart disease", "no heartache", "chest pain", 0.1],
  ["no heart disease", "no heartache", "no chest pain", 0.9],
], [heart_disease.distribution, heartache.distribution]), name="chest pain")

blood_pressure = Node(ConditionalProbabilityTable([
  ["heart disease", "high", 0.85],
  ["heart disease", "not high", 0.15],
  ["no heart disease", "high", 0.2],
  ["no heart disease", "not high", 0.8],
], [heart_disease.distribution]), name="blood pressure")

universe = BayesianNetwork()
universe.add_states(exercise, diet, heart_disease, heartache, chest_pain, blood_pressure)

universe.add_edge(exercise, heart_disease)
universe.add_edge(diet, heart_disease)
universe.add_edge(diet, heartache)
universe.add_edge(heart_disease, chest_pain)
universe.add_edge(heartache, chest_pain)
universe.add_edge(heart_disease, blood_pressure)

universe.bake()
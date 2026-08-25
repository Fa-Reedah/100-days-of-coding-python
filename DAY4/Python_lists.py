# Lists (data storage)

states_in_Nigeria = ["Abia", "Adamawa", "Akwa Ibom", "Anambra", "Bauchi", "Bayelsa", "Benue", "Borno"]
print(states_in_Nigeria[3])
print(states_in_Nigeria[-2])

states_in_Nigeria[1] = "Adama"
print(states_in_Nigeria)

states_in_Nigeria.append("Fareedahland")
print(states_in_Nigeria)

states_in_Nigeria.extend(["Fareedahland", "Cross river", "Delta", "Ebonyi"])
print(states_in_Nigeria)

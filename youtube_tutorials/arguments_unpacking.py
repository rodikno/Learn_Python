def health_calculator(age, apples_eaten, cigs_smoked):
    answer = (100-age) + (apples_eaten * 3.5) - (cigs_smoked*2)
    print(answer)

data = [27, 20, 0]
health_calculator(data[0], data[1], data[2])
health_calculator(*data)
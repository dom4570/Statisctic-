import codecademylib
import numpy as np
import matplotlib.pyplot as plt


survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']

total_ceballos = 0

for survey in survey_responses:
  if survey == "Ceballos":
    total_ceballos += 1

print(total_ceballos)
survey_lenghth = float(len(survey_responses))
percentage_ceballos = 100 * total_ceballos / survey_lenghth

print(percentage_ceballos)

possible_surveys = np.random.binomial(survey_lenghth, 0.54, 10000) / survey_lenghth

plt.hist(possible_surveys, range = (0,1), bins = 20)
plt.show()

ceballos_loss_surveys = float(np.mean(possible_surveys < 0.50))
print(ceballos_loss_surveys)

large_survey = np.random.binomial(float(7000), 0.54, 10000) / float(7000)

incorrect_prediction = len(large_survey[large_survey < .50])

ceballos_loss_new = incorrect_prediction / float(7000)

print(ceballos_loss_new)

import pandas as pd

# The Dataset "HospitalDataset.csv" should be placed in the same directory.
dataset_filename = 'HospitalDataset.csv'
hospital_data = pd.read_csv(dataset_filename)

def diagnose_disease(symptoms, age, gender):
    # Filter the dataset based on user input
    condition = (
        (hospital_data['Fever'] == symptoms['Fever']) &
        (hospital_data['Cough'] == symptoms['Cough']) &
        (hospital_data['Fatigue'] == symptoms['Fatigue']) &
        (hospital_data['Difficulty Breathing'] == symptoms['Difficulty Breathing']) &
        (hospital_data['Blood Pressure'] == symptoms['Blood Pressure']) &
        (hospital_data['Age'] == age) &
        (hospital_data['Gender'] == gender)
    )

    # Get the disease column for matching condition
    possible_diseases = hospital_data.loc[condition, 'Disease'].values

    if len(possible_diseases) == 0:
        return "No matching diseases found. Please consult a healthcare professional."
    else:
        return f"You might have: {', '.join(possible_diseases)}"


def get_user_input():
    symptoms = {}
    symptoms['Fever'] = input("Do you have Fever? (Yes/No): ").capitalize()
    symptoms['Cough'] = input("Do you have Cough? (Yes/No): ").capitalize()
    symptoms['Fatigue'] = input("Do you have Fatigue? (Yes/No): ").capitalize()
    symptoms['Difficulty Breathing'] = input("Do you have Difficulty Breathing? (Yes/No): ").capitalize()
    symptoms['Blood Pressure'] = input("Enter your Blood Pressure: ")
    age = int(input("Enter your Age: "))
    gender = input("Enter your Gender (Male/Female): ").capitalize()

    return symptoms, age, gender


if __name__ == "__main__":
    user_symptoms, user_age, user_gender = get_user_input()

    diagnosis_result = diagnose_disease(user_symptoms, user_age, user_gender)

    print("\nDiagnosis Result:")
    print(diagnosis_result)

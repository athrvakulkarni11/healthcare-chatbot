import pandas as pd


df = pd.read_csv('dataset.csv')


df = df.applymap(lambda x: x.lower() if type(x) == str else x)


def health_chatbot():
    print("Welcome to the Health Chatbot!")

    
    fever = input("Do you have fever? (yes/no): ").lower()
    cough = input("Do you have cough? (yes/no): ").lower()
    fatigue = input("Are you fatigued? (yes/no): ").lower()
    breath_difficulty = input("Do you have difficulty in breathing? (yes/no): ").lower()
    age = int(input("What is your age?: "))
    
    
    user_data = {
        'fever': fever,
        'cough': cough,
        'fatigue': fatigue,
        'difficulty breathing': breath_difficulty,
        'age': age
    }

    
    user_data = {df.columns[df.columns.str.lower().str.contains(key, case=False)].values[0]: value for key, value in user_data.items()}

    
    for index, row in df.iterrows():
        if all(str(row[key]) == str(user_data[key]) for key in user_data):
            
            predicted_disease = row['Disease']
            outcome_variable = row['Outcome Variable']
            print(f"\nBased on your responses, you may have {predicted_disease}.")
            print(f"Outcome Variable: {outcome_variable}")
            return

    
    print("\nNo matching records found. Please consult a healthcare professional.")


health_chatbot()

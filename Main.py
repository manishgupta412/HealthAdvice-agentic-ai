# Importing the needed modules 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor, as_completed
from Utils.Agents import Cardiologist, Psychologist, Pulmonologist, MultidisciplinaryTeam
from dotenv import load_dotenv
import json, os
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Loading API key from a dotenv file.
load_dotenv(dotenv_path='apikey.env')

# read the medical report
with open("Medical Reports\Medical Report - Robert Miller - COPD.txt", "r") as file:
    medical_report = file.read()


agents = {
    "Cardiologist": Cardiologist(medical_report),
    "Psychologist": Psychologist(medical_report),
    "Pulmonologist": Pulmonologist(medical_report)
}

# Function to run each agent and get their response
def get_response(agent_name, agent):
    response = agent.run()
    return agent_name, response

# Run the agents concurrently and collect responses
responses = {}
with ThreadPoolExecutor() as executor:
    futures = {executor.submit(get_response, name, agent): name for name, agent in agents.items()}

    print("\nAgent Responses:")
for name, resp in responses.items():
    print(name, ":", resp)
    
    for future in as_completed(futures):
        agent_name, response = future.result()
        responses[agent_name] = response

team_agent = MultidisciplinaryTeam(
    cardiologist_report=responses["Cardiologist"],
    psychologist_report=responses["Psychologist"],
    pulmonologist_report=responses["Pulmonologist"]
)

# Run the MultidisciplinaryTeam agent to generate the final diagnosis
final_diagnosis = team_agent.run()

# Convert output safely
if isinstance(final_diagnosis, list):
    formatted = []
    for item in final_diagnosis:
        if isinstance(item, dict):
            formatted.append(str(item))
        else:
            formatted.append(item)
    final_diagnosis_text = "### Final Diagnosis:\n\n" + "\n".join(formatted)
else:
    final_diagnosis_text = "### Final Diagnosis:\n\n" + str(final_diagnosis)


# Define output path
txt_output_path = "results/final_diagnosis.txt"

# Ensure folder exists
os.makedirs(os.path.dirname(txt_output_path), exist_ok=True)

# Write result
with open(txt_output_path, "w", encoding="utf-8") as txt_file:
    txt_file.write(final_diagnosis_text)

print(f"Final diagnosis has been saved to {txt_output_path}")



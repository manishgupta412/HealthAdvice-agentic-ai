from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import os


class Agent:
    def __init__(self, medical_report=None, role=None, extra_info=None):
        self.medical_report = medical_report
        self.role = role
        self.extra_info = extra_info

        self.prompt_template = self.create_prompt_template()

        self.model = ChatGoogleGenerativeAI(
            model="gemini-3-flash-preview",
            temperature=0,
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )


    def create_prompt_template(self):

        if self.role == "MultidisciplinaryTeam":

            template = """
Act like a multidisciplinary team of healthcare professionals.

Analyze the reports from different specialists and list 3 possible health issues with reasons.

Cardiologist Report:
{cardiologist_report}

Psychologist Report:
{psychologist_report}

Pulmonologist Report:
{pulmonologist_report}
"""

        else:

            templates = {

                "Cardiologist": """
Act like a cardiologist.

Review the medical report and identify possible cardiac issues.

Medical Report:
{medical_report}
""",

                "Psychologist": """
Act like a psychologist.

Review the report and identify possible psychological issues.

Patient Report:
{medical_report}
""",

                "Pulmonologist": """
Act like a pulmonologist.

Review the report and identify possible respiratory issues.

Patient Report:
{medical_report}
"""
            }

            template = templates[self.role]

        return PromptTemplate.from_template(template)


    def run(self):

        print(f"{self.role} is running...")

        try:

            if self.role == "MultidisciplinaryTeam":

                prompt = self.prompt_template.format(
                    cardiologist_report=self.extra_info.get("cardiologist_report", ""),
                    psychologist_report=self.extra_info.get("psychologist_report", ""),
                    pulmonologist_report=self.extra_info.get("pulmonologist_report", "")
                )

            else:

                prompt = self.prompt_template.format(
                    medical_report=self.medical_report
                )

            response = self.model.invoke(prompt)

            return response.content

        except Exception as e:
            print("Error occurred:", e)
            return None

# Define specialized agent classes
class Cardiologist(Agent):
    def __init__(self, medical_report):
        super().__init__(medical_report, "Cardiologist")

class Psychologist(Agent):
    def __init__(self, medical_report):
        super().__init__(medical_report, "Psychologist")

class Pulmonologist(Agent):
    def __init__(self, medical_report):
        super().__init__(medical_report, "Pulmonologist")

class MultidisciplinaryTeam(Agent):
    def __init__(self, cardiologist_report, psychologist_report, pulmonologist_report):
        extra_info = {
            "cardiologist_report": cardiologist_report,
            "psychologist_report": psychologist_report,
            "pulmonologist_report": pulmonologist_report
        }
        super().__init__(role="MultidisciplinaryTeam", extra_info=extra_info)

import os
import sys

# Attempt to import docx_generator
sys.path.insert(0, r"C:\Users\Rohit yadav\.gemini\antigravity\brain\cdab3f9b-499f-4ec5-8ac6-3599e1d39acf\scratch")
try:
    from docx_generator import create_practice_guide
except ImportError:
    print("Error: docx_generator not found in the specified path.")
    sys.exit(1)

base_dir = r"D:\LEARN_PYTHON\Practice\09_pandas_practice"

# Let's define a helper function to create a docx file
def make_docx(folder, filename, questions):
    full_dir = os.path.join(base_dir, folder)
    os.makedirs(full_dir, exist_ok=True)
    full_path = os.path.join(full_dir, filename)
    create_practice_guide(questions, full_path)
    print(f"Created {full_path}")

# --- 01_Easy ---
easy_series_qs = [
    {
        "title": "Create a Basic Series",
        "explanation": "Pandas mein Series ek 1D array ki tarah hoti hai. Ismein aap koi bhi data type store kar sakte hain. Yeh ek list ka advanced version hai jismein index bhi hota hai.",
        "difficulty": "Easy",
        "concept": "Series Creation",
        "approach": "1. pandas ko import karein. 2. pd.Series() function use karein aur ek list pass karein.",
        "methods_used": "pd.Series()",
        "time_complexity": "O(N)",
        "space_complexity": "O(N)",
        "edge_cases": "Empty list pass karna, ya different data types mix karna.",
        "code": "import pandas as pd\n\ndata = [10, 20, 30, 40, 50]\nmy_series = pd.Series(data)\nprint(my_series)",
        "alternative": "Aap dictionary pass karke bhi Series bana sakte hain jahan keys index ban jayengi.",
        "interview_followup": "Agar main list mein ek string aur baaki numbers daalun, toh Series ka dtype kya hoga?"
    }
]

make_docx("01_Easy/Series_Operations", "Pandas_Series_Notes_Easy_Questions.docx", easy_series_qs)

print("Successfully generated all the files!")

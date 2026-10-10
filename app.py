from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

# I created a simple database of common diseases with their symptoms and management tips
# In a real production app, I'd use a proper medical database or API
# This is just for learning purposes and educational use
disease_database = {
    "Common Cold": {
        "symptoms": ["runny nose", "sneezing", "sore throat", "cough", "mild fever", "headache", "fatigue"],
        "management": [
            "Get plenty of rest",
            "Drink lots of fluids (water, juice, warm broth)",
            "Use over-the-counter cold medications",
            "Gargle with salt water for sore throat",
            "Use a humidifier to ease congestion",
            "Rest and avoid strenuous activities"
        ],
        "severity": "mild",
        "when_to_see_doctor": "If symptoms last more than 10 days or you have high fever"
    },
    "Flu (Influenza)": {
        "symptoms": ["high fever", "body aches", "chills", "fatigue", "dry cough", "sore throat", "headache", "runny nose"],
        "management": [
            "Rest and stay home",
            "Drink plenty of fluids",
            "Take antiviral medications if prescribed",
            "Use over-the-counter pain relievers",
            "Monitor your temperature regularly",
            "Isolate yourself to prevent spreading"
        ],
        "severity": "moderate",
        "when_to_see_doctor": "If you have difficulty breathing, chest pain, or high fever that won't go away"
    },
    "COVID-19": {
        "symptoms": ["fever", "cough", "shortness of breath", "loss of taste", "loss of smell", "fatigue", "body aches", "sore throat"],
        "management": [
            "Isolate yourself from others",
            "Monitor your symptoms closely",
            "Rest and stay hydrated",
            "Take over-the-counter medications for symptoms",
            "Use a pulse oximeter if available",
            "Seek emergency care if breathing becomes difficult"
        ],
        "severity": "moderate to severe",
        "when_to_see_doctor": "Immediately if you have difficulty breathing, persistent chest pain, or confusion"
    },
    "Gastroenteritis (Stomach Flu)": {
        "symptoms": ["nausea", "vomiting", "diarrhea", "stomach cramps", "low fever", "headache", "muscle aches"],
        "management": [
            "Stay hydrated with clear fluids",
            "Eat bland foods (BRAT diet: bananas, rice, applesauce, toast)",
            "Rest your stomach for a few hours",
            "Avoid dairy, caffeine, and spicy foods",
            "Gradually return to normal diet",
            "Wash hands frequently to prevent spread"
        ],
        "severity": "mild to moderate",
        "when_to_see_doctor": "If you see blood in stool, have severe abdominal pain, or signs of dehydration"
    },
    "Migraine": {
        "symptoms": ["severe headache", "nausea", "vomiting", "sensitivity to light", "sensitivity to sound", "visual aura", "dizziness"],
        "management": [
            "Rest in a dark, quiet room",
            "Apply cold or warm compresses",
            "Take migraine medications as prescribed",
            "Stay hydrated",
            "Try relaxation techniques",
            "Keep a headache diary to identify triggers"
        ],
        "severity": "moderate",
        "when_to_see_doctor": "If headaches become more frequent or severe, or if you have sudden severe headache"
    },
    "Allergies": {
        "symptoms": ["sneezing", "runny nose", "itchy eyes", "watery eyes", "skin rash", "hives", "swelling", "itching"],
        "management": [
            "Avoid known allergens",
            "Take antihistamines as needed",
            "Use nasal sprays for congestion",
            "Apply cold compresses to skin rashes",
            "Keep windows closed during high pollen seasons",
            "Wash bedding regularly in hot water"
        ],
        "severity": "mild to moderate",
        "when_to_see_doctor": "If you have difficulty breathing or swelling of the throat"
    },
    "Bronchitis": {
        "symptoms": ["persistent cough", "chest discomfort", "shortness of breath", "mild fever", "fatigue", "production of mucus"],
        "management": [
            "Get plenty of rest",
            "Drink lots of fluids",
            "Use a humidifier",
            "Avoid smoke and other irritants",
            "Take over-the-counter cough medicine",
            "Practice breathing exercises"
        ],
        "severity": "mild to moderate",
        "when_to_see_doctor": "If cough lasts more than 3 weeks or you have high fever"
    },
    "Sinusitis": {
        "symptoms": ["facial pain", "nasal congestion", "headache", "reduced sense of smell", "thick nasal discharge", "fever", "bad breath"],
        "management": [
            "Use nasal saline rinses",
            "Apply warm compresses to face",
            "Stay hydrated",
            "Use decongestants",
            "Sleep with your head elevated",
            "Avoid irritants like smoke"
        ],
        "severity": "mild to moderate",
        "when_to_see_doctor": "If symptoms last more than 10 days or you have severe headache"
    },
    "Anemia": {
        "symptoms": ["fatigue", "weakness", "pale skin", "shortness of breath", "dizziness", "cold hands and feet", "headache"],
        "management": [
            "Eat iron-rich foods (red meat, spinach, beans)",
            "Take iron supplements if prescribed",
            "Increase vitamin C intake",
            "Avoid caffeine with meals",
            "Get regular exercise",
            "Have regular blood tests"
        ],
        "severity": "mild to moderate",
        "when_to_see_doctor": "If symptoms worsen or you have chest pain"
    },
    "Dehydration": {
        "symptoms": ["dry mouth", "extreme thirst", "dark urine", "dizziness", "fatigue", "dry skin", "headache", "confusion"],
        "management": [
            "Drink water immediately",
            "Oral rehydration solutions",
            "Avoid caffeine and alcohol",
            "Eat water-rich foods",
            "Rest in a cool place",
            "Monitor urine color"
        ],
        "severity": "mild to severe",
        "when_to_see_doctor": "If you have severe confusion, fainting, or can't keep fluids down"
    }
}

def analyze_symptoms(user_symptoms):
    """
    This function takes the user's symptoms and tries to match them
    against the diseases in my database. It calculates a match percentage
    and returns the most likely conditions.
    """
    results = []
    
    # Go through each disease in the database
    for disease, data in disease_database.items():
        # Convert everything to lowercase for easier matching
        disease_symptoms = [s.lower() for s in data["symptoms"]]
        user_symptoms_lower = [s.lower() for s in user_symptoms]
        
        # Count how many of the user's symptoms match this disease
        matches = 0
        for symptom in user_symptoms_lower:
            if any(symptom in ds for ds in disease_symptoms):
                matches += 1
        
        # Calculate the match percentage
        if len(user_symptoms_lower) > 0:
            match_percentage = (matches / len(user_symptoms_lower)) * 100
        else:
            match_percentage = 0
        
        # Only add this disease if there's at least some match
        if match_percentage > 0:
            results.append({
                "disease": disease,
                "match_percentage": round(match_percentage, 1),
                "severity": data["severity"],
                "management": data["management"],
                "when_to_see_doctor": data["when_to_see_doctor"]
            })
    
    # Sort the results so the highest matches come first
    results.sort(key=lambda x: x["match_percentage"], reverse=True)
    
    return results

@app.route('/')
def home():
    """This is the main page - just renders the HTML template"""
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    """This endpoint takes the symptoms from the frontend and analyzes them"""
    try:
        # Get the symptoms data from the request
        data = request.get_json()
        symptoms_text = data.get('symptoms', '')
        
        # Split the symptoms by comma and clean up any extra spaces
        symptoms = [s.strip() for s in symptoms_text.split(',') if s.strip()]
        
        # Make sure the user actually entered something
        if not symptoms:
            return jsonify({"error": "Please enter at least one symptom"}), 400
        
        # Run the analysis function
        results = analyze_symptoms(symptoms)
        
        # If no matches found, let the user know
        if not results:
            return jsonify({"error": "No matching conditions found. Try different symptoms."}), 404
        
        # Send the results back to the frontend
        return jsonify({"results": results})
    
    except Exception as e:
        # If something goes wrong, return an error message
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/diseases')
def diseases():
    """This endpoint returns a list of all diseases in the database"""
    diseases_list = list(disease_database.keys())
    return jsonify({"diseases": diseases_list})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=5000)

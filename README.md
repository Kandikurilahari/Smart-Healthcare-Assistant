# Smart Healthcare Assistant

A healthcare web application I built using Python and Flask to help analyze symptoms and provide basic disease management suggestions. This was a learning project to understand web development with Flask and basic symptom analysis.

## Features

- **Symptom Analysis** - Enter your symptoms and get possible disease predictions
- **Match Percentage** - See how well your symptoms match each condition
- **Management Suggestions** - Get basic tips for managing each condition
- **Severity Indicators** - See the severity level of each possible condition
- **Doctor Recommendations** - Know when you should see a doctor
- **User-Friendly Interface** - Simple and clean design with healthcare theme

## Supported Conditions

The app can analyze symptoms for these common conditions:
- Common Cold
- Flu (Influenza)
- COVID-19
- Gastroenteritis (Stomach Flu)
- Migraine
- Allergies
- Bronchitis
- Sinusitis
- Anemia
- Dehydration

## Tech Stack

- **Python** - Backend logic
- **Flask** - Web framework
- **HTML** - Frontend structure
- **CSS** - Styling
- **JavaScript** - Frontend interactivity
- **LocalStorage** - (could be added for saving history)

## Installation

1. Make sure you have Python installed
2. Install Flask:
```bash
pip install Flask
```

Or use the requirements file:
```bash
pip install -r requirements.txt
```

## How to Run

1. Navigate to the project directory
2. Run the Flask app:
```bash
python app.py
```
3. Open your browser and go to: http://localhost:5000

## How to Use

1. Enter your symptoms in the text area (separated by commas)
   - Example: "fever, cough, headache, fatigue"
2. Click "Analyze Symptoms"
3. View the possible conditions and their match percentages
4. Read the management suggestions for each condition
5. Check the severity indicator and when to see a doctor

## Project Structure

```
HealthcareApp/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html     # HTML template
├── static/
│   └── style.css      # CSS styling
└── README.md          # This file
```

## Important Disclaimer

⚠️ **This tool is for educational purposes only and should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.**

## Future Improvements

- [ ] Add more diseases to the database
- [ ] Use a proper medical API or database
- [ ] Add user authentication
- [ ] Save symptom history
- [ ] Add machine learning for better predictions
- [ ] Add mobile app version
- [ ] Include medication information
- [ ] Add location-based doctor recommendations

## Learning Outcomes

This project helped me learn:
- Building web applications with Flask
- Creating REST API endpoints
- Working with JSON data
- Frontend-backend communication
- Basic symptom matching algorithms
- Building user-friendly interfaces

## License

This is a personal learning project. Feel free to use it for educational purposes!

## Contact

If you have questions or suggestions, feel free to reach out!

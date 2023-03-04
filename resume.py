from flask import Flask, jsonify, json, render_template
import click

app = Flask(__name__)

# Load data from JSON file
with open('Resources/resume.json', 'r') as f:
    cv_data = json.load(f)

# Define endpoints
@app.route('/personal')
def get_personal_info():
   return render_template('personal.html', data=cv_data)

@app.route('/experience')
def get_experience():
    return render_template('experience.html', data=cv_data)

@app.route('/education')
def get_education():
    return render_template('education.html', data=cv_data)

# User interface
@app.route('/')
def index():
    return render_template('index.html', data=cv_data)

#Format output for CLI usage
@app.cli.command('json_data')
def print_json_data():
    for section, section_data in cv_data.items():
        print(f"\n{section.title()}:")

        if section == 'skills':
            for skill in section_data:
                print(f"{skill['name']}: {skill['level']}")
        elif section == 'experience':
            for job in section_data:
                print(
                    f"{job['title']} at {job['company']}, {job['location']} from {job['start_date']} to {job['end_date']}:\n{job['description']}\n")
        elif section == 'education':
            for degree in section_data:
                print(
                    f"{degree['degree']} from {degree['institution']}, {degree['location']} from {degree['start_date']} to {degree['end_date']}")
        else:
            for key, value in section_data.items():
                print(f"{key.title()}: {value}")



if __name__ == '__main__':
    app.run(debug=True)

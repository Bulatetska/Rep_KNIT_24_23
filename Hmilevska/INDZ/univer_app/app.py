from flask import Flask, jsonify, request
from flask_cors import CORS
from itertools import groupby

app = Flask(__name__)
CORS(app)

@app.route('/')
def get_text():
    response = 'This is text from Python!'  # Sample text response
    return response

@app.route('/menu')
def get_menu():
    menu_data = [
        {"title": "Add Student Profile", "link": "/profile"},
        {"title": "Student Profiles", "link": "/profiles"},
        {"title": "Add Customer Profile", "link": "/customer-profile"},
        {"title": "Customer Profiles", "link": "/customer-profiles"},
        {"title": "Calculations", "link": "/calculations"},
        {"title": "Register", "link": "/register"},
        {"title": "Login", "link": "/login"}
    ]
    return jsonify(menu_data)

profiles = []  # List to store profiles
customer_profiles = []  # List to store customer profiles

@app.route('/profiles', methods=['POST', 'GET'])
def handle_profiles():
    if request.method == 'POST':
        data = request.get_json()
        profiles.append(data)  # Add new profile to the list
        return 'OK', 200
    elif request.method == 'GET':
        return jsonify(profiles)  # Return all profiles as JSON

@app.route('/customer-profiles', methods=['POST', 'GET'])
def handle_customer_profiles():
    if request.method == 'POST':
        data = request.get_json()
        customer_profiles.append(data)  # Add new customer profile to the list
        return 'OK', 200
    elif request.method == 'GET':
        return jsonify(customer_profiles)  # Return all customer profiles as JSON

@app.route('/calculations', methods=['GET'])
def perform_calculations():
    try:
        total_profiles = len(profiles)  # Calculate total number of profiles
        total_rating = sum(int(profile['rating']) for profile in profiles)  # Calculate total rating

        average_rating = total_rating / total_profiles if total_profiles > 0 else 0  # Calculate average rating

        category_ratings = {}  # Dictionary to store category ratings
        category_min_profiles = {}  # Dictionary to store profiles with minimum rating in each category
        category_max_profiles = {}  # Dictionary to store profiles with maximum rating in each category

        for category, group in groupby(profiles, key=lambda p: p['category']):
            category_profiles = list(group)
            category_total_rating = sum(int(profile['rating']) for profile in category_profiles)
            category_average_rating = category_total_rating / len(category_profiles) if len(category_profiles) > 0 else 0

            category_ratings[category] = {
                'total_rating': category_total_rating,
                'average_rating': category_average_rating
            }

            min_rating_profile = min(category_profiles, key=lambda p: int(p['rating']))
            max_rating_profile = max(category_profiles, key=lambda p: int(p['rating']))

            category_min_profiles[category] = min_rating_profile
            category_max_profiles[category] = max_rating_profile

        response = {
            'total_profiles': total_profiles,
            'total_rating': total_rating,
            'average_rating': average_rating,
            'category_ratings': category_ratings,
            'category_min_profiles': category_min_profiles,
            'category_max_profiles': category_max_profiles
        }

        return jsonify(response)  # Return calculations as JSON
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Return error message with HTTP status code 500

if __name__ == '__main__':
    app.run(port=8000)

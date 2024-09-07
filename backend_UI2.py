from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('frontend_UI3.html')

@app.route('/api/test_case', methods=['POST'])
def test_case():
    data = request.json
    prompt = data.get('prompt', '')

    # Example processing based on the prompt; in a real application, you would have more complex logic
    response_data = {
        "prompt": prompt,
        "complexity": "simple" if "?" in prompt else "complex",
        "task_type": "general_knowledge",
        "ideal_model": "small_efficient_model" if "?" in prompt else "large_powerful_model",
        "energy_efficiency": {
            "energy_saved": "50 kWh",
            "power_usage": "200 W",
            "environmental_impact": "Minimal"
        }
    }
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)

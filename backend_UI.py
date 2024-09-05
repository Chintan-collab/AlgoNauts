from flask import Flask, request, jsonify
from flask import Flask, render_template
import plotly.graph_objs as go
import plotly.io as pio

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('frontend_UI.html')


# Mock data for test cases
test_cases = [
    {"name": "Test Case 1", "status": "Pass"},
    {"name": "Test Case 2", "status": "Fail"},
    {"name": "Test Case 3", "status": "Pass"},
    {"name": "Test Case 4", "status": "Fail"},
]

# Heuristic for classifying prompt
def classify_prompt(prompt):
    word_count = len(prompt.split())
    if word_count > 10:
        return 'complex', 'Large LLM'
    else:
        return 'simple', 'Small LLM'

# API endpoint for handling prompt classification
@app.route('/classify', methods=['POST'])
def classify():
    data = request.json
    prompt = data.get('prompt', '')

    complexity, model = classify_prompt(prompt)
    return jsonify({
        'complexity': complexity,
        'model': model
    })

# API endpoint to fetch test case results and generate graph
@app.route('/test_case_status', methods=['GET'])
def test_case_status():
    pass_count = sum(1 for case in test_cases if case['status'] == 'Pass')
    fail_count = sum(1 for case in test_cases if case['status'] == 'Fail')
    
    # Create a simple pie chart using Plotly
    labels = ['Pass', 'Fail']
    values = [pass_count, fail_count]
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig.update_traces(marker=dict(colors=['green', 'red']))

    graph_html = pio.to_html(fig, full_html=False)

    return jsonify({
        'test_cases': test_cases,
        'graph_html': graph_html
    })

if __name__ == "__main__":
    app.run(debug=True)

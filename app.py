from flask import Flask, render_template, request, jsonify
import pennylane as qml
import numpy as np
import os

app = Flask(__name__)

# ================================================================
# QUANTUM SETUP  — unchanged from original
# ================================================================
dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def quantum_circuit(theta):
    # Step 1: Hadamard — puts voter in superposition (undecided)
    qml.Hadamard(wires=0)

    # Step 2: RY rotation — applies influence
    # CHANGED: theta can now be negative (bias toward B)
    #          or positive (bias toward A), or 0 (neutral)
    qml.RY(theta, wires=0)

    # Step 3: Return measurement probabilities [P(A), P(B)]
    return qml.probs(wires=0)


# ================================================================
# SIMULATION FUNCTION
# CHANGED: influence now ranges from -1 to +1
#   +1 → full bias toward Candidate A
#    0 → neutral 50/50
#   -1 → full bias toward Candidate B
# ================================================================
def simulate_votes(num_voters, influence):
    votes = {"Candidate A": 0, "Candidate B": 0}

    # CHANGED: theta = influence * pi
    # Positive influence → positive theta → rotates toward |0⟩ (Candidate A)
    # Negative influence → negative theta → rotates toward |1⟩ (Candidate B)
    theta = influence * np.pi

    for _ in range(num_voters):
        probs = quantum_circuit(theta)

        # Simulate quantum measurement — collapses to 0 (A) or 1 (B)
        result = np.random.choice([0, 1], p=probs)

        if result == 0:
            votes["Candidate A"] += 1
        else:
            votes["Candidate B"] += 1

    return votes


# ================================================================
# ROUTES
# ================================================================

@app.route('/')
def home():
    return render_template('index.html')


# CHANGED: Added /simulate JSON endpoint for single-page use
# The old /result POST route is kept below so nothing breaks
@app.route('/simulate', methods=['POST'])
def simulate():
    data      = request.get_json()
    voters    = int(data.get('voters', 100))

    # CHANGED: influence now accepted as -1 to +1, clamped for safety
    influence = float(data.get('influence', 0))
    influence = max(-1.0, min(1.0, influence))

    votes = simulate_votes(voters, influence)

    total     = voters
    percent_a = round((votes["Candidate A"] / total) * 100, 2)
    percent_b = round((votes["Candidate B"] / total) * 100, 2)
    winner    = "Candidate A" if votes["Candidate A"] > votes["Candidate B"] else "Candidate B"

    # CHANGED: also return bias_direction so the frontend can label it clearly
    if influence > 0.05:
        bias_direction = "toward Candidate A"
    elif influence < -0.05:
        bias_direction = "toward Candidate B"
    else:
        bias_direction = "neutral (no bias)"

    return jsonify({
        "votes_a":        votes["Candidate A"],
        "votes_b":        votes["Candidate B"],
        "percent_a":      percent_a,
        "percent_b":      percent_b,
        "winner":         winner,
        "total":          total,
        "influence":      influence,
        "bias_direction": bias_direction,
        "theta":          round(influence * np.pi, 3)
    })


# Original route — kept intact so old code still works
@app.route('/result', methods=['POST'])
def result():
    voters    = int(request.form['voters'])
    influence = float(request.form['influence'])
    votes     = simulate_votes(voters, influence)
    total     = voters
    percent_a = round((votes["Candidate A"] / total) * 100, 2)
    percent_b = round((votes["Candidate B"] / total) * 100, 2)
    winner    = "Candidate A" if votes["Candidate A"] > votes["Candidate B"] else "Candidate B"
    return render_template('result.html',
                           votes=votes,
                           percent_a=percent_a,
                           percent_b=percent_b,
                           winner=winner)


# ================================================================
if __name__ == '__main__':
    app.run(debug=True)

# Quantum Election Simulator (QES)

## Overview

The Quantum Election Simulator (QES) is a web-based application that models voting behavior using **quantum-inspired probabilistic concepts**. The system represents each voter as a qubit and simulates how external influence affects decision-making.

This project bridges the gap between **quantum computing theory and real-world applications**, providing an interactive and educational platform.

---

## Key Features

* Qubit-based voter modeling
* Superposition using Hadamard Gate
* Influence modeling using Rotation (RY) Gate
* Bidirectional influence (-1 to +1)
* Real-time simulation results
* Graphical visualization using Chart.js
* Clean and responsive user interface

---

## Tech Stack

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* Flask

### Simulation

* PennyLane
* NumPy

### Visualization

* Chart.js

---

## Project Structure

```
quantum-election-simulator/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
```

---

## How It Works

1. Each voter is modeled as a **qubit initialized in state |0⟩**

2. **Hadamard Gate (H)** creates superposition (equal probability)

3. **Rotation Gate (RY)** applies influence:

   θ = influence × π

4. Measurement determines the final vote:

   * |0⟩ → Candidate A
   * |1⟩ → Candidate B

5. Results are aggregated and displayed graphically

---

## Installation & Setup

### 1. Clone the Repository

```
git clone https://github.com/aditibhoir06/quantum-election-simulator.git
cd quantum-election-simulator
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Run the Application

```
python app.py
```

### 4. Open in Browser

```
http://127.0.0.1:5000
```

---

## Deployment

The application can be deployed using platforms like:

* Render
* Railway
* Replit

Make sure to update:

```
app.run(host="0.0.0.0", port=10000)
```

---

## Sample Inputs

| Voters | Influence | Expected Result      |
| ------ | --------- | -------------------- |
| 100    | 0         | ~50-50 split         |
| 100    | +0.8      | Candidate A dominant |
| 100    | -0.8      | Candidate B dominant |

---

## Challenges Faced

* Python version compatibility issues
* Qiskit installation errors
* Transition to PennyLane
* Frontend-backend integration debugging
* Visualization issues with Chart.js

---

## Future Scope

* Multi-candidate election support
* Integration with real quantum hardware (IBM Quantum)
* Advanced behavioral modeling
* Enhanced UI/UX

---

## Author

Aditi Bhoir
Electronics and Computer Science Engineering

---

## License

This project is for academic purposes.

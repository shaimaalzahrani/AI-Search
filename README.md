# 🧠 AI Medical Diagnosis System

This project is an **Intelligent Diagnostic System (IDS)** developed as part of an Artificial Intelligence course. The system simulates basic medical reasoning by analyzing patient symptoms and suggesting possible diagnoses, tests, and treatments.

---

## 📌 Overview

The goal of this project is to demonstrate how different AI techniques can be combined to model a real-world problem in the medical domain.

The system takes patient symptoms as input and processes them using logical rules and search algorithms to:

- Identify possible diseases  
- Recommend diagnostic tests  
- Suggest appropriate treatments  

---

## ⚙️ Features

- Knowledge representation using **First-Order Logic (FOL)**
- Rule-based reasoning (designed for Prolog integration)
- Implementation of **Search Algorithms**
- Performance comparison between algorithms
- Simple and clear system workflow

---

## 🔍 Search Algorithms

This project implements and compares two search algorithms:

### 1. Breadth-First Search (BFS)
- Uninformed search algorithm  
- Explores all possible paths equally  
- Guarantees finding a solution  
- Less efficient due to exploring many nodes  

### 2. A* Search (A-Star)
- Informed search algorithm  
- Uses a heuristic to guide the search  
- Explores fewer nodes  
- More efficient and faster  

---

## 🧪 Example Output

The system outputs:

- Path to diagnosis  
- Nodes explored  
- Execution time  
- Exploration order of nodes  

Example:

BFS Result:
Path: start → pcr → diagnosis  
Nodes explored: 5  
Time: 0.0001 seconds  

A* Result:
Path: start → pcr → diagnosis  
Nodes explored: 3  
Time: 0.00005 seconds  

---

## ▶️ How to Run

1. Make sure Python is installed  
2. Run the following command:

python3 main.py

---

## 🧰 Technologies Used

- Python  
- First-Order Logic (FOL)  
- Search Algorithms (BFS, A*)  
- AI Concepts (Knowledge Representation, Reasoning, Search)

---

## 📊 Project Structure

ai-medical-diagnosis-system/
│
├── main.py
├── README.md

---

## 🎯 Purpose

This project demonstrates how AI can be used to simulate decision-making in healthcare by combining:

- Logical reasoning  
- Search strategies  
- Structured knowledge representation  

---

## 👩‍💻 Authors

- AI Course Students (Group Project)

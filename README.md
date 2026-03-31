
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
Result Path: start → pcr → diagnosis
Explored order: start → pcr → blood → xray → diagnosis
Nodes explored: 5
Time: 4e-06 seconds

A* Result:
Result Path: start → pcr → diagnosis
Explored order: start → pcr → diagnosis
Nodes explored: 3
Time: 3e-06 seconds

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


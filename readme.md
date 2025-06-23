# 📚 Crossword Puzzle Auto Generator & Solver using CSP

This project is a fully functional **crossword puzzle generator and solver**, developed in Python using **Constraint Satisfaction Problem (CSP)** modeling. It auto-generates crossword puzzles based on a blank or partially-filled grid, using real English words, while enforcing valid intersections and grid structure.

It includes:
- A full CSP solver
- Word slot extraction engine
- Intelligent dictionary filtering
- A GUI built with Tkinter
- Performance evaluation metrics like solve time and fill rate

---

## 🧠 Key Features

- 🔁 CSP-based auto-filling of crossword puzzles
- 📚 Uses NLTK's word corpus for real dictionary words
- ✍️ Works on both blank and **partially-filled** grids
- 📐 Automatically detects horizontal & vertical word slots
- ✅ Validates intersections and word lengths
- 🖥️ Tkinter GUI to display and interact with generated puzzles
- 📊 Displays metrics: solve time, fill rate, and slot usage

---

## 🔧 Tech Stack

- **Python 3.10+**
- `python-constraint` (for CSP modeling)
- `nltk` (for dictionary word lists)
- `tkinter` (for GUI)
- VS Code / Linux

---

## 📁 Folder Structure

CrosswordSolver/
├── assets/ # Sample puzzle grids
│ └── sample_grid.txt
├── csp/
│ └── solver.py # CSP setup and solving
├── dictionary/
│ └── word_loader.py # Dictionary loading and filtering
├── grid/
│ └── crossword_grid.py # Grid parsing, slot extraction, filler
├── ui/
│ └── gui.py # GUI logic using Tkinter
├── main.py # CLI tester
├── gui_main.py # GUI launcher
├── requirements.txt
└── README.md # This file


---

## ▶️ How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
python main.py //cli mode
python gui_main.py /gui mode

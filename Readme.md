# Deadlock Detection & Avoidance Simulator

### Operating Systems Lab Project | Python

A Python-based console application that demonstrates **Deadlock Detection and Deadlock Avoidance using the Banker's Algorithm**. This project helps understand how operating systems manage limited resources, prevent unsafe allocations, and identify possible deadlock situations.

---

## 📌 Table of Contents

1. Project Overview
2. Objectives
3. Concepts Used
4. Features
5. Technologies Used
6. Project Structure
7. Installation and Setup
8. How to Run
9. Input Format
10. Sample Input
11. Sample Output
12. Algorithms Used
13. Expected Results
14. Applications
15. Limitations
16. Future Improvements
17. Learning Outcomes
18. Author

---

## 1. Project Overview

Deadlock is a situation in an operating system where two or more processes are unable to continue their execution because each process is waiting for a resource held by another process.

To understand and demonstrate this problem, this project implements a **Deadlock Detection and Avoidance Simulator** using Python.

The project uses the Banker's Algorithm to determine whether the system is in a safe state and whether a resource request can be granted without making the system unsafe.

It also implements a separate deadlock detection mechanism that checks the currently outstanding resource requests of processes.

The simulator accepts process and resource information from the user and displays the results in the terminal.

---

## 2. Objectives

The main objectives of this project are:

- To understand the concept of deadlock in operating systems.
- To implement the Banker's Safety Algorithm using Python.
- To calculate the Need Matrix.
- To determine whether the system is in a safe or unsafe state.
- To display a safe sequence of process execution.
- To detect possible deadlock situations.
- To validate additional resource requests.
- To understand how operating systems allocate limited resources.

---

## 3. Concepts Used

### A. Deadlock

Deadlock occurs when a group of processes remains blocked because each process is waiting for resources that cannot currently be allocated.

### B. Deadlock Avoidance

Deadlock avoidance checks whether granting a resource request will keep the system in a safe state.

### C. Banker's Algorithm

The Banker's Algorithm is a resource-allocation algorithm that checks whether the system can complete all processes in some safe sequence.

### D. Safe State

A system is in a safe state if there is at least one sequence in which every process can complete its execution using the available resources and resources released by completed processes.

### E. Need Matrix

The Need Matrix represents the remaining resources required by each process.

**Formula:**

`Need = Maximum - Allocation`

---

## 4. Features

The project includes the following features:

- User input for the number of processes and resource types.
- Input of Allocation Matrix.
- Input of Maximum Matrix.
- Input of Available Resources.
- Automatic calculation of the Need Matrix.
- Banker's Safety Algorithm implementation.
- Safe and unsafe state identification.
- Display of the safe execution sequence.
- Separate deadlock detection using the current Request Matrix.
- Additional resource request validation.
- Clear console-based output.
- Basic input validation for resource values.

---

## 5. Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Main programming language |
| VS Code | Code editor |
| Terminal | Program execution |
| Lists | Storing matrices and resource values |
| Loops | Iterating through processes |
| Conditional Statements | Checking resource conditions |
| Functions | Dividing the program into modules |

**External libraries:** No external Python libraries are required.

---

## 6. Project Structure

```text
Deadlock_Detection_Avoidance_Project/
│
├── deadlock_simulator.py
│
├── README.md
│
├── Project_Report_10_Pages.pdf
│
├── sample_output.txt
│
└── screenshots/
    ├── bankers_safety.png
    ├── deadlock_detection.png
    └── final_summary.png
```

### File Description

- `deadlock_simulator.py` – Main Python source code.
- `README.md` – Project documentation.
- `Project_Report_10_Pages.pdf` – Detailed project report.
- `sample_output.txt` – Example program output.
- `screenshots/` – Screenshots showing the execution and results.

---

## 7. Installation and Setup

Follow these steps to set up the project:

**Step 1:** Install Python 3 on your computer.

**Step 2:** Install Visual Studio Code.

**Step 3:** Download or clone the project repository.

**Step 4:** Extract the ZIP file if you downloaded the project.

**Step 5:** Open the project folder in VS Code.

**Step 6:** Open the terminal in VS Code.

Check Python installation:

```bash
python --version
```

---

## 8. How to Run

Open the terminal inside the project folder and execute:

```bash
python deadlock_simulator.py
```

If the above command does not work on Windows, try:

```bash
py deadlock_simulator.py
```

The program will ask the user to enter:

1. Number of processes.
2. Number of resource types.
3. Allocation Matrix.
4. Maximum Matrix.
5. Available Resources.
6. Current outstanding Request Matrix.

After entering the values, the program performs the required calculations and displays the results.

---

## 9. Input Format

The program accepts the following inputs:

| Input | Description |
|---|---|
| Number of Processes | Total processes in the system |
| Number of Resources | Total resource types |
| Allocation Matrix | Resources currently allocated |
| Maximum Matrix | Maximum resources required |
| Available Vector | Resources currently available |
| Request Matrix | Current outstanding resource requests |

All matrix rows must contain the same number of values as the number of resource types.

---

## 10. Sample Input

```text
Number of processes: 5
Number of resource types: 3

Allocation Matrix:
P0: 0 1 0
P1: 2 0 0
P2: 3 0 2
P3: 2 1 1
P4: 0 0 2

Maximum Matrix:
P0: 7 5 3
P1: 3 2 2
P2: 9 0 2
P3: 2 2 2
P4: 4 3 3

Available Vector:
3 3 2
```

---

## 11. Sample Output

```text
Need Matrix
P0: 7 4 3
P1: 1 2 2
P2: 6 0 0
P3: 0 1 1
P4: 4 3 1

Banker's Safety Check

Initial Work: [3, 3, 2]

P1 can finish
P3 can finish
P4 can finish
P0 can finish
P2 can finish

SAFE STATE

Safe Sequence:
P1 -> P3 -> P4 -> P0 -> P2
```

### Deadlock Detection Output

```text
Deadlock Detection

NO DEADLOCK DETECTED
```

### Resource Request Output

```text
REQUEST GRANTED;
System remains safe.
```

*Note: The sample output assumes the sample matrices and an appropriate Request Matrix are entered.*

---

## 12. Algorithms Used

### A. Banker's Safety Algorithm

1. Initialize Work with the Available vector.
2. Calculate the Need Matrix.
3. Find an unfinished process whose Need is less than or equal to Work.
4. Mark that process as finished.
5. Add its allocated resources back to Work.
6. Repeat until all processes finish or no eligible process is found.
7. If all processes finish, the system is safe; otherwise, it is unsafe.

### B. Deadlock Detection Algorithm

1. Initialize Work with Available resources.
2. Check the current outstanding Request Matrix.
3. Find a process whose Request can be satisfied.
4. Mark it as finished.
5. Release its allocated resources into Work.
6. Repeat the process.
7. Any unfinished process is reported as potentially deadlocked.

### C. Resource Request Validation

When a process makes an additional resource request:

1. Check whether the request exceeds its remaining Need.
2. Check whether the requested resources are currently available.
3. Temporarily allocate the resources.
4. Run the safety algorithm.
5. Grant the request only if the resulting state is safe.
6. Otherwise, reject the request.

---

## 13. Expected Results

After successful execution, the simulator displays:

- Calculated Need Matrix.
- Current Available Resources.
- Safe or Unsafe State.
- Safe Sequence, if available.
- Deadlock Detection Result.
- Resource Request Approval or Rejection.

The results help users understand how resource allocation affects process execution.

---

## 14. Applications

The concepts demonstrated in this project are useful in:

- Operating System resource management.
- Process scheduling and resource allocation studies.
- Understanding deadlock avoidance.
- Understanding deadlock detection.
- Operating Systems laboratory practicals.
- Learning algorithm implementation using Python.

---

## 15. Limitations

- This is a console-based educational simulator.
- It does not interact with real operating system resources.
- The results depend on the values entered by the user.
- It does not implement automatic deadlock recovery.
- It does not provide a graphical user interface.

---

## 16. Future Improvements

The project can be improved by adding:

- A graphical user interface using Tkinter.
- Visual representation of resource allocation.
- Automatic generation of test cases.
- Detailed step-by-step algorithm visualization.
- Exporting results into PDF or CSV files.
- More advanced deadlock recovery techniques.

---

## 17. Learning Outcomes

Through this project, I learned:

- How deadlocks occur in operating systems.
- How the Banker's Algorithm works.
- How to calculate the Need Matrix.
- How to identify safe and unsafe states.
- How deadlock detection works.
- How to validate resource requests.
- How to implement operating system concepts using Python.
- How to organize and document a programming project.

---

## 18. Author

**Shalini Sharma**

B.Tech – Computer Science Engineering (Data Analytics)

**Project:** Deadlock Detection & Avoidance Simulator

**Subject:** Operating Systems Lab

**Programming Language:** Python

---

## Conclusion

The Deadlock Detection and Avoidance Simulator is an educational project developed to demonstrate important operating system concepts using Python.

By implementing the Banker's Algorithm and a separate deadlock detection procedure, this project explains how resource allocation can be managed safely and how blocked processes can be identified.

It provides practical understanding of deadlock handling and strengthens programming and problem-solving skills.

---


# decisions 001: what language to use?

## context:

for this project, i need a system that automates hospital tasks. For this, I need a language that can be used for task automation, and for that reason, I've considered a few possibilities:

- python
- JavaScript/TypeScript
- Java
- Bash/Shell
- C#(windows/.NET)
- Ruby

The project aims to create an automation solution for [briefly describe the problem here, e.g., processing monthly reports / integration between APIs X and Y]. The primary objective is to reduce manual intervention, mitigate human error, and ensure process scalability. Although the team has knowledge of JavaScript (Node.js) and C# (.NET), the choice of language should prioritize speed of delivery, ease of maintenance, and the availability of specific libraries for the mapped automation tasks.

## decision:

The programming language chosen for the development of this project is Python.

The decision is based on the maturity of the language's automation ecosystem and the productivity offered by its high-level syntax. Compared to C#, Python dispenses with the verbosity of complex environment configurations; and compared to JavaScript, it offers more robust and "straight to the point" libraries for data and file system manipulation, without the added complexity of the asynchronous model (Event Loop) when this is not the central requirement.

## consequences:

### ✅ Gains (Pros):

- Time-to-Market: Drastic reduction in code writing time and rapid prototyping.
- Library Ecosystem: Immediate access to leading tools such as pandas (data), playwright/selenium (web), and requests (APIs).
- Readability: Ease of use for other team members (or "future self") to perform maintenance without the burden of complex typing or rigid interfaces.
- Portability: Simplified execution across different operating systems (Windows/Linux) with dependencies isolated via virtual environments (venv).

### ⚠️ Losses/Risks (Cons):

- Raw Performance: Python is an interpreted language and slower than C# in CPU-intensive processing (although irrelevant for most workflow automation).
- Flexible Typing: The absence of static typing (as in C#) can hide errors that only appear at runtime, requiring greater discipline in writing tests and using *type hints*.
- Memory Consumption: Tends to be higher than that of applications compiled and optimized in .NET.
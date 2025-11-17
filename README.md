# **Quad**

A command-line **quadratic equation solver** for equations of the form:

```
ax² + bx + c = 0
```

Created because writing the full quadratic formula every time during homework was getting old.

---

## ✨ Features

* Solves quadratic equations quickly
* Displays roots in **fraction form** *and* **decimal form**
* Supports **real and complex solutions**
* Uses **ANSI colored output** for readability
* Input validation and clear error messages

Example output formatting:

```
The solution x1 is:
   Fraction: 4/3
   Decimal : 1.333333
```

---

## 🧠 How it works

Uses the standard quadratic formula:

```
x = (-b ± √(b² - 4ac)) / (2a)
```

Automatically:

* Detects whether discriminant > 0, = 0, or < 0
* Converts exact roots to simplified fractions
* Colors different results for clarity

---

## 🚀 Usage

Run with Python 3:

```bash
python Quad.py
```

Enter coefficients when prompted:

```
Enter coefficient a: 1
Enter coefficient b: -3
Enter coefficient c: -4
```

Output:

```
The solution x1 is:
   Fraction: 4
   Decimal : 4.0
The solution x2 is:
   Fraction: -1
   Decimal : -1.0
```

---

## 📦 Requirements

* Python 3.x (no external libraries needed)

---

## 🧠 Why I made it

I kept getting annoyed writing out the full quadratic formula manually for every problem.
So I wrote a tool that calculates the result instantly, displays fractions cleanly, and looks cool in a terminal with colored output.

---

## ⚠️ Note

This script is meant as a **convenience tool**, not a replacement for learning how quadratics work.
It’ll help check your results, not do your homework *for* you.

---

## 🤝 Contributions

Open to improvements — such as:

* GUI version
* Command-line arguments so it can be used non-interactively
* Parsing full expressions (e.g. `"x^2 + 5x + 6"`)

PRs welcome.

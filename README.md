<!--

# Constant-Time

**Algorithmic Explanation of Constant Time Complexity (O(1))**

This repository provides explanations and examples related to **constant time complexity** in algorithms — specifically what it means for an operation to run in *O(1)* time and how to recognize or design constant-time algorithmic behavior.

---

## 📌 What Is Constant Time (O(1))?

In computer science, an algorithm or operation runs in **constant time** if the amount of time it takes to complete **does not depend on the size of the input**. That is, the execution time remains the same whether the input is small or large.

Example: Accessing an element in an array by index is typically O(1).

---

## 🚀 Key Concepts

- **Definition:** O(1) time complexity means execution time is bounded and **independent of input size**.
- **Examples:**
  - Reading a value from a fixed-index position in an array.
  - Assigning a value to a variable.
- **Non-Examples:**
  - Looping through input elements (e.g., O(n)).
  - Recursive calls that depend on input size.

---

### ✍️ Source Code


```python
"""
AN INTRODUCTION TO CONSTANT TIME COMPLEXITY: O(1)

In Computer Science, Big O Notation is used to describe the performance 
or complexity of an algorithm. Constant Time, denoted as O(1), is the 
gold standard of efficiency

WHATA IS CONSTANT TIME?
It means that the time taken to complete an operation is independent of
the size of the input data (n). Whether you have 10 items or 10 billion items
the execution time remains the same.
"""


def get_first_element(data_list):
    """
    Example 1: Accessing an element in array/list

    This is O(1) because python list are implemented as contigous arrays
    To find the first element, the computer simply looks at the memory address
    of the start of the array. It doesn't matter if the list has 10
    elements or 10000000 elements; the jump to index 0 is instantenous
    """ 

    if not data_list:
        return None
    
    # This single operation is Constant Time

    return data_list[0]




def check_if_even(number):
    """
    Example 2: Basic Arithmetic and Logic

    Mathematical opeartions(addition, multiplication, modula) on a fixed size
    integers are considered O(1). The CPU performs these in a fixed number
    of cycles regardless of what "number" is.
    """

    # Calculation and comparison take the same time regardless of the input size
    return number % 2 == 0




def lookup_in_dictionary(data_dict, key):
    """
    Example 3: Hash Table (Dictionary) Lookup

    Dictionaries in Python use hash tables. When you look up a key
    Python hashes the key to find its bucket immediately.  While there
    are rare "worst-case" scenarios (collisions), the average time
    complexity for a lookp is O(1)
    """

    # Finding the value for a key does not require "searching" through the dict
    return data_dict.get(key)



# ----- DEMONSTRATION -----
if __name__ == "__main__":
    small_list = [i for i in range(10)]
    large_list = [i for i in range(1_000_000)]
    large_dictionary = {
    "user_profile": {
        "id": 1001,
        "name": "Charles Akinnurun",
        "age": 21,
        "gender": "Male",
        "nationality": "Nigerian",
        "location": {
            "country": "Nigeria",
            "state": "Lagos",
            "city": "Ikeja",
            "timezone": "WAT"
        },
        "contact": {
            "email": "charles@example.com",
            "phone": "+2348012345678",
            "socials": {
                "github": "https://github.com/charles",
                "linkedin": "https://linkedin.com/in/charles",
                "twitter": "@charles_dev"
            }
        }
    },

    "education": {
        "institution": "Lagos State University of Education",
        "degree": "B.Sc",
        "field": "Computer Science",
        "level": "Undergraduate",
        "cgpa": 4.2,
        "courses": [
            "Data Structures",
            "Algorithms",
            "Computer Hardware",
            "Operating Systems",
            "Machine Learning"
        ]
    },

    "skills": {
        "programming_languages": [
            {"name": "Python", "level": "Advanced"},
            {"name": "JavaScript", "level": "Intermediate"},
            {"name": "C++", "level": "Beginner"}
        ],
        "data_science": [
            "Pandas",
            "NumPy",
            "Matplotlib",
            "Scikit-learn"
        ],
        "web_development": {
            "frontend": ["HTML", "CSS", "React"],
            "backend": ["Node.js", "Flask"],
            "databases": ["MySQL", "MongoDB"]
        }
    },

    "projects": [
        {
            "project_id": 1,
            "title": "Stock Price Prediction",
            "description": "Machine learning model using regression techniques",
            "tools": ["Python", "yfinance", "Scikit-learn"],
            "status": "Completed"
        },
        {
            "project_id": 2,
            "title": "Big-O Visualizer",
            "description": "Educational project explaining time complexity",
            "tools": ["Python", "Matplotlib"],
            "status": "In Progress"
        }
    ],

    "experience": {
        "internships": [
            {
                "company": "JP Morgan Chase",
                "role": "Virtual Data Science Intern",
                "duration": "2024",
                "type": "Remote"
            }
        ],
        "certifications": [
            "Python for Data Science",
            "Machine Learning Foundations",
            "Git & GitHub"
        ]
    },

    "preferences": {
        "theme": "dark",
        "language": "English",
        "notifications": {
            "email": True,
            "sms": False,
            "push": True
        }
    },

    "system_metrics": {
        "login_count": 245,
        "last_login": "2026-02-06",
        "account_status": "Active",
        "storage_usage_mb": 512.75
    },

    "statistics": {
        "completed_projects": 12,
        "github_repositories": 18,
        "coding_hours_per_week": 35,
        "accuracy_scores": {
            "linear_regression": 0.82,
            "ridge_regression": 0.85,
            "random_forest": 0.91
        }
    }
}
    


    print("----- O(1) Demonstration -----")
    
    # Accessing the first element of the small list
    print(f"Small list first item: {get_first_element(small_list)}")

    # Accessing the first element of the large lits
    # Notice that logically, this take the exact same amount of work for the CPU
    print(f"Large list first item: {get_first_element(large_list)}")


    # Arithmetic is always O(1)
    print(f"Is 500 even? {check_if_even(500)}")
    print(f"Is 999,999,999 even? {check_if_even(999_999_999)}")

    # Get the keys in the large dictionary
    print("----- Keys in the large dictionary -----")
    for key in large_dictionary.keys():
        print(key)





"""
    SUMMARY:
    An algorithm is O(1) if:
    1. It doesn't contain loops that depend on the input size.
    2. It doesn't use recursion that depends on the input size.
    3. It performs a fixed number of operations every time.
"""
```


## 🧠 Why It Matters

Understanding constant-time behavior is crucial for designing **efficient algorithms**, especially in performance-sensitive areas like systems programming, cryptography, and real-time computing.



-->












<!-- # 📘 Constant Time – README -->
<h1 align="center" >Constant Time</h1>


## Overview

**Constant Time** refers to an algorithm whose execution time does not depend on the size of the input.
No matter how large the dataset grows, the operation always takes the same amount of time.

In algorithm analysis, this is represented as:

```
O(1)
```

This is the most efficient time complexity possible.


<a href="/src/main.py">Check out for source code</a>

---

## ⚙️ What Constant Time Means

An operation is constant time if it performs the same number of steps regardless of input size.

For example:

* Accessing an element by index in an array
* Returning the first element of a list
* Checking if a number is even

Even if the array has 10 elements or 10 million, the time taken is the same.

---


<!-- ## 📁 Source Code -->



## 🧠 Python Examples

### Example 1 — Accessing an Element by Index

```python
def get_first_element(arr):
    return arr[0]
```

This always takes one step, so it runs in **O(1)** time.

---

### Example 2 — Checking if a Number is Even

```python
def is_even(n):
    return n % 2 == 0
```

Only one calculation is performed, so the runtime is constant.

---

### Example 3 — Hash Table Lookup (Average Case)

```python
my_dict = {"a": 1, "b": 2, "c": 3}
value = my_dict["b"]
```

Dictionary lookup typically runs in constant time.

---

## ⏱️ Time Complexity Comparison

| Operation Type | Complexity |
| -------------- | ---------- |
| Constant Time  | O(1)       |
| Linear Time    | O(n)       |
| Logarithmic    | O(log n)   |
| Quadratic      | O(n²)      |

Constant time algorithms are always faster than those whose runtime grows with input size.

---

## 👍 Advantages

* Extremely fast and efficient
* Performance unaffected by input size
* Ideal for critical system operations
* Useful in real-time applications

## 👎 Disadvantages

* Rare for full algorithms (usually only small operations)
* Often relies on extra memory (e.g., hash tables)
* Not all problems can be solved in constant time

---

## 📌 When Constant Time Occurs

Constant time operations appear in:

* Array indexing
* Stack push/pop
* Queue enqueue/dequeue
* Hash map lookup (average case)
* Returning a stored value

They are building blocks for efficient algorithms.

---

## 🏁 Summary

Constant time complexity **O(1)** means the runtime never changes as input grows.
It represents the fastest and most scalable type of algorithmic operation and is fundamental to efficient program design.


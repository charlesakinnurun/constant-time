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


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



    # Get the keys in the large dictionary
print("----- Keys in the large dictionary -----")
for key in large_dictionary.keys():
    print(key)
import requests as r

response = r.get("https://api.github.com/users/Parakhatdin/repos")
projects = response.json()
print(projects)

"""for project in projects():
    print(f"Project name {projects}")"""
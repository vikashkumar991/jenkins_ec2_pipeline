from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

# Sample data - you can replace with your actual information
profile_data = {
    "name": "Vikash Kumar Singh",
    "title": "DevOps Engineer",
    "about": "I'm a passionate DevOps professional with expertise in cloud infrastructure, CI/CD pipelines, and automation. I love building scalable and reliable systems.",
    "skills": [
        "AWS/GCP/Azure",
        "Docker & Kubernetes",
        "Terraform & Ansible",
        "CI/CD Pipelines",
        "Python & Bash Scripting",
        "Monitoring & Logging"
    ],
    "experience": [
        {
            "role": "Senior DevOps Engineer",
            "company": "Tech Solutions Inc.",
            "duration": "2020 - Present",
            "description": "Implemented Kubernetes clusters for microservices architecture and automated deployment pipelines."
        },
        {
            "role": "DevOps Engineer",
            "company": "Cloud Innovations",
            "duration": "2018 - 2020",
            "description": "Migrated on-premise infrastructure to AWS and set up monitoring systems."
        }
    ],
    "projects": [
        {
            "name": "Automated Deployment System",
            "description": "Created a zero-downtime deployment system using Kubernetes and ArgoCD."
        },
        {
            "name": "Infrastructure as Code",
            "description": "Developed Terraform modules for provisioning cloud resources across multiple environments."
        }
    ]
}

@app.route("/")
def home():
    return render_template('home.html', data=profile_data)

@app.route("/info")
def info():
    return render_template('info.html', data=profile_data)

@app.route("/profile")
def profile():
    return render_template('profile.html', data=profile_data)

@app.route("/contact")
def contact():
    return render_template('contact.html', data=profile_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
# Docker Deployment

## How to Run Locally

Open PowerShell and run these commands:

```powershell
cd C:\Users\KANISHK\.gemini\antigravity\scratch\streamlit_deployment_demo
pip install -r requirements.txt
streamlit run app.py
```

The app will open in your browser automatically at `http://localhost:8501`


🚀 Zero to Hero: Deploying Python Apps with Docker & Render
This guide is designed to teach you how to take a simple Python application, containerize it with Docker, and deploy it to the web using Render.

📋 Prerequisites
Before we start, verify you have the following accounts and tools:

GitHub Account: Sign up here
Render Account: Sign up here (Login with GitHub recommended)
Git Installed: Download Git
VS Code Installed: Download VS Code
Part 1: Project Setup 🛠️
First, we create the application locally.

Create a folder named deployment-demo.
Open VS Code and open this folder.
Create three essential files:
1. 
app.py
 (The Application)
This is our simple web app using Streamlit.

import streamlit as st
st.set_page_config(page_title="My Deployment App", page_icon="🚀")
st.title("Hello, World! 🌍")
st.write("This application was deployed using Docker and Render.")
if st.button("Celebrate"):
    st.balloons()
2. 
requirements.txt
 (Dependencies)
Tells Python which libraries to install.

streamlit
3. 
Dockerfile
 (The Blueprint)
Tells the server how to build and run our app.

# 1. Base Image: Use a lightweight Python version
FROM python:3.9-slim
# 2. Work Directory: Set the folder inside the container
WORKDIR /app
# 3. System Dependencies (Clean and minimal)
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*
# 4. Copy Requirements & Install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# 5. Copy Application Code
COPY . .
# 6. Expose Port (Streamlit runs on 8501)
EXPOSE 8501
# 7. Healthcheck (Optional but good practice)
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1
# 8. Start Command
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
Part 2: Git & GitHub 🐙
Now we need to save our code to the cloud.

1. Initialize Git
Open the Terminal in VS Code (Ctrl + ~) and run:

git init
2. Add and Commit Files
git add .
git commit -m "Initial commit: App setup"
3. Push to GitHub
Go to GitHub.com -> Click + (top right) -> New repository.
Name it deployment-class-demo.
Do not check "Initialize with README".
Copy the commands shown under "…or push an existing repository from the command line":
git remote add origin https://github.com/YOUR_USERNAME/deployment-class-demo.git
git branch -M master
git push -u origin master
Part 3: Deploy on Render ☁️
Go to the Render Dashboard.
Click New + -> Web Service.
Select "Build and deploy from a Git repository".
Find your repo (deployment-class-demo) and click Connect.
Configure the Service:
Name: my-awesome-app (this will be part of your URL).
Region: Closest to you (e.g., Singapore).
Runtime: Select Docker.
Instance Type: Free.
Click Create Web Service.
Render will now build your Docker image and deploy it. Watch the logs! Once it says "Your service is live", click the URL at the top left.

Part 4: The CI/CD Workflow 🔄
The best part? Updates are automatic.

Make a Change: Open 
app.py
 and change the title:

st.title("Updated Version 2.0! 🚀")
Push the Change:

git add app.py
git commit -m "Update app title"
git push origin master
Watch Magic Happen: Go back to the Render dashboard. You will see it automatically detected the new commit and started a new deployment.

🎓 Key Learnings for Students
Portability: Docker ensures the app runs exactly the same on your laptop and the server.
Automation: Connecting GitHub to Render creates a "Pipeline". You push code, they handle the rest.
Statelessness: Free servers often "sleep". The first load might be slow (cold start), but subsequent loads are fast.
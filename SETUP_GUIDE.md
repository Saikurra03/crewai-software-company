# Complete Beginner Guide - Run This Project

## What Is This Project?

Imagine you have an idea for a website or app, but you don't know how to plan it.
This project is like having a **team of 4 AI experts** who help you:

1. **Project Manager** - Figures out what you need
2. **Software Architect** - Decides what technologies to use
3. **Developer** - Plans how to build it
4. **QA Engineer** - Checks if the plan is good

You just type your idea, and they give you a complete plan!

---

## Part 1: Get Your Free API Key (Cohere)

Before you can run the project, you need an API key from Cohere (the AI company).

### Step 1: Go to Cohere Website
- Open your browser
- Go to: **https://cohere.com**
- Click **"Get Started"** or **"Sign Up"**

### Step 2: Create Account
- Enter your email
- Create a password
- Verify your email (check inbox)
- Log in to your account

### Step 3: Get API Key
- After logging in, you'll see the **Dashboard**
- Look for **"API Keys"** in the left menu
- Click **"Create API Key"**
- Copy the key (it looks like: `cohere_abc123xyz...`)
- **Save it somewhere safe!**

---

## Part 2: Run on Your Computer (Local)

### What You Need
- Python 3.10 or higher installed
- Internet connection
- Your Cohere API key

### Step 1: Download the Project
Open Terminal (Mac) or Command Prompt (Windows) and type:

```bash
git clone https://github.com/Saikurra03/crewai-software-company.git
cd crewai-software-company
```

### Step 2: Install Python Packages
```bash
pip install -r requirements.txt
```
Wait for it to finish (may take 2-3 minutes).

### Step 3: Create the .env File
Create a file called `.env` in the project folder and add your API key:

```
COHERE_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with the key you copied from Cohere.

### Step 4: Run the App
```bash
streamlit run frontend/app.py
```

A browser window will open automatically. That's your app!

---

## Part 3: Deploy Online (Free Hosting)

Make your app available to anyone on the internet using **Streamlit Cloud** (free).

### Step 1: Push Code to GitHub
You already did this! Your code is at:
```
https://github.com/Saikurra03/crewai-software-company
```

### Step 2: Go to Streamlit Cloud
- Open browser
- Go to: **https://share.streamlit.io**
- Click **"Sign up"**
- Sign up with your **GitHub account**

### Step 3: Deploy Your App
1. Click **"New app"**
2. Select your repository: **crewai-software-company**
3. Set **Main file path**: `frontend/app.py`
4. Click **"Deploy"**

### Step 4: Add Your API Key (Important!)
Your app won't work without the API key. Add it like this:

1. In Streamlit Cloud, click on your app
2. Click **"Settings"** (gear icon)
3. Go to **"Secrets"**
4. Add this text:

```toml
COHERE_API_KEY = "your_api_key_here"
```

5. Click **"Save"**
6. Your app will restart automatically

### Step 5: Your App is Live!
You'll get a URL like:
```
https://your-app-name.streamlit.app
```

Share this link with anyone!

---

## Part 4: How to Use the App

### On the Website
1. Type your project idea in the text box
   - Example: "Build a food delivery app"
   - Example: "Create a library management system"
2. Click **"Start Planning"**
3. Wait 1-2 minutes
4. See your complete project plan!
5. Click **"Download Plan"** to save it

### On Your Computer (Terminal)
```bash
python app.py
```
Type your idea when asked, and press Enter.

---

## Part 5: Troubleshooting

### Problem: "API key not found"
**Solution:** Make sure your `.env` file has the correct API key.

### Problem: "Module not found"
**Solution:** Run this again:
```bash
pip install -r requirements.txt
```

### Problem: "Port already in use"
**Solution:** Use a different port:
```bash
streamlit run frontend/app.py --server.port 8502
```

### Problem: App is slow
**Reason:** The AI agents take 1-2 minutes to think. This is normal!

### Problem: "Command not found"
**Solution:** Make sure Python is installed. Check with:
```bash
python --version
```

---

## Quick Reference

| What | Command |
|------|---------|
| Install packages | `pip install -r requirements.txt` |
| Run locally | `streamlit run frontend/app.py` |
| Run on terminal | `python app.py` |
| Get API key | https://cohere.com |
| Deploy free | https://share.streamlit.io |

---

## Need Help?

If something doesn't work:
1. Check the error message
2. Make sure Python 3.10+ is installed
3. Make sure you have internet
4. Make sure your API key is correct
5. Try reinstalling: `pip install -r requirements.txt`

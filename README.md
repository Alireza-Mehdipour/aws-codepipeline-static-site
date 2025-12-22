#  AWS CodePipeline Static Website Deployment

This project demonstrates a fully automated CI/CD pipeline for deploying a static website to Amazon S3 using **AWS CodePipeline**, **AWS CodeBuild**, and **GitHub**.  
It includes automated testing, build version injection, artifact packaging, and S3 static website hosting.

---

## 🏗️ Architecture Overview

**Pipeline Flow:**  
**GitHub → CodePipeline → CodeBuild → S3 (Static Website Hosting)**

###  Components

- **GitHub** – Stores the source code  
- **AWS CodePipeline** – Orchestrates the CI/CD workflow  
- **AWS CodeBuild** – Runs tests, injects build version, and prepares artifacts  
- **Amazon S3** – Hosts the static website  
- **Bash + Python** – Used for testing and version injection  

---

## 📁 Project Structure

```
.
├── app/
│   ├── index.html
│   └── style.css
├── scripts/
│   └── inject_version.py
├── tests/
│   └── app.test.sh
├── buildspec.yml
└── README.md
```

---

##  Features

- Fully automated CI/CD pipeline using AWS CodePipeline  
- Build version injection using Python  
- Pre‑build validation and testing using Bash  
- Automatic deployment to an S3 static website bucket  
- Clean, modular, and production‑ready project structure  

---

##  Testing

The script at `tests/app.test.sh` validates:

- Required files exist  
- Directory structure is correct  

These tests run during the **pre_build** phase in CodeBuild.

---

## 🔧 Build Process (buildspec.yml)

The build pipeline includes:

### **1. Install Phase**
- Prints Python and Bash versions  
- Prepares the environment  

### **2. Pre‑build Phase**
- Executes test scripts  
- Validates project structure  

### **3. Build Phase**
- Generates a timestamped `BUILD_VERSION`  
- Logs build metadata  

### **4. Post‑build Phase**
- Copies files into the `dist/` directory  
- Injects the build version into HTML  
- Prepares final artifacts for deployment  

---

##  Deployment

The final build artifacts are deployed to an **S3 bucket configured for static website hosting**.

---

## 🌐 Live Demo

The static website is deployed to Amazon S3 and available at:

**https://your-bucket-name.s3-website-<region>.amazonaws.com**

(Replace with your actual S3 website endpoint.)

---

##  Summary

This project demonstrates a complete, automated CI/CD workflow for static website deployment using AWS-native services.  
It’s a practical example of DevOps automation, infrastructure best practices, and clean project design.

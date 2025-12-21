# AWS CodePipeline Static Website Deployment

This project demonstrates a fully automated CI/CD pipeline for deploying a static website to Amazon S3 using AWS CodePipeline, AWS CodeBuild, and GitHub as the source repository. It includes automated testing, build version injection, and S3 static website hosting.

---

## Architecture Overview

The pipeline follows this flow:
GitHub → CodePipeline → CodeBuild → S3 (Static Website Hosting)
### Components
- **GitHub** – Source code repository  
- **AWS CodePipeline** – Orchestrates the CI/CD workflow  
- **AWS CodeBuild** – Runs tests, injects build version, prepares artifacts  
- **Amazon S3** – Hosts the static website  
- **Bash + Python** – Used for testing and version injection  

---

## Project Structure
. ├── app/ │   ├── index.html │   └── style.css ├── scripts/ │   └── inject_version.py ├── tests/ │   └── app.test.sh ├── buildspec.yml └── README.md

---

## Features

- Automated CI/CD pipeline using AWS CodePipeline  
- Build version injection using Python  
- Pre-build tests using Bash  
- Automatic deployment to S3  
- Static website hosting enabled  
- Clean, modular project structure  

---

## Testing

The `tests/app.test.sh` script validates:

- Required files exist  
- Directory structure is correct  

CodeBuild runs this script during the **pre_build** phase.

---

## Build Process (buildspec.yml)

The build pipeline performs:

1. **Install phase**  
   - Prints Python and Bash versions

2. **Pre-build phase**  
   - Runs tests  
   - Validates file structure

3. **Build phase**  
   - Generates a timestamped `BUILD_VERSION`

4. **Post-build phase**  
   - Copies files into `dist/`  
   - Injects build version into HTML  
   - Prepares artifacts for deployment  

---

## Deployment

The final artifacts are deployed to an S3 bucket configured for **static website hosting**.

### Example S3 Website Endpoint

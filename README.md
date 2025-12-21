# AWS CodePipeline Static Site with Python and Bash

This project demonstrates a complete CI/CD pipeline on AWS with:

- Source: GitHub
- Build: AWS CodeBuild (Python + Bash scripts)
- Deploy: AWS CodePipeline to an S3 static website bucket

Each commit to `main` triggers the pipeline, runs tests, injects a build version into the HTML, and deploys the result.
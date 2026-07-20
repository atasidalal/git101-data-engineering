## Git101 Capstone: Customer Orders ETL Workflow

This repository contains the baseline starter code for the data engineering team's customer orders ETL pipeline. 

### Core Pipeline Process
1. **Data Ingestion:** Reads the raw customer order data files.
2. **Data Transformation & Normalization:** Processes fields to ensure downstream matching integrity. Specifically, customer email values are trimmed of leading/trailing whitespace and converted to lowercase to prevent duplicate records during identity resolution.
3. **Branch Validation:** This project serves as the Git workflow capstone, validating proper feature branching (`feature/ch10-capstone`), local repository hygiene, and successful automated checks via GitHub Actions.
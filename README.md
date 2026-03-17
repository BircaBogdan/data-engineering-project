# Data Engineering Project (AWS + Power BI)

## Overview

This project demonstrates an end-to-end data pipeline built using Python, AWS RDS (PostgreSQL), and Power BI.

The pipeline simulates a real-world workflow:

* Data generation
* Data ingestion into a cloud database
* Data querying and transformation
* Data visualization

---

## Tech Stack

* Python (data generation & ingestion)
* AWS RDS (PostgreSQL database)
* pgAdmin (database querying)
* Power BI (data visualization)

---

## Data Pipeline Flow

1. **Data Generation**

   * Synthetic dataset created using Python

2. **Data Ingestion**

   * Data uploaded to AWS RDS PostgreSQL database

3. **Data Storage**

   * Structured tables stored in cloud database

4. **Data Querying**

   * SQL queries executed via pgAdmin

5. **Data Visualization**

   * Dashboard built in Power BI

---

## Dashboard Features

* Revenue per product
* Quantity sold per product
* Total revenue KPI

---

## Dashboard Preview

![Dashboard](dashboard.png)

---

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/BircaBogdan/data-engineering-project.git
```

2. Create a `.env` file based on `.env.example`

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the script:

```bash
python upload_data.py
```

---

## Security Note

Sensitive credentials (such as database passwords) are managed using environment variables and are not included in the repository.

---

## Future Improvements

* Add ETL pipeline orchestration (Airflow)
* Automate data ingestion
* Add data validation
* Deploy pipeline to production environment

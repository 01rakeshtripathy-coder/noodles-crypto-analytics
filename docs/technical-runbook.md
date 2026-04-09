# Technical Runbook: Noodles Crypto Analytics

## System Overview

Python-based ETL pipeline loading currency and social engagement data into a SQL data warehouse (NoodlesDW), with Power BI dashboards for executive reporting and analytics.

The system processes JSON data sources, applies transformation and validation, loads into a star schema, and serves aggregated data to Power BI.

---

## Daily Operations

### 1. Manual ETL Execution

```bash
# Activate Python environment
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Run complete pipeline
cd scripts
python run_full_pipeline.py
```

**Expected Duration**: 5–10 minutes

**Success Indicators**:

* Exit code: 0
* Log file shows: "Pipeline Finished Successfully"
* No errors in `logs/` directory

---

### 2. Automated Execution (Cron / Task Scheduler)

#### Linux / Mac (cron)

```bash
# Run daily at 6 AM
0 6 * * * cd /path/to/noodles-analytics/scripts && /path/to/venv/bin/python run_full_pipeline.py
```

#### Windows (Task Scheduler)

* Open Task Scheduler
* Create Basic Task: **Noodles ETL**
* Trigger: Daily at 6:00 AM
* Action: Start program

  * Program: `C:\path\to\venv\Scripts\python.exe`
  * Arguments: `run_full_pipeline.py`
  * Start in: `C:\path\to\noodles-analytics\scripts\`

---

### 3. Power BI Refresh

#### Manual Refresh

* Open Power BI Desktop
* Click **Home → Refresh**
* Wait 30–60 seconds

#### Scheduled Refresh (Power BI Service)

* Configured: Daily at 7:00 AM
* Check dataset → Refresh history
* Investigate failures via gateway logs

---

## Monitoring & Validation

### Check ETL Logs

```bash
# View latest log
tail -n 50 logs/etl_$(date +%Y%m%d)*.log

# Search for errors
grep -i error logs/etl_*.log
```

---

### Validate Data Quality

```bash
python scripts/validate_star_schema.py
```

**Expected Output**:

* ✓ No orphaned records
* ✓ Row counts match expectations
* ✓ Referential integrity checks pass

---

### Check Power BI Service

* Go to: https://app.powerbi.com
* Open workspace: **Noodles Analytics**
* Verify dataset **Last Refresh** timestamp
* Ensure no refresh failures

---

## Troubleshooting

### Issue: Python Import Error

**Symptom**:
`ModuleNotFoundError: No module named 'pandas'`

**Solution**:

```bash
pip install -r scripts/requirements.txt
```

---

### Issue: Database Connection Failure

**Symptom**:
`sqlalchemy.exc.OperationalError`

**Solution**:

1. Ensure SQL Server is running
2. Verify `.env` credentials
3. Test connection:

```python
from etl.load import get_engine
engine = get_engine()
print("Connection successful!")
```

---

### Issue: Staging Tables Empty

**Symptom**:
Row counts = 0

**Solution**:

1. Check JSON files exist in `data/raw/`
2. Verify read permissions
3. Inspect `data/rejects/` for failed records
4. Review ETL logs

---

### Issue: Power BI Refresh Failure

**Symptom**:
"Data source error"

**Solution**:

1. Verify on-premises gateway is running
2. Check gateway logs
3. Validate credentials
4. Reconfigure dataset connection

---

## File Locations

| Resource          | Path         |
| ----------------- | ------------ |
| JSON Files        | `data/raw/`  |
| Python Scripts    | `scripts/`   |
| SQL Scripts       | `sql/`       |
| Logs              | `logs/`      |
| Power BI Reports  | `reports/`   |
| Documentation     | `docs/`      |
| Jupyter Notebooks | `notebooks/` |

---

## Database Information

* **Server**: localhost
* **Database**: NoodlesDW
* **Schemas**: staging, dw
* **Authentication**: Windows / SQL Server

---

## Key Contacts

* **Data Engineer**: [Rakesh Tripathy]
* **Database Admin**: [DBA Name]
* **Business Owner**: [Stakeholder Name]

---

## Backup & Recovery

### Database Backup

```sql
BACKUP DATABASE NoodlesDW
TO DISK = 'C:\Backups\NoodlesDW_Full.bak'
WITH FORMAT, INIT, NAME = 'Full Backup of NoodlesDW';
```

---

### Code Backup

* Version controlled via Git
* Repository: https://github.com/yourname/noodles-analytics
* Branch: main

---

## Operational Notes

* Pipeline is designed to be **idempotent** (safe to re-run without duplication)
* Daily execution ensures fresh data for dashboards
* Aggregation tables optimize Power BI performance
* Validation scripts enforce data integrity before reporting

---

## Success Criteria

* ETL completes without errors
* Data warehouse populated with expected row counts
* Power BI dashboards refresh successfully
* No data quality violations detected

---

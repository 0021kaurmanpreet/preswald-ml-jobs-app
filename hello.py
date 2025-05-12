from preswald import connect, get_df, query, table, text
from preswald import plotly
import plotly.express as px
connect()
df = get_df("1000_ml_jobs_us")  

sql = """
SELECT job_title, company_name, job_posted_date
FROM 1000_ml_jobs_us
WHERE company_address_region = 'California'
ORDER BY job_posted_date DESC
LIMIT 30
"""

filtered_df = query(sql, "1000_ml_jobs_us")

text("# My Data Analysis App-Machine Learning Jobs in USA")
table(filtered_df, title="Filtered Data")

fig = px.bar(filtered_df, x="job_title", color="company_name", title="Job Titles by Company")
plotly(fig)
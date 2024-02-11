# Development deployment
1. Install dependencies `poetry install`
2. Deploy scrapper by executing this commands:
   ```
   cd data_scrapper
   poetry run celery -A scrap_data_task worker -B --loglevel=info
   ```
3. Deploy bot `poetry run python3 main.py`

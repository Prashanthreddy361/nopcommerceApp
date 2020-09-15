pytest -s -v -m "sanity" --html=./Reports/report_sanity.html testCases/ --browser chrome
pytest -s -v -m "regression" --html=./Reports/report_sanity.html testCases/ --browser chrome

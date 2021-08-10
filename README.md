# cars-python-cleaning

cars: client code.

python: languague used in project.

cleaning: main task.



## Context
Client wants to build a database to provide information for automotive industry.

On the day by day the data came in different files and formats so i had to convert to .csv and join them by source.

For the important but not urgent tasks i had to determine first if we should use SQL or noSQL, if SQL then should we go with a OLAP or OLTP.

OLAP was chosen because at the moment we don't fill the requierments for OLTP, even if it's the objective and there will be new relationships that would be difficult to determine without a more traditional schema.

Pandas is used instead of pySpark because data fits the memory.

Open Refine is used for spellcheking.


## Used libraries

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install libraries.

```bash
pip install pandas
pip install numpy
pip install vininfo
```

## Readability

These all are different projects within the same job:
- Bike cleaning
  - No particular order, code is split because i had to read from different sources.
- Country Cleaning
  - Each country is it's own problem and it's saved to .csv to be uploaded to MySQL.
- OCR
  - One particular country's source was in form of images.
- SQL
  - SQL scripts to be used by me or teammates and edited on the moment of query.


## Goal
Extract as much info as possible without lossing data. Each car is it's own entity that can be researched to complete empty columns.

## License
[MIT](https://choosealicense.com/licenses/mit/)
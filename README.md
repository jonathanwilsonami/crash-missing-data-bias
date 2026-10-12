# crash-missing-data-bias

Comparing mean, median and complete-case missing-data treatments on PennDOT crash data under MAR and MNAR.

## Contents

- `missing_data_analysis.ipynb`: the full analysis (data quality, outliers, side-by-side histograms, logistic regression, bias comparison, summary)
- `MAR_ex1.xls`, `MNAR_ex1.xls`: the same 1,000 crashes, with values missing at random (MAR) and missing not at random (MNAR)
- `features.xls`: the full crash extract, used to rebuild a reference "truth" dataset
- `treated_datasets/`: CSVs of each dataset after mean imputation, median imputation and complete-case removal

## Setup

```bash
pip install pandas numpy matplotlib seaborn plotly statsmodels scikit-learn xlrd openpyxl jupyter
jupyter notebook missing_data_analysis.ipynb
```

## Key findings

- Complete-case removal is the most biased treatment, especially under MNAR.
- Mean imputation is the least biased simple method.
- Median imputation turns every missing yes/no value into "no", distorting those variables.
- The treatments differ little in accuracy or F1. The predictors are weak (only speeding is significant).

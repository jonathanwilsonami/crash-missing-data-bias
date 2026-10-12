# crash-missing-data-bias

Missing-data treatments and rural crash severity in PennDOT crash data.

**Project site (paper, slides, notebooks):** https://jonathanwilsonami.github.io/crash-missing-data-bias/

## Contents

- `missing_data_analysis.ipynb`: Part I. Mean, median and complete-case treatments under MAR and MNAR, compared against a reconstructed reference
- `rural_severity_model.ipynb`: Part II. A ten-feature logistic regression for fatal / serious-injury crashes, interpreted for rural roads
- `MAR_ex1.xls`, `MNAR_ex1.xls`, `features.xls`: the crash extracts
- `project-site/`: the Quarto site (`paper.qmd` renders both the paper and the slides)

## Reproduce

```bash
pip install pandas numpy matplotlib seaborn plotly statsmodels scikit-learn xlrd openpyxl jupyter
jupyter nbconvert --to notebook --execute --inplace missing_data_analysis.ipynb rural_severity_model.ipynb
python project-site/scripts/export_assets.py   # copy figures + notebook pages into the site
cd project-site && quarto render               # builds project-site/docs/
```

Pushing to `main` publishes the committed `project-site/docs/` to GitHub Pages.

## Key findings

- Complete-case removal is the most biased missing-data treatment, especially under MNAR. Mean imputation is the least biased simple method.
- On rural roads, aggressive driving contributes the most severe crashes, motorcycles are the most dangerous single factor, and impairment and speeding each raise the odds about 2.4×.

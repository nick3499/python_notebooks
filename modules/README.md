# python_notebooks / modules / README.md
## featured libraries include

 - itertools
 - math
 - numpy
 - matplotlib
 - tornado

Note: when python executes the code example in `csv_life_expectancy_dict.ipynb`, the dict rows output similar to the following example when the dict rows output to Bash CLI:

`{'Indicator': 'Healthy life expectancy (HALE) at birth (years)', 'Country': 'Zimbabwe', 'Comments': '', 'Display Value': '51', 'World Bank income group': 'Low-income', 'Numeric': '51.00000', 'Sex': 'Female', 'High': '', 'Low': '', 'Year': '2012', 'WHO region': 'Africa', 'PUBLISH STATES': 'Published'}`

But Jupyter Notebook outputs the above example incorrectly:

`"OrderedDict([('Indicator', 'Healthy life expectancy (HALE) at birth (years)'), ('PUBLISH STATES', 'Published'), ('Year', '2012'), ('WHO region', 'Africa'), ('World Bank income group', 'Low-income'), ('Country', 'Zimbabwe'), ('Sex', 'Female'), ('Display Value', '51'), ('Numeric', '51.00000'), ('Low', ''), ('High', ''), ('Comments', '')])\n"`

import json
import os
import shutil

import nbconvert

# Create output directory
if os.path.exists('output'):
    shutil.rmtree('output')
os.mkdir('output')

# Read source notebook
with open('example-notebook.ipynb') as f:
    nb = json.load(f)
    
# Loop through cells
for i, c in enumerate(nb['cells']):
    # Look at code cells with tag "solution"
    if not c['cell_type'] == 'code':
        continue
    if not 'tags' in c['metadata']:
        continue
    if not 'solution' in c['metadata']['tags']:
        continue
    nb['cells'][i]['source'] = ['# Write here']

# Create questions and solution notebooks
with open('output/solutions.ipynb', 'w') as f:
    json.dump(nb, f)
shutil.copyfile('example-notebook.ipynb', 'output/questions.ipynb')

# Clear outputs for questions notebook
if nbconvert.__version__ > '6':
    os.system('jupyter nbconvert '
              '--clear-output '
              '--inplace output/solutions.ipynb')
else:
    os.system('jupyter nbconvert '
              '--ClearOutputPreprocessor.enabled=True '
              '--inplace output/solutions.ipynb')


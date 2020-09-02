# Issue-Analysis

Tools:
JQAssistant 1.8: 
- jqa-java-plugin
- jqa-github_issue-plugin
- jqa-git-plugin.

The actual task is to merge different sources like git, java byte code and issues to find cross sectional aspects which are often affected by bugfixes in the application code.


The hotspot analysis consists of 3 steps:

## Text analysis
In order to perform the analysis on a wide range of Java programs and github repos, the respective issues and git commits are analyzed based on their descriptions.
Subsequently, a classification of "bugs and problems" is performed. This has the advantage that no labeling of bugs or errors has to be included in the documentation of the git repo.
For this reason, text analysis mainly refers to the project data collected by Git.

[Text analysis](https://github.com/softvis-research/issue-analysis/blob/master/text_analyse.ipynb)

## Component analysis
The data classified as bugs and errors are associated with the corresponding methods/classes and a statistical analysis is performed, which should display hotspots in the respective areas.
This evaluation includes for example the number of bugs/bugs per method|class, the relevance of the individual methods/classes in relation to the errors.


## Time analysis

Finally, the development of error sources in the project is to be visualized. The development of an error hotspot will be documented chronologically using the Git versioning. By visualizing these temporal developments, the emergence of potential errors is to be tracked and the causes better understood.

[Component and time analysis](https://github.com/softvis-research/issue-analysis/blob/master/components_analyse.ipynb)


### Run all Jupyter Notebooks with binder 
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/softvis-research/issue-analysis/master)
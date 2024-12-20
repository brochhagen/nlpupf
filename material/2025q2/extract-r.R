library(knitr)
require(markdown) #required for md to html

#purl('session.Rmd')
knit('session.Rmd','session.md')
markdownToHTML('session.md','session.html')

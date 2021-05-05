# crypto_portfolio



### Phase 1 Aims
- Deployment of base portfolio to Heroku
- Ability to update portfolio from Heroku
- Ability to review performance of individual and overall portfolio 
- User interfaces to assist with above
- Graphical and Numerical Visualisations of above

# Required files for heroku deployment 
1. setup.sh
2. Procfile
3. requirements.txt

### Phase 1 User Interface Overview

Interface and Actions

1. Would you like to create, add to or update your portfolio in any way.
    i) if yes then take to portfolio update page
        a) what would you like to do.. create a portfolio or update an existing portfolio
        b) complete necessary tasks and save the new portfolio

    ii) if no then take to portfolio analysis page
        a) Would you like to look at an individual coin or overall portfolio performance
        b) if individual ask user for the name of a coin
        c) display visualisation showing performance of the requested metric
        d) display %age change, £ change
        e) display 

2. Enable automatic updates so that the portfolio prices are updated on an hourly basis.
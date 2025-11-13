from pyscript import display


commarts = {'Precones', 'Ramos', 'Banaag', 'Rufo'} # specifying set
display(commarts, target='output')

socsci = {'Ramos', 'Rufo', 'De Mata', 'Ledesma'} 
display(socsci, target='output')

check_commarts = 'Ramos', 'Rufo' in commarts
display(check_commarts, target='output')
check_socsci = 'Ramos', 'Rufo' in socsci
display(check_socsci, target='output')


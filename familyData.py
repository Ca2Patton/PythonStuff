#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python 
import copy

fMovies = []
relatives = {'fname' : None, 'lname' : None, 'favorite movie' : None}
relatives['favorite movie'] = fMovies
immediate = {}
family = {'immediate' : immediate}
immediate['mother'] = copy.deepcopy(relatives)
immediate['father'] = copy.deepcopy(relatives)
immediate['brother'] = copy.deepcopy(relatives)

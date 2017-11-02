#
# Some URL contains #
#

href = 'http://www.ucla.edu/#footer'

idx = href.find('#')
print('href = {}, idx = {}'.format(href,idx))


# cut out the part after "#"

href = href[:idx]
print('href = {}'.format(href))


import webbrowser
import os

from streetview import addr_to_img


N = 8  # number of viewing angles between 0 and 360 degrees
addr = 'Cancun, Mexico'

fp = open('streetview.html', 'w')
fp.write('<html>\n')

for i in range(N):
    angle = i * (360 / N)
    imgfile = 'streetview-'+str(i) + '.jpg'
    addr_to_img(addr, imgfile, heading=angle, verbose=0)
    fp.write('<img src="' + imgfile + '"' + 
             ' alt="view angle "' + str(angle) + ' height="200">\n')

fp.write('</html>')
fp.close()

webbrowser.open_new('file://' + os.path.realpath('./streetview.html'))


import urllib.request
import time
import json

def addr_to_latlng(addr, verbose=0):
    #addr = url_encoding(addr)
    addr = urllib.parse.quote_plus(addr)
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' \
          + addr
    if verbose: print("url = ", url)
    u = urllib.request.urlopen(url)
    data = u.read().decode()
    js = json.loads(data)
    c = js['results'][0]['geometry']['location']

    return c['lat'], c['lng']


def addr_to_img(addr, img_file_name, heading=150, pitch=0, fov=120, \
                size='640x640', verbose=0):

    if not img_file_name.lower().endswith('.jpg'):
        print('image file name must have .jpg')
        img_file_name = img_file_name + '.jpg'
    
    lat, lng = addr_to_latlng(addr, verbose)

    with open('map.key','r') as f:
       key_string = f.read()
    print("Using map key = {}".format(key_string))
    
    url = 'https://maps.googleapis.com/maps/api/streetview?size=' + size \
        + '&location=' + str(lat) + ',' + str(lng)     \
        + '&heading=' + str(heading)    \
        + '&pitch=' + str(pitch)        \
        + '&fov=' + str(fov)            \
        + '&key=' + str(key_string)

    if verbose: print('Google Street view: {}'.format(url))
         
    r = urllib.request.urlopen(url)
    data = r.read()
    r.close()
    with open(img_file_name,'wb') as f:   # 'b' for binary file
        f.write(data)
    
    time.sleep(1)   # don't want to overwhelm google server
    if verbose: print('image written to = {}'.format(img_file_name))
    
if __name__ == '__main__':

   addr_to_img('UCLA Royce Hall', 'streetview.jpg', verbose=0)




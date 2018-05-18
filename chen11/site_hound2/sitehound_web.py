import requests
from bs4 import BeautifulSoup
import os
import time

# requirements:
# pip3 install requests
# pip3 install beautifulsoup4

SITE_URL = 'http://scbx.mssm.edu/sitehound/sitehound-web/cgi'

def fwrite(fname, text, mode='w'):
    file = open(fname, mode, encoding='utf-8')
    file.write(text)
    file.close()

def fappend(fname, text):
    fwrite(fname, text, 'a')

# cut ending
def rchop(s, ending):
  if s.endswith(ending):
    return s[:-len(ending)]
  return s

def log(s):
    fappend('run.log', s + '\n')
    print(s)     

def upload(pdbfile):
    data = {
        'SITE_NAME': 'SITEHOUND',
        'pdb_id': '',
        'probe': 'CMET',   # methyl probe
        'algorithm': 'a',  # averaging clustering 
        'filename': pdbfile,
    }

    log('UPLOADING ' + pdbfile)

    session = requests.session()
    files = {'file': open('../%s' % pdbfile, 'rb')}
    html = session.post(SITE_URL+'/wait1.cgi', data=data, files=files).text
    inputs = BeautifulSoup(html, 'html.parser').find_all('input')
    data = {}
    for item in inputs:
        data[item.get('name')] = item.get('value')
    html = session.post(SITE_URL+'/protein_processing.cgi', data=data).text
    inputs = BeautifulSoup(html, 'html.parser').find_all('input')
    data = {}  
    for item in inputs:
        data[item.get('name')] = item.get('value')
    html = session.post(SITE_URL+'/wait3.cgi', data=data).text
    inputs = BeautifulSoup(html, 'html.parser').find_all('input')
    data = {}
    for item in inputs:
        data[item.get('name')] = item.get('value')
    html = session.post(SITE_URL+'/sitehound.cgi', data=data).text
    url = BeautifulSoup(html, 'html.parser').find('div', id='main').find('a').get('href')

    print('Result URL:', url)

    sleep_seconds = 5 
    max_trials = 120     # 10 min
    trial = 1

    while trial <= max_trials:
        html = session.get(url).text

        fwrite('results/' + pdbfile + '.html', html)    

        if 'Cluster Data' in html:
            # f = open('result/%s.txt' % filename, 'w', encoding='utf-8')
            # result = BeautifulSoup(html, 'html.parser').find('td', {'align': 'center'}).find('table').find_all('tr')
            # for tr in result:
            #     for td in tr.find_all('td'):
            #         f.write(td.get_text().replace('\r', '').replace('\n', '') + '\t')
            #     f.write('\r\n')
            # f.close()

            # download file linked by "[Cluster Data]" link directly
            clust_url = rchop(url, 'output.html') + 'clusters_summary.dat'
            clust_outf = 'results/' + pdbfile + '.clusters_summary.dat' 
            fwrite(clust_outf, session.get(clust_url).text)

            log('OK. FILE %s\n' % pdbfile)
            return
        elif 'An error occurred' in html:
            log('FAILED. FILE %s: (An error occurred)\n' % pdbfile)
            return
        else:  
            trial += 1
            print('sleep... next tiral: ' + str(trial) + '/' + str(max_trials))
            time.sleep(sleep_seconds)
    log('FAILED. TIMEOUT')        

def main():
    log('START\n')

    if not os.path.exists('results'):
        os.makedirs('results')
    
    for pdbfile in os.listdir('../'):
        if pdbfile.endswith(".pdb"):
            try:
                upload(pdbfile)
            except Exception as e:
                log('ERROR ' + pdbfile + ': ' + str(e) + '\n')
    log('\nDONE')        

main()

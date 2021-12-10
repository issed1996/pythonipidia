from django.http import response
import requests
import json

with open('data.json', 'r') as file:
 data=json.load(file)
 servers = data['annuaire']
 topics=data['topics']
 file.close()

urls = ['http://'+str(server)+'ws/annuaire' for server in servers]
for url in urls:

    try:
        #updating urls list
        reponse = requests.get(url)
        contenu=reponse.json()

        for i in contenu:
            if i not in servers:
                #servers.append(i)
                data={
                    'topics':topics,
                    'annuaire':servers
                }
                with open('data.json', 'w') as jsonfile:
                    json.dump(data, jsonfile)
                    
    except: pass



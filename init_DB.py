import json

data={
    'topics':{
    "types" :
      {
       	"définition": ["https://www.geeksforgeeks.org/python-type-function/"],
        "tuto": ["https://www.programiz.com/python-programming/methods/built-in/type"],
        "forum": ["https://github.com/python/typing/discussions"]
      },
    "fonctions" :
    {
     	"définition": ['https://python.doctor/page-apprendre-creer-fonction-en-python'],
        "tuto": ["https://www.programiz.com/python-programming/methods/built-in/type"],
        "forum": ["https://github.com/python/typing/discussions"]
      },
    "fonctions" :
    {
     	"définition": ['https://python.doctor/page-apprendre-creer-fonction-en-python'],
        "astuce": ["https://moncoachdata.com/blog/trucs-et-astuces-en-python/"],
        "exemple": ["http://www.jybaudot.fr/Programmation/pyfcts.html"],
        "bonne pratique": ["https://python.sdv.univ-paris-diderot.fr/15_bonnes_pratiques/"]
    },

    "multithreading" :
      {
       	"exemples": ["url"],
        "piège": ["url"],
        "FAQ": ["url"],
        "définition": ["url"]
   },

    "multithreading" :
      {
        "exemples": ["url"],
        "piège": ["url"],
        "FAQ": ["url"],
     	"définition": ["url"]
      },
    "POO" :
      {
        "tuto": ["url"],
        "exemple": ["url"]
      }
},
'annuaire':['127.0.0.1:8000/']
}



with open('data.json', 'w') as jsonfile:
    json.dump(data, jsonfile)


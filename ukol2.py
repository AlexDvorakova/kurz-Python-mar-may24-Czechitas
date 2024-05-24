import requests
import json

### 1.CAST ### ===czechitas ico: 22834958, klice: obchodniJmeno, sidlo, textovaAdresa
ico = int(input('Zadej ICO:')) 

def informace_subjekt(ico):
    url = f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}"
    response = requests.get(url) 
    
    if response.status_code == 200:
        data = response.json()
        # print(data)

        try:    
            obchodni_jmeno = data['obchodniJmeno']
            adresa = data ['sidlo']['textovaAdresa']
            return obchodni_jmeno, adresa
            
        except KeyError:
            return print ('Chyba v klici.')
        
    else: print ('Chyba pri komunikaci s API.')

   
obchodni_jmeno, adresa = informace_subjekt(ico)
print (f"Obchodni jmeno je: {obchodni_jmeno}.")
print(f'Adresa subjektu je: {adresa}.')


### 2.CAST ### test: Moneta
import requests
import json

def vyhledat_subjekty(nazev):
    url = 'https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat'
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }
    data = json.dumps({'obchodniJmeno': nazev})
    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        return response.json().get('ekonomickeSubjekty', [])
    else:
        print ('Chyba')


nazev = input('Zadejte nazev subjektu:')
subjekty = vyhledat_subjekty(nazev)

if subjekty:
    print('Nalezene subjekty:')
    for subjekt in subjekty:
        print(f'{subjekt.get('obchodniJmeno')}, {subjekt.get('ico')}')
else:
    print('Zadne subjekty nebyly nalezeny.')


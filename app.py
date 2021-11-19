from fastapi import FastAPI, status
import base64
from datetime import datetime

app = FastAPI()

# Génération et envoi de l'ID de traitement
@app.get("/client/scanner/generateur", response_description="Generate treatment ID")
async def createTreatmentId(user: str, scanner: int):

    try :
        # Décodage de l'identifiant utilisateur 
        user_decoded = base64.b64decode(user).decode('ascii')

        # Récupération de la date et transformation du format de la date
        timestamp = datetime.now().strftime("%Y%-j%H%M%S")

        # Concaténation et encodage de notre ID de traitement
        to_encode = user_decoded + str(scanner) + timestamp
        treatmentId = base64.b64encode(to_encode.encode('ascii'))
    
        return {"status": status.HTTP_200_OK, "result": treatmentId}
    
    except: 
        return {"status": status.HTTP_500_INTERNAL_SERVER_ERROR, "message": "Erreur lors du traitement vérifiez les paramètres trasmis et réessayez."}
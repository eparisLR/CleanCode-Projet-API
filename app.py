import base64
from datetime import datetime
from fastapi import FastAPI, status

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

        # Le renvoi de la date sert à pouvoir testé la validation de l'id de traitement
        return {"status": status.HTTP_200_OK, "result": treatmentId, "date": timestamp}
  
    except:
        return {
            "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "message": "Erreur lors du traitement, vérifiez les paramètres transmis et réessayez."
        }



# Vérification de l'ID de traitement
@app.get("/client/scanner/validation", response_description="Validate treatment ID")
async def validateTreatmentId(scanner: str, user: str, date: str, treatmentId: bytes):

    try :
        # Décodage de l'identifiant utilisateur
        user_decoded = base64.b64decode(user).decode('ascii')

        # Concaténation et encodage de notre ID de traitement
        to_encode = user_decoded + scanner + date
        newTreatmentId = base64.b64encode(to_encode.encode('ascii'))

        # Vérification que l'id de traitement transmis correspond à celui recréé
        valid = bool(newTreatmentId == treatmentId)
    
        return {"status": status.HTTP_200_OK, "request": treatmentId, "result": valid}
    
    except:
        return {
            "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "message": "Erreur lors du traitement, vérifiez les paramètres transmis et réessayez."
        }
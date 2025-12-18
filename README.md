# Pràctica de Gestió de Projectes de Software (GPS)

Aquest repositori conté el treball realitzat per a una pràctica de l'assignatura de Gestió de Projectes de Software.

## Objectiu

L'objectiu principal d'aquesta pràctica era familiaritzar-nos amb les eines d'integració contínua (CI) i el seu funcionament. Per a això, hem configurat un pipeline de CI utilitzant GitHub Actions.

## Contingut del Repositori

El projecte consisteix en una senzilla aplicació en Python, juntament amb la configuració necessària per a la seva automatització.

-   `main.py`: Punt d'entrada de l'aplicació.
-   `transform.py`: Mòdul amb lògica de transformació de dades.
-   `test.py`: Proves unitàries per a l'aplicació.
-   `requirements.txt`: Dependències de Python del projecte.
-   `Dockerfile` i `docker-compose.yml`: Configuració per a contenir l'aplicació amb Docker.
-   `.github/workflows/python-app.yml`: Defineix el pipeline d'integració contínua amb GitHub Actions. Aquest pipeline s'encarrega d'executar les proves i construir l'aplicació de forma automàtica.

## Pipeline de CI

El pipeline configurat a GitHub Actions realitza les següents tasques a cada *push* o *pull request* a la branca `main`:

1.  **Configuració de l'entorn**: Prepara un entorn de Python.
2.  **Instal·lació de dependències**: Instal·la les llibreries necessàries des de `requirements.txt`.
3.  **Execució de proves**: Executa les proves unitàries amb `unittest` per assegurar que el codi funciona correctament.

Aquesta pràctica ens ha permès entendre els conceptes bàsics de CI i com aplicar-los en un projecte real.
In dit project heb ik de afgelopen weken gewerkt aan ons eerste proto-type spel met gebruik van Hand-recognition. 
Vanaf de start wilde ik naast het leren van Python, een aantal veel gebruikte bibliotheken eigen maken.
Dit om later via Tensorflow een eigen script te trainen op basis van spraak en camera-detectie. 

In dit project zitten meerdere python-scripts:
1. Gestart met de statische handen detectie om mediapipe te leren (PlaatjeHerkennen)
2. Doorgegeaan met handen-tracker met gebruik webcam (HandTracker)
3. Daarna eerste koppeling van de landmarks gebonden aan een simpel gebaar (LeukNietLeuk)
4. Vervolgens na brainstorm spel challenge-groep gestart met de vingerteller (CountFingers)

Vanuit hier ben ik met de opgedane kennis mezelf verder gaan verdiepen in het spelidee en heb ik geprobeerd een 1e prototype klaar te hebben waarin de Arduino kan samenwerken met de vingerteller in een spel. Dit is de map "CameraTeller" geworden. In dit script ben ik ook de SOLID Single Responsibility gaan toepassen en gaan kijken hoe ik eenmalige acties kan verbinden aan een constante stroom van webcam-data. 

Dit spel "CameraTeller" moet de basis gaan vormen van complexere uitbreidingen, maar heeft uiteindelijk wel de samenwerking tussen meerdere platformen in zich werken. 

# Para crear el ambiente virtual
- Se crea una carpeta del proyecto
- Estando en la terminal, se crea en ambiente 
  
   Windows

   ```py -m venv nombre_venv```

   Linux/Mac

   ```python3 -m venv nombre_venv```

- Para activar el ambiente
  
   Windows

   ```.\venv\Scripts\activate```

   Windows con git bash

   ```source venv/Scripts/activate```

   Linux/Mac

   ```source venv/bin/activate```

- Para desactivar el ambiente
  
   ```deactivate```

- Alternativo: Crear un alias para activar

   ```alias avenv=.\venv\Scripts\activate```
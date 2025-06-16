from flask import Flask, render_template_string  # Importa Flask y la función para renderizar HTML como texto
import pandas as pd  # Importa pandas para leer el archivo Excel
import os

app = Flask(__name__)  # Crea la aplicación Flask

@app.route('/')  # Define la ruta principal (cuando visitas http://localhost:5000/)
def mostrar_excel():
    archivo_excel = 'excel/importacion_final.xls'

    # Lee el archivo Excel usando pandas con el motor 'xlrd' (compatible con archivos .xls)
    df = pd.read_excel(archivo_excel, engine='xlrd')

    # Selecciona solo las primeras 5 columnas del archivo
    df = df.iloc[:, :5]

    # Convierte el DataFrame a una tabla HTML con clases de Bootstrap y le asigna un ID para usar con DataTables
    tabla_html = df.to_html(classes='table table-striped', index=False, table_id="miTabla")

    # HTML completo de la página, con estilos y scripts incluidos
    html = f'''
    <!doctype html>
    <html lang="es">
    <head>
      <meta charset="utf-8">
      <title>Datos del Excel</title>

      <!-- Bootstrap CSS para estilos rápidos -->
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
      
      <!-- DataTables CSS: le da estilos y funciones a la tabla -->
      <link rel="stylesheet" href="https://cdn.datatables.net/1.13.6/css/jquery.dataTables.min.css">
      
      <style>
        /* Estilo general del fondo y texto */
        body {{
          background: linear-gradient(135deg, #71b7e6, #9b59b6);  /* Degradado de fondo */
          color: white;
          min-height: 100vh;
        }}
        h1 {{
          text-shadow: 2px 2px 4px rgba(0,0,0,0.7);  /* Sombra al título */
          margin-bottom: 30px;
        }}
        .container {{
          padding-top: 40px;  /* Espaciado superior */
        }}
        /* Estilo específico para la tabla */
        table.dataTable {{
          background-color: white !important;  /* Fondo blanco */
          color: black !important;  /* Texto negro */
          border-radius: 10px;
          box-shadow: 0 4px 8px rgba(0,0,0,0.1);  /* Sombra */
        }}
      </style>
    </head>
    <body>
      <div class="container">
        <h1 class="text-center">Datos desde Excel</h1>
        {tabla_html}  <!-- Inserta la tabla HTML generada desde pandas -->
      </div>

      <!-- jQuery (requisito para DataTables) -->
      <script src="https://code.jquery.com/jquery-3.7.0.min.js"></script>

      <!-- DataTables JavaScript -->
      <script src="https://cdn.datatables.net/1.13.6/js/jquery.dataTables.min.js"></script>

      <!-- Inicializa DataTables cuando la página esté lista -->
      <script>
        $(document).ready(function() {{
          $('#miTabla').DataTable({{
            paging: true,        // Muestra paginación
            searching: true,     // Activa el campo de búsqueda
            ordering: true,      // Permite ordenar columnas
            language: {{
              // Traduce la interfaz al español
              //url: '//cdn.datatables.net/plug-ins/1.13.6/i18n/es-ES.json'
            }}
          }});
        }});
      </script>
    </body>
    </html>
    '''

    # Devuelve el HTML al navegador
    return render_template_string(html)

# Ejecuta la app si se corre este archivo directamente
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Usa el puerto que Render le asigna
    app.run(host='0.0.0.0', port=port, debug=True)  # Escucha en el puerto adecuado



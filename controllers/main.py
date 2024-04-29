from odoo import http
import pandas as pd
import io
import xlsxwriter
import zipfile

class Main(http.Controller):
    @http.route('/download_excel', type='http', auth='user')
    def download_excel(self):
        # Obtén los registros del modelo
        registros = http.request.env['gestor.clase_inscrita'].search([])

        # Convierte los registros a un DataFrame de pandas
        data = pd.DataFrame([registro.read()[0] for registro in registros])

        # Divide el DataFrame en subconjuntos de 20 registros cada uno
        subconjuntos = [data[i:i+20] for i in range(0, len(data), 20)]

        # Crea un archivo ZIP en memoria
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'a', zipfile.ZIP_DEFLATED, False) as zip_file:
            # Exporta cada subconjunto a un archivo de Excel separado y añádelo al archivo ZIP
            for i, subset in enumerate(subconjuntos):
                excel_buffer = io.BytesIO()
                writer = pd.ExcelWriter(excel_buffer, engine='xlsxwriter')
                subset.to_excel(writer, index=False)
                writer.close()

                excel_data = excel_buffer.getvalue()
                zip_file.writestr(f'archivo_{i+1}.xlsx', excel_data)

        # Prepara los datos del archivo ZIP para la descarga
        zip_buffer.seek(0)
        zip_data = zip_buffer.read()

        # Envía el archivo ZIP al cliente como una descarga
        return http.request.make_response(
            zip_data,
            headers=[
                ('Content-Disposition', 'attachment; filename=archivos.zip'),
                ('Content-Type', 'application/zip'),
            ]
        )

{
    'name': 'stesi_fleet_documents',
    'version': '17.0',
    'author': "Luca Cocozza",
    'application': True,
    'description': "Aggironamento stesi fleet document.",
    'depends': ['stesi_fleet_documents'],
    'data': [
        # # Caricamento delle view,
    ],
    'external_dependencies': {
        'python': ['python-docx', 'docx2pdf', 'pdfkit', 'pydocx'],
    },
}

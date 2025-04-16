from docling.document_converter import DocumentConverter

converter = DocumentConverter()

result = converter.convert("data/docling-technical-report.pdf")

document = result.document

markdown_output = document.export_to_markdown()
json_output = document.export_to_dict()

print(markdown_output)

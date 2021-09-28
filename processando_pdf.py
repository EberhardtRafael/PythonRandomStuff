import PyPDF2

'''
try:
	with open("twopage.pdf", 'rb') as documento:
		documento_origem = PyPDF2.PdfFileReader(documento)
		pagina = documento_origem.getPage(1)
		documento_final = PyPDF2.PdfFileWriter()
		documento_final.addPage(pagina)
		with open("documento_criado.pdf", 'wb') as novo_documento:
			documento_final.write(novo_documento)
		
except IOError:
	pass
'''

with open("lattes.pdf", 'rb') as documento:
	documento_origem = PyPDF2.PdfFileReader(documento)
	with open("wtr.pdf", 'rb') as documentoII:
		documento_origemII = PyPDF2.PdfFileReader(documentoII)
		documento_final = PyPDF2.PdfFileWriter()
		paginaII = documento_origemII.getPage(0)

		for i in range(documento_origem.getNumPages()):
			paginaI = documento_origem.getPage(i)
			paginaI.mergePage(paginaII)
			documento_final.addPage(paginaI)
			
		with open("documento_combinado.pdf", 'wb') as novo_documento:
			documento_final.write(novo_documento)



'''
merger = PyPDF2.PdfFileMerger()
merger.append("twopage.pdf")
merger.append("dummy.pdf")
merger.write("super_documento_criado.pdf")
'''

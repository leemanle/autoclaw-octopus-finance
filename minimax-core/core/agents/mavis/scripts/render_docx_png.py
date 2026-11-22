import fitz
for label in ['8', '9']:
    pdf_path = f'C:/Users/Administrator/Desktop/{label}月.pdf'
    doc = fitz.open(pdf_path)
    print(f'{label}月: {doc.page_count} 页')
    for i in range(doc.page_count):
        page = doc.load_page(i)
        pix = page.get_pixmap(dpi=120)
        out = f'C:/Users/Administrator/Desktop/{label}_p{i+1}.png'
        pix.save(out)
    doc.close()
print('PNG OK')
from pypdf import PdfReader

def show_pdf(path):
    reader = PdfReader(path)

    print("=" * 60)
    print(path)
    print("pages =", len(reader.pages))

    for i, page in enumerate(reader.pages):
        print()
        print("Page", i + 1)

        print("MediaBox =", page.mediabox)
        print("CropBox  =", page.cropbox)
        print("Rotate   =", page.rotation)

        print("Width    =", float(page.mediabox.width))
        print("Height   =", float(page.mediabox.height))

show_pdf("POP_売り切りセール_ロゴなし.pdf")
show_pdf("temp_report.pdf")
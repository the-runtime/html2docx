from io import BytesIO
from docx.document import Document as DocumentObject
from .html2docx import HTML2Docx


def html2docx(content: str, doc: DocumentObject) -> DocumentObject:
    """Convert valid HTML content to a docx document and return it as a
    io.BytesIO() object.
    """
    parser = HTML2Docx(doc)
    parser.feed(content.strip())

    # # buf = BytesIO()
    # # parser.doc.save(buf)
    # return buf
    return doc

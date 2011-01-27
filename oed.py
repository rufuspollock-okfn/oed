'''
Grab original source files from:

pdf: http://www.archive.org/download/oed01arch/oed01arch.pdf
jp2: http://www.archive.org/download/oed01arch/oed01arch_jp2.tar   

Put them inside oed/

cache/ directory is created and used for storing results of processing.

Dictionary
==========

Dictionary itself begins on p.25 of first scan volume.
'''
import os

TIF_DIR = './cache/tif'
PDF_DIR = './cache/pdf'
def ensure_dir(dir):
    if not os.path.exists(dir): os.makedirs(dir)
ensure_dir(TIF_DIR)
ensure_dir(PDF_DIR)

def basename(path):
    basename = os.path.basename(path)
    return os.path.splitext(basename)[0]

def pdf2tif(pdf):
    basename = os.path.basename(pdf)
    outfile = os.path.splitext(basename)[0] + '-%03d.tif'
    outfile = os.path.join(TIF_DIR, outfile)
    first_page = 1
    last_page = 10
    cmd = 'gs -q -dNOPAUSE -dBATCH -dSAFER -r300x300 -sDEVICE=tiffg3 ' + \
        '-dFirstPage=%s -dLastPage=%s ' % (first_page, last_page) + \
        '-sOutputFile="%s" -c save pop -f "%s"' % (outfile, pdf)
    os.system(cmd)

def chop_pdf(in_fp, out_fp):
    '''Chop up the large pdf file (250MB, 1.3k pages) into more manageable
    chunks (gs b0rks on the whole thing).
    '''
    from pyPdf import PdfFileWriter, PdfFileReader

    output = PdfFileWriter()
    input1 = PdfFileReader(file(in_fp, "rb"))
    for ii in range(10):
        output.addPage(input1.getPage(24+ii))
    # finally, write "output" to document-output.pdf
    outputStream = file(out_fp, "wb")
    output.write(outputStream)
    outputStream.close()

def jp22tif(src, dest):
    '''Convert jpeg 2000 documents to tiff.

    Requires imagemagick's convert command line utility.
    
    Remarks: for our purposes this has the disadvantage that a 1.5MB jp2 doc
    becomes a 30MB tiff!
    '''
    cmd = 'convert %s %s' % (src, dest)
    os.system(cmd)

def get_jp2_fp(page_num):
    num = str(page_num).rjust(4, '0')
    fp = 'oed/oed01arch_jp2/oed01arch_%s.jp2' % num
    return fp

def tesseract():
    pass

def main():
    usage = \
'''%prog [options] 

Process oed to plain text.'''
    import optparse
    parser = optparse.OptionParser(usage)
    options, args = parser.parse_args()
    if len(args) > 0:
        pdf2tif(args[0])

def test_pdf_route():
    '''Produces unusable tiffs ...'''
    in_fp = 'oed/oed01arch.pdf'
    out_fp = os.path.join(PDF_DIR, 'chunk1.pdf')
    chop_pdf(in_fp, out_fp)
    pdf2tif(out_fp)

def test_jp2_route():
    src = get_jp2_fp(26)
    dest = os.path.join(TIF_DIR, basename(src) + '.tif')
    jp22tif(src,dest)

if __name__ == '__main__':
    test_jp2_route()


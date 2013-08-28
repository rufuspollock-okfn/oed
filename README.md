Kragen Sitaker did amazing work back in 2005/2006 'liberating' the OED first
edition which is now (mostly) in the public domain and he posted up fairly
good scans of volumes 1-6 on archive.org (see [1], [2]).

The home pages for the six volumes are:

1. http://www.archive.org/details/oed01arch
2. http://www.archive.org/details/oed02arch
3. http://www.archive.org/details/oed03arch
4. http://www.archive.org/details/oed04arch
5. http://www.archive.org/details/newenglishdict05murrmiss
6. (6a) http://www.archive.org/details/oed6aarch
6. (6b) http://www.archive.org/details/oed6barch 

However at the time he was unable to do much on the OCR front (no doubt because
of the poor performance of open source OCR, particularly on such a complex text
as the OED which has lots of non-standard English and font changes). With the
better open source OCR engine it would be possible to convert the OED back into
text and perhaps wikify it to allow for gradual proof-editing and correction.

[1]: <http://blog.okfn.org/2006/03/17/open-version-of-the-oed/>
[2]: <http://lists.canonical.org/pipermail/kragen-tol/2006-March/000816.html>

Install
=======

1. Download source pdfs

    mkdir cache/pdf
    cd cache/pdf
    wget http://www.archive.org/download/oed01arch/oed01arch.pdf

   Note jp2 is also available:
   http://www.archive.org/download/oed01arch/oed01arch_jp2.tar   

2. Install requirements.

   * tesseract for doing ocr. On Debian/Ubuntu:: 

          apt-get install tesseract-ocr

   * python and pypdf

3. Run the script:

      python oed.py


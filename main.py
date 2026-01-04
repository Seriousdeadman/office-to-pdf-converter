import subprocess
from pathlib import Path
import os

downloads = Path(r"D:\Downloads")
libreoffice_path = r"C:\Program Files\LibreOffice\program\soffice.exe"
newest_file = max(downloads.glob('*'), key=os.path.getctime)

office_extensions = ['.docx', '.doc', '.xlsx', '.xls', '.pptx', '.ppt']
if newest_file.suffix.lower() not in office_extensions:
    print(f"Latest file is not an Office document: {newest_file.name}")
    exit()

print(f"Converting: {newest_file.name}")

r = subprocess.run([
    libreoffice_path,
    '--headless',
    '--convert-to', 'pdf',
    '--outdir', str(downloads),
    str(newest_file)
], capture_output=True, text=True)

if r.returncode == 0:
    pdf_name = newest_file.stem + '.pdf'
    pdf_path = downloads / pdf_name
    print(f"✓ Converted successfully: {pdf_name}")

    # Open the PDF with default viewer
    os.startfile(pdf_path)
else:
    print(f"✗ Conversion failed: {r.stderr}")
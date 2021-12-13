# Resume Management System using NER
## Parts Handled
Lim Hang Shen - Search Engine & GUI

Liew Zi Feng - NER

Yong Yung Jun - Data Extraction


## How to run
1. Install requirements - `pip install -r requirements.txt`
2. (optional) If new files are added to `static`, run `setup.py` to do NER on them, it has an optional flag `-f` for the Flair NER engine requiring CUDA
3. (For Linux systems) Run resume.sh - `./resume.sh`

   (For Windows systems) Run resume.bat - `resume.bat`

## Functionality
* Allow user to search for documents via named entities
* Allow user to search for documents with entity type related to query

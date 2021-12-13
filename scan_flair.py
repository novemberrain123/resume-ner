
from ner_flair_pred import flair_predict


def scan_flair():
    directory = "static/"
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            num = filename[-8:-4]
            text = read_pdf(os.path.join(directory, filename))
            f = open(directory + "raw_" + num + ".txt", "w")
            f.write(text)
            f.close()
            s = flair_predict(text)
            f = open(directory + ner + "/" + "ner_" + num + ".txt", "w")
            f.write(s)
            f.close()
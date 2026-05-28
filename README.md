# Docx2Pdf

Script semplice per convertire file `.docx` in PDF, ordinarli in base al numero di lezione e unirli in un singolo PDF finale.

## Descrizione

Lo script cerca i file `.docx` nella stessa cartella di `docx2pdf.py`, li converte in PDF (cartella `pdf/`), li ordina seguendo il numero trovato dopo la parola `LEZIONE` nel nome del file e infine unisce tutti i PDF in `pdf/Risultato_Finale.pdf`.

I file temporanei di Word (che iniziano con `~$`) vengono ignorati e i PDF già presenti nella cartella `pdf` non vengono ricreati (lo script li salta).

## Requisiti

- Python 3.8+
- Microsoft Word installato (su Windows, necessario per `docx2pdf`) 
- Pacchetti Python:

```bash
pip install docx2pdf pypdf
```

Nota: `docx2pdf` utilizza Microsoft Word sul sistema per effettuare la conversione; quindi lo script è pensato per esecuzione su Windows con Word disponibile.

## Uso

1. Copia tutti i file `.docx` nella stessa cartella di `docx2pdf.py`.
2. Esegui lo script:

```bash
python docx2pdf.py
```

3. I PDF convertiti verranno salvati nella sottocartella `pdf/` creata automaticamente. Il file unito finale sarà `pdf/Risultato_Finale.pdf`.

## Ordinamento

Lo script ordina i file cercando nel nome la parola `LEZIONE` seguita da un numero (es. `LEZIONE 03 - Introduzione.docx`). Esempi di nomi riconosciuti:

- `Corso - LEZIONE 01 - Titolo.docx`
- `LEZIONE2 Argomenti.docx` (funziona anche senza spazio)

Se non viene trovato un numero di lezione in un file, quel file viene considerato dopo quelli con numero (viene assegnato un valore predefinito alto nella fase di ordinamento).

## Risoluzione problemi

- Se la conversione di un `.docx` fallisce lo script segnala che il file potrebbe essere in "Visualizzazione protetta". Aprire il file in Word, abilitare la modifica, salvare e chiudere, quindi rieseguire lo script.
- Verificare che non ci siano file `.docx` aperti in Word durante l'esecuzione.

## Esempio rapido

Se nella cartella ci sono i file:

- `LEZIONE 01 - Introduzione.docx`
- `LEZIONE 02 - Capitolo.docx`
- `Appunti.docx` (senza numero di lezione)

L'ordine nell'unione finale sarà: 01, 02, Appunti.

## Output

Il PDF unito viene salvato in:

`pdf/Risultato_Finale.pdf`
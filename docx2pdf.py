import os
import re
from docx2pdf import convert
from pypdf import PdfWriter

def estrai_numero_lezione(nome_file):
    """Estrae solo il numero dopo la parola LEZIONE per un ordinamento perfetto"""
    match = re.search(r'LEZIONE\s*(\d+)', nome_file, re.IGNORECASE)
    if match:
        return int(match.group(1))
    return 999

def converti_e_unisci_ordinato():
    cartella_corrente = os.path.dirname(os.path.abspath(__file__))
    cartella_output_pdf = os.path.join(cartella_corrente, "pdf")
    
    if not os.path.exists(cartella_output_pdf):
        os.makedirs(cartella_output_pdf)

    # 1. Trova i file .docx IGNORANDO i file temporanei nascosti
    lista_docx = [f for f in os.listdir(cartella_corrente) if f.endswith('.docx') and not f.startswith('~$')]
    
    if not lista_docx:
        print("Nessun file .docx valido trovato.")
        return

    # >>> NOVITÀ: ORDINA I FILE DOCX PRIMA DI INIZIARE LA CONVERSIONE <<<
    lista_docx = sorted(lista_docx, key=estrai_numero_lezione)

    print(f"Trovati {len(lista_docx)} file validi. Inizio la conversione in ordine logico...\n")
    
    # 2. Conversione file per file (salta quelli già fatti)
    for docx in lista_docx:
        percorso_docx = os.path.join(cartella_corrente, docx)
        nome_pdf = docx.replace('.docx', '.pdf')
        percorso_pdf = os.path.join(cartella_output_pdf, nome_pdf)
        
        # Se il file è già stato convertito nei tentativi precedenti, lo salta!
        if os.path.exists(percorso_pdf):
            print(f"  -> SALTO: {docx} (PDF già esistente)")
            continue
            
        print(f"  -> CONVERTO: {docx}")
        try:
            convert(percorso_docx, percorso_pdf)
        except Exception as e:
            print(f"\n[!] ERRORE SUL FILE: '{docx}'")
            print("    Il file è bloccato da Windows (Visualizzazione protetta).")
            print("    Soluzione: Apri il file a mano in Word, abilita la modifica, salva e chiudi.\n")
            continue
            
    print("\nConversione completata! Preparo l'unione dei file PDF...\n")
    
    # 3. Raccogli e ordina i PDF per l'unione finale
    lista_pdf = [f for f in os.listdir(cartella_output_pdf) if f.endswith('.pdf')]
    if "Risultato_Finale.pdf" in lista_pdf:
        lista_pdf.remove("Risultato_Finale.pdf")
        
    lista_pdf_ordinata = sorted(lista_pdf, key=estrai_numero_lezione)
    
    # 4. Unisci i file
    merger = PdfWriter()
    print("Ordine di unione nel file finale:")
    for pdf in lista_pdf_ordinata:
        percorso_pdf = os.path.join(cartella_output_pdf, pdf)
        numero_rilevato = estrai_numero_lezione(pdf)
        print(f"  [Lezione {numero_rilevato:02d}] -> Aggiunto")
        merger.append(percorso_pdf)
        
    # 5. Salva il file finale
    percorso_output_finale = os.path.join(cartella_output_pdf, "Risultato_Finale.pdf")
    with open(percorso_output_finale, "wb") as file_output:
        merger.write(file_output)
        
    print(f"\nFatto! Il PDF unito e perfettamente ordinato è in: {percorso_output_finale}")

if __name__ == "__main__":
    converti_e_unisci_ordinato()
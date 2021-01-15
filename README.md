# UnRar_Multiple_Protected_Files
Script che estrae file RAR con diverse password automaticamente.

# Utilizzo
   1) Scaricare e inserire lo script nella cartella in cui si trovano i file RAR;
   2) Creare un file .txt contenente tutte le password dei file rar ordinate come i file;
   3) Sostituire il path del file contenente le password con quello del file da voi appena creato;
   4) Avviare lo script e attendere che si concluda.

# Realizzazione
Per la realizzazione sono state usate le librerie:
   1) os : per lanciare il comando che si occuperà di estrarre il file;
   2) Path : per poter prendere i nomi dei file RAR da estrarre.
   
Il tool utilizzato per estrarre i file è unrar, un tool di sistema installabile facilmente con il comando "sudo apt-get install unrar" nella maggior parte delle distribuzioni Linux.

# Funzionamento
Lo script una volta eseguito apre il file contenente le password e li estrae inserendoli in una lista.
Fa partire un ciclo che scorre tutti i file rar all'interno della directory.
Per ogni file viene fatta l'estrazione degli elementi prendendo la password dal file txt.

# N.B.
   I file e le password devono avere lo stesso ordine, così che il ciclo funzioni.
   E.X.:
    File1    Password1
    File2    Password2
    ...      ...

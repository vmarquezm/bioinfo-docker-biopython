from Bio import SeqIO
import sys

def analizar_fasta(fasta_path):
    for registro in SeqIO.parse(fasta_path, "fasta"):
        seq = registro.seq
        print(f"> {registro.id}")
        print(f" - Largo: {len(seq)}")
        if set(seq.upper()) <= {"A", "T", "G", "C"}:
            gc = 100 * float(seq.count("G") + seq.count("C")) / len(seq)
            print(f" - Contenido GC: {gc:.2f}%")
        else:
            print(" - Secuencia no es ADN, contenido GC no calculado.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python analisis.py archivo.fasta")
        sys.exit(1)
    analizar_fasta(sys.argv[1])

from PIL import Image
from tkinter import Tk, filedialog
import threading
import  time

def processar_faixa(imagem, imagem_pb, inicio, fim):
    """Processa uma faixa horizontal da imagem e aplica a conversão para preto e branco."""
    largura, _ = imagem.size
    for x in range(largura):
        for y in range(inicio, fim):
            r, g, b = imagem.getpixel((x, y))
            luminancia = int(0.299 * r + 0.587 * g + 0.114 * b)
            imagem_pb.putpixel((x, y), luminancia)

def converter_para_preto_e_branco_manual():
    try:
        root = Tk()
        root.withdraw()

        caminho_imagem = filedialog.askopenfilename(
            title="Selecione uma imagem",
            filetypes=[("Imagens", "*.jpg *.jpeg *.png *.bmp *.gif"), ("Todos os arquivos", "*.*")]
        )

        if not caminho_imagem:
            print("Nenhuma imagem foi selecionada.")
            return

        imagem = Image.open(caminho_imagem)
        imagem = imagem.convert("RGB")  # Garante que a imagem esteja no modo RGB
        largura, altura = imagem.size
        imagem_preto_branco = Image.new("L", (largura, altura))

        num_threads = 4  # Definindo o número de threads
        threads = []
        faixa_altura = altura // num_threads

        inicio_tempo = time.time()

        for i in range(num_threads):
            inicio = i * faixa_altura
            fim = altura if i == num_threads - 1 else (i + 1) * faixa_altura
            thread = threading.Thread(target=processar_faixa, args=(imagem, imagem_preto_branco, inicio, fim))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        fim_tempo = time.time()

        caminho_saida = filedialog.asksaveasfilename(
            title="Salvar imagem em preto e branco",
            defaultextension=".jpg",
            filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png"), ("Todos os arquivos", "*.*")]
        )

        if not caminho_saida:
            print("Operação de salvamento cancelada.")
            return

        # Salva a imagem em preto e branco no caminho especificado

        imagem_preto_branco.save(caminho_saida)
        print(f"Imagem convertida com sucesso! Salva em: {caminho_saida}")
        print(f"Tempo de execução com threads: {fim_tempo - inicio_tempo:.4f} segundos")

    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")

# Exemplo de uso

if __name__ == "__main__":
   converter_para_preto_e_branco_manual()

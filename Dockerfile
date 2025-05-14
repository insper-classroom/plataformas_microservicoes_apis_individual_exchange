FROM python:3.11.3-slim

# 2. Define diretório de trabalho
WORKDIR /app

# 3. Copia arquivos do projeto
COPY . .

# 4. Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# 5. Expõe a porta padrão do Uvicorn
EXPOSE 8000

# 6. Comando para rodar o servidor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
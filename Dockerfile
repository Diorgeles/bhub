FROM python:3.12-alpine

# Essa variável de ambiente é usada para controlar se o Python deve 
# gravar arquivos de bytecode (.pyc) no disco. 1 = Não, 0 = Sim
ENV PYTHONDONTWRITEBYTECODE 1

# Define que a saída do Python será exibida imediatamente no console ou em 
# outros dispositivos de saída, sem ser armazenada em buffer.
# Em resumo, você verá os outputs do Python em tempo real.
ENV PYTHONUNBUFFERED 1

COPY . /backend
WORKDIR /backend

RUN apk add --no-cache bash
RUN pip install -r requirements/base.txt
EXPOSE 8000

CMD ["./commands.sh"]

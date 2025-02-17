FROM ubuntu:latest
RUN apt-get update && apt-get install -y python3 python3-pip
WORKDIR /app
COPY . .
RUN pip install --break-system-packages -r requirements.txt
EXPOSE 8000
CMD ["python3", "app.py"]

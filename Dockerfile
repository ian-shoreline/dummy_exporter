FROM python
# Prometheus server exposed on 8000
EXPOSE 8000
# WORKDIR should be root
WORKDIR /
ADD main.py .

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]
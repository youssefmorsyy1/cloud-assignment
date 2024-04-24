FROM python:3.9
WORKDIR /app
COPY paragraphs.txt .
COPY cloud.py .
RUN pip install nltk
CMD [ "python","cloud.py" ] 
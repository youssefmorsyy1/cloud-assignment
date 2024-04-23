FROM python:3.9
WORKDIR /app
COPY paragraphs.txt .
COPY cloud.ipynb . 
RUN pip install nltk
RUN python -m nltk.downloader stopwords punkt stopwords
CMD [ "python","cloud.ipynb" ] 









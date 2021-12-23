FROM python:3.8.2-slim

COPY app.py .
COPY nltk_summarization.py .
COPY spacy_summarization.py .
COPY spacy_summarizer.py .
COPY assets/logo.png .
COPY static/css/custom.css .
COPY static/css/materialize.css .
COPY static/css/materialize.min.css .
COPY static/js/init.js .
COPY static/js/materialize.js .
COPY static/js/materialize.min.js .
COPY templates/index.html .
COPY templates/compare_summary.html .
COPY requirements.txt .

RUN python -m spacy download en_core_web_sm
RUN pip install -r requirements.txt

CMD python app.py --server.port=8050 --server.address=0.0.0.0 --logger.level error
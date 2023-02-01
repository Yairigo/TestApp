FROM python:3.8-slim
# Pip installs vulnerable versions of modules
# Urllib3 1.23 https://security.snyk.io/package/pip/urllib3/1.23
# Requests 2.19.1 https://security.snyk.io/package/pip/requests/2.19.1
# Certifi 2022.9.24 https://security.snyk.io/package/pip/certifi/2022.9.24
# Pyyaml 5.3.1 https://security.snyk.io/package/pip/pyyaml/5.3.1
# cryptography 38.0.2 https://security.snyk.io/package/pip/cryptography/38.0.2
# loguru 0.5.3 https://security.snyk.io/package/pip/loguru/0.5.3
# scrapy 2.5.1 https://security.snyk.io/package/pip/scrapy/2.5.1
# priority 1.1.1 https://security.snyk.io/package/pip/priority/1.1.1
# lxml 4.6.4 https://security.snyk.io/package/pip/lxml/4.6.4
# Twisted 22.8.0 https://security.snyk.io/package/pip/twisted/22.8.0

RUN pip install --upgrade pip && pip install --no-cache-dir urllib3==1.23 requests==2.19.1 certifi==2022.9.24 pyyaml==5.3.1 cryptography==38.0.2 loguru==0.5.3 scrapy==2.5.1 priority==1.1.1 lxml==4.6.4 twisted==22.8.0

COPY pystress.py /app/pystress.py

CMD ["python", "/app/pystress.py"]
FROM python
WORKDIR /PTask/
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV ENV=dev
CMD python -m pytest -s --alluredir=allure_result_folder/ /PTask/tests


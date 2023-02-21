FROM robd003/python3.9
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
# RUN apt-get update && apt-get upgrade -y && apt-get install python3.9 python3.9-venv -y 
EXPOSE 5000
WORKDIR /usr/app
COPY requirments.txt requirments.txt  
RUN python3.9 -m venv venv
RUN source venv/bin/activate
RUN pip install -r requirments.txt
COPY app.py ./

CMD ["python3.9", "app.py"]
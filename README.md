## Steps for running in local system
**STEP-1**: Clone the repo to your local system:
```
git clone https://github.com/SubhamZap/sentence-similarity.git
```

**STEP-1**: Install all the dependencies mentioned in requirements.txt file. You can run the following command in your command prompt to install all the dependencies:
```python
pip install -r requirements.txt
```

**STEP-2:** After installing all the dependencies, open command prompt from the direction where main.py file is present and run the following command:

```python
python main.py
```

**STEP-3:** Open Postman and copy the below curl:
```curl
curl --location 'http://127.0.0.1:5000/score' \
--header 'Content-Type: application/json' \
--data '{
    "text1": "terror suspects face arrest",
    "text2": "nuclear body seeks new tech"
}'
```
That's it, you can hit the above curl to get the .
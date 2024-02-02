import numpy as np
import boto3
import json

s3 = boto3.client('s3')
bucket = 'glove-embedding'

try:
    response = s3.get_object(Bucket=bucket, Key='glove.6B.300d.txt')
    content = response['Body'].read().decode('utf-8')

    embeddings_index = {}
    for line in content.split('\n'):
        if line.strip():
            try:
                values = line.split(' ')
                if len(values) >= 2:
                    word = values[0]
                    coefs = np.asarray(values[1:], dtype='float32')
                    embeddings_index[word] = coefs
                else:
                    print(f"Invalid line: {line}")
            except Exception as e:
                print(f"Error processing line: {line}. Error: {e}")
        else:
            print(f"Invalid line2: {line}")
except Exception as e:
    print(f"Error fetching S3 object. Error: {e}")
glove_words =  set(embeddings_index.keys())

def convert_sen_to_vec(sentence):
    vector = np.zeros(300) # as word vectors are of zero length
    cnt_words =0; # num of words with a valid vector in the sentence
    try:
        for word in sentence.split():
            if word in glove_words:
                vector += embeddings_index[word]
                cnt_words += 1
        if cnt_words != 0:
            vector /= cnt_words
        return vector
    except Exception as e:
        print('convert_sen_to_vec error: ', e)

def cosine(u, v):
    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v)) 

def evaluate_sim_score(text1, text2):
    text1_emb = convert_sen_to_vec(text1)
    text2_emb = convert_sen_to_vec(text2)
    score = cosine(text1_emb, text2_emb)
    return score

def handler(event, context):
    try:
        print('event:', event)
        # Check if the request has a body
        if 'body' in event:
            # Parse the JSON body
            request_body = json.loads(event['body'])
            text1 = request_body.get('text1')
            text2 = request_body.get('text2')
        else:
            # If no body is present, look for query parameters
            text1 = event.get('text1')
            text2 = event.get('text2')

        # Check if text1 and text2 are present
        if text1 is None or text2 is None:
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'Missing required parameters: text1 and text2'})
            }

        # Now you can proceed with your similarity score calculation
        score = evaluate_sim_score(text1=text1, text2=text2)

        return {
            'statusCode': 200,
            'body': json.dumps({'similarity score': score})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': f'{e}'})
        }
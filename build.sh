docker build -t sentence-similarity .
docker tag sentence-similarity:latest 923812021176.dkr.ecr.ap-south-1.amazonaws.com/sentence-similarity:latest
docker push 923812021176.dkr.ecr.ap-south-1.amazonaws.com/sentence-similarity:latest
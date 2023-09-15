# AI Piping Development Task

This project demonstrates a simple app that displays 3 recommendations to do in a country given a season.

The tech stacked used here is React for the frontend, FastAPI for the backend calling the OpenAI API.


# How to run this project

1. Clone this project

```
git clone https://github.com/Vasallius/fastapi-openai-demo.git
```

2. Create credentials.py

```
cd .\fastapi-backend\
cd app
mkdir credentials.py
```

Inside credentials.py, set api_key variable to openai api key

api_key = "your-openai-api-key"

3. Go back to fastapi-backend and build the docker image

```
docker image build --tag myimage .
```

4. Run the server/container

```
docker container run --publish 80:80 --name my-container my-image
```

This server should now be available at local host, try this: http://localhost/stream?country=spain&season=spring

5. Go to `react-frontend` and install packages and view the app

```
npm install
npm run dev
```

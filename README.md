# personalizehn
- View this repository in NBViewer [here](https://nbviewer.org/github/jhojin7/personalizehn/tree/main/)

## Objective
- Use natural language processing techniques to implement a recommendation model from user data.

## Key Results
- Try some well-known text preprocessing techniques.
- Use cosine similarity, LDA, and other techniques.
- Implement incremental learning and continuous deployment at regular interval as new data is aggregated.
- User customized. GitHub login.

## Resources
- https://huggingface.co/datasets/julien040/hacker-news-posts

## TODO
- [] Refactor. variable naming.
- [] Dockerize 
- [] Automatic deployment to OC with GitHub Actions
- [] GitHub login and user-specific personalized data.



```
curretn top page crawl
## use cosine sim
X_cur = current top page embedding
X = embedding of all past dataset
cos sim(X_cur, X)
각 x_cur에 대한 prob의 avg를 사용.

## use topic modeling
x_new embedding화.
calculate point coordinates for new text
get nearest topic's representing data


```
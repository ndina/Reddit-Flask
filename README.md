# Simple [Reddit](https://www.reddit.com/) clone using [Flask](http://flask.pocoo.org/) framework


## Prerequisites

Make sure you have Python 3 on your system


### Build with:
- ```Flask``` as the web framework.
- ```bootstrap-journal``` to make them beautiful.
- ```virtualenv``` emcompasses everything.
- ```MySQL``` for database.
- ```pytest, unittest``` for testing.


### Features:
- ```subreddits``` 
- ```user karma``` 
- ```search``` 
- ```upvoting``` 
- ```downvoting```
- ```comments```
- ```user history```
- ```collections```
- ```feed```




## Build Instructions

A step by step series of examples to get  development running

##### Step 1. Clone this repository simply by typing:

```
$ git clone https://github.com/ndina/Reddit-Flask.git
```

##### Step 2. Create a Virtual Environment and Install Dependencies

```
$ virtualenv venv
$ source venv/bin/activate
```
##### Step 3.  Install the project dependencies, which are listed in ```requirements.txt```.


```
(venv) $ pip install -r requirements.txt
```

##### Step 4. Run the Server
```
(venv) $ python3 run.py
```
##### Step 5. Finally project will be able at:
```
http://localhost:5000/
```



## Testing

Explanation how to run the automated tests for this system

##### testing using [pytest](https://docs.pytest.org/en/latest/)

```
$ pytest -m <test-name>.py
```

##### testing using [unittest](https://docs.python.org/3/library/unittest.html)

```
$ python -m unittest tests/unittest_sample.py
```


















## Docker
You can use `docker run` command and run an app on any machine:
```
$ docker run -p 4000:80 dina2505/redditclone
```

 

## Author

*  **[Dina Nassyrkhan](https://github.com/ndina)**




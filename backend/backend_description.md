## The data base description:

The data base is Elasticsearch. Has the following architecture:

### Index: twitter  
#### Document: twitter_data
{  
id: int8,  
news_text: text,  
twitter_page text,  
twitter_tag text,  
twitter_name text,  
news_created_at timestamp,  
latitude: float,  
longitude: float,  
positive_probability float,  
negative_probability float,  
}

#### Document: twitter_account
{  
id: int8,
twitter_name: text,  
twitter_tag: text,  
twitter_page: text,  
country text,  
city text,  
longitude float,  
latitude float,  
language float,  
max_twitter_id int8  
}

#### Index: user
#### Document: user_information